import math as math
import numpy as np
from enum import Enum
from numpy import *
#from os import *
import rocket as mmr

#enumeration for constants
class cnst(Enum):
    G=0
    RE=1    
    DE=2
    ME=3
    MM=4
    MS=5
    MMARS=6
    DEM=7

#enumeration for state variables
class st(Enum):
    T=0    
    XE=1    
    YE=2
    VXE=3
    VYE=4
    XM=5
    YM=6
    VXM=7
    VYM=8
    VXS=9
    VYS=10
    XS=11
    YS=12
    XMA=13
    YMA=14
    VXMA=15
    VYMA=16
    X=17
    Y=18
    VX=19
    VY=20
    
#enumeration for state variables
class ctl(Enum):
    DT=0
    NS=1   #NUMBER OF STEPS
    SINT=2   #SAVE INTERVAL
    FX=3    # FORCE X DIRECTION
    FY=4    # FORCE Y DIRECTION
    MR=5    # rocket mass
    
def setconst():
#function [state, const, control]=initmarsmission()
#%% Initialise parameters for rocket to the moon
#% will eventually take inputs e.g. read arguments from file

#const.G=6.67e-11; %gravitational constants SI units
#const.re=6.3781e6; %radius of the earth metres
#const.de=2*6.3781e6; %diameter of the earth metres
#const.me=5.97237e24; %earth mass kg
#const.mm=7.342e22; %moonmas kg
#const.ms=1.99e30; %mass sun
#const.mmars=6.42e23 ; %mass mars
#const.dem=381.5e6; %average dist moon-earth metres

    const={}
    const[ cnst.G]=6.67e-11
    const[cnst.RE]=6.3781e6 
    const[cnst.DE]=2*6.3781e6
    const[cnst.ME]=5.97237e24
    const[cnst.MM]=7.342e22
    const[cnst.MS]=1.99e30
    const[cnst.MMARS]=6.42e23
    const[cnst.DEM]=381.5e6
    
    return const
    


# In[13]:


class marsmission(object):

    const=setconst()
    state={}
    control={}
    rocket={}
    maxforce=100000
    
    def __init__(self, control, state):
        self.control = control
        self.state = state

        

    
    def __init__(self, missionfile):
        status=loadmission(missionfile)
        if status!=0:            
            self.setdefaultstate()

    
    def __init__(self):
        self.setdefaultstate()

    def setrocket(self, irocket):
        self.rocket=irocket
    
    def setdefaultstate(self):
        control={}
        #control[ctl.DT]=float(3000)
        control[ctl.DT]=float(0.00001) #keep sim running vvve....eeeer..rrrr...yyyy slow.....llllll...y
        control[ctl.NS]=100000 
        control[ctl.SINT]=100000
        control[ctl.FX]=float(0) #FX FY forces in x and Y direction
        control[ctl.FY]=float(0)
        control[ctl.MR]=float(1)  #mass of rocket        
        
        state={}
        state[st.T]=float(0.0)
        
        #earth
        state[st.XE]=float(0.0)
        state[st.YE]=float(0.0)
        state[st.VXE]=float(30000.0)
        state[st.VYE]=float(0.0)
        
        #moon
        state[st.XM]=float(381.5e6)
        state[st.YM]=float(0.0)
        state[st.VXM]=state[st.VXE]
        state[st.VYM]=1023.1+state[st.VYE] 
        
        #sun
        state[st.XS]=float(0.0)
        state[st.YS]=float(149.6e9)
        state[st.VXS]=float(0.0)
        state[st.VYS]=float(0.0)        
        
        #rocket
        state[st.X]=float(0.0)
        state[st.Y]=float(6.3781e6+50000)
        state[st.VX]=float(90.0+state[st.VXE])
        #state[st.VY]=float(40000.0+state[st.VYE])
        state[st.VY]=float(13000.0+state[st.VYE])
        
        #mars
        state[st.XMA]=float(0.0)
        state[st.YMA]=float(225.0e9+state[st.YS])
        state[st.VXMA]=-24130.0
        state[st.VYMA]=0         
       
        self.control = control
        self.state = state


    def getallstates(self):
        return self.state
        
    def setstate(self,id,val):
        self.state[id]=val
        
    def setcontrol(self,id,val):
        self.control[id]=val
        
    def getstate(self,id):
        return self.state[id]
        
    def getcontrol(self,id):
        return self.control[id]

    def updaterocket(self):
        #update the rocket properties
        self.maxforce=100*self.rocket.rockprop[mmr.rck.NE]*self.rocket.rockprop[mmr.rck.EP] #e.g. 4
        
        #how much fuel used
        fx=self.control[ctl.FX]
        fy=self.control[ctl.FY]
        totalf=math.sqrt(fx**2+fy**2)
        if self.rocket.payload[mmr.payld.FUEL]>0:
            fuelused=0.0000001*self.control[ctl.DT]*totalf*self.rocket.rockprop[mmr.rck.NE]*self.rocket.rockprop[mmr.rck.EP]/self.maxforce        
            #update fuel remaining
            self.rocket.payload[mmr.payld.FUEL]=self.rocket.payload[mmr.payld.FUEL]-fuelused
        else:
            self.maxforce=0
        
        #revise maxforce if not much fuel remaining!
        fuelremaining=self.rocket.payload[mmr.payld.FUEL]
        fuelused=10*self.control[ctl.DT]*totalf*self.rocket.rockprop[mmr.rck.NE]*self.rocket.rockprop[mmr.rck.EP]*totalf/self.maxforce
        if (fuelused>fuelremaining) & (self.control[ctl.DT]>0):
                #recalculatemax force
                self.maxforce=fuelremaining/(10*self.control[ctl.DT]*self.rocket.rockprop[mmr.rck.NE]*self.rocket.rockprop[mmr.rck.EP])
        
        
        #update remaining oxygen
        self.rocket.payload[mmr.payld.OXY]=self.rocket.payload[mmr.payld.OXY]-0.0000001*self.control[ctl.DT]*self.rocket.payload[mmr.payld.CREW]
        
        #update water  #plants use water too!
        self.rocket.payload[mmr.payld.H2O]=self.rocket.payload[mmr.payld.H2O]-0.0000001*self.control[ctl.DT]*self.rocket.payload[mmr.payld.CREW]        
        self.rocket.payload[mmr.payld.H2O]=self.rocket.payload[mmr.payld.H2O]-0.00000001*self.control[ctl.DT]*self.rocket.payload[mmr.payld.PLNT]        
        
        #update food
        self.rocket.payload[mmr.payld.FOOD]=self.rocket.payload[mmr.payld.FOOD]-0.00000001*self.control[ctl.DT]*self.rocket.payload[mmr.payld.CREW]        
        
        #plants make oxygen 
        self.rocket.payload[mmr.payld.OXY]=self.rocket.payload[mmr.payld.OXY]+0.00000001*self.control[ctl.DT]*self.rocket.payload[mmr.payld.PLNT]
        
        #plants use water
        
        #update mass
        self.rocket.updatemass()
        
    def updatestate(self):
        #print('hello')
        newstate=self.state
        #newstate[st.XE]=newstate[st.XE]+10
        #print(newstate[st.XE])
        #print('goodbye')
        
        
        #update rocket
        gx=0
        gy=0
        #rocket-earth
        gt=self.gravaccel(newstate[st.X],newstate[st.XE],newstate[st.Y],newstate[st.YE],self.const[cnst.ME]) #earth contrib
        gx=gx+gt[0];
        gy=gy+gt[1];        
        
        #rocket-moon
        gt=self.gravaccel(newstate[st.X],newstate[st.XM],newstate[st.Y],newstate[st.YM],self.const[cnst.MM]) #moon contrib
        gx=gx+gt[0];
        gy=gy+gt[1];   
        
        #%rocket-sun
        gt=self.gravaccel(newstate[st.X],newstate[st.XS],newstate[st.Y],newstate[st.YS],self.const[cnst.MS]) #sun contrib
        gx=gx+gt[0];
        gy=gy+gt[1];
       
        #%rocket-mars
        gt=self.gravaccel(newstate[st.X],newstate[st.XMA],newstate[st.Y],newstate[st.YMA],self.const[cnst.MMARS]) #moon contrib
        gx=gx+gt[0];
        gy=gy+gt[1]; 

        massr=self.rocket.updatemass()
        self.control[ctl.MR]=massr                       
        gx=gx+self.control[ctl.FX]/self.control[ctl.MR]
        gy=gy+self.control[ctl.FY]/self.control[ctl.MR]
       
        #calculate vy
        newvy=newstate[st.VY]-gy*self.control[ctl.DT];
        newvx=newstate[st.VX]-gx*self.control[ctl.DT];

        #calculate x and y
        newstate[st.X]=newstate[st.X]+0.5*(newstate[st.VX]+newvx)*self.control[ctl.DT];
        newstate[st.Y]=newstate[st.Y]+0.5*(newstate[st.VY]+newvy)*self.control[ctl.DT];
        
        newstate[st.VX]=newvx
        newstate[st.VY]=newvy
        
        #update moon 
        gx=0
        gy=0
        #moon-earth
        gt=self.gravaccel(newstate[st.XM],newstate[st.XE],newstate[st.YM],newstate[st.YE],self.const[cnst.ME]) #earth contrib
        gx=gx+gt[0];
        gy=gy+gt[1]; 
        
        #moon-mars
        gt=self.gravaccel(newstate[st.XM],newstate[st.XMA],newstate[st.YM],newstate[st.YMA],self.const[cnst.MMARS]) #mars contrib
        gx=gx+gt[0];
        gy=gy+gt[1];
        
        #moon-sun
        gt=self.gravaccel(newstate[st.XM],newstate[st.XS],newstate[st.YM],newstate[st.YS],self.const[cnst.MS]) #sun contrib
        gx=gx+gt[0];
        gy=gy+gt[1]; 
        
        #calculate vy
        newvy=newstate[st.VYM]-gy*self.control[ctl.DT];
        newvx=newstate[st.VXM]-gx*self.control[ctl.DT];
          
        #calculate x and y
        newstate[st.XM]=newstate[st.XM]+0.5*(newstate[st.VXM]+newvx)*self.control[ctl.DT];
        newstate[st.YM]=newstate[st.YM]+0.5*(newstate[st.VYM]+newvy)*self.control[ctl.DT]; 
        
        newstate[st.VXM]=newvx
        newstate[st.VYM]=newvy

        #update mars 
        gx=0
        gy=0
        #mars-earth
        gt=self.gravaccel(newstate[st.XMA],newstate[st.XE],newstate[st.YMA],newstate[st.YE],self.const[cnst.ME]) #earth contrib
        gx=gx+gt[0];
        gy=gy+gt[1]; 
                
        #mars-sun
        gt=self.gravaccel(newstate[st.XMA],newstate[st.XS],newstate[st.YMA],newstate[st.YS],self.const[cnst.MS]) #sun contrib
        gx=gx+gt[0];
        gy=gy+gt[1]; 
        
        #calculate vy
        newvy=newstate[st.VYMA]-gy*self.control[ctl.DT];
        newvx=newstate[st.VXMA]-gx*self.control[ctl.DT];
          
        #calculate x and y
        newstate[st.XMA]=newstate[st.XMA]+0.5*(newstate[st.VXMA]+newvx)*self.control[ctl.DT];
        newstate[st.YMA]=newstate[st.YMA]+0.5*(newstate[st.VYMA]+newvy)*self.control[ctl.DT];

        newstate[st.VXMA]=newvx
        newstate[st.VYMA]=newvy         

        #update earth 
        gx=0
        gy=0
        #earth-moon
        gt=self.gravaccel(newstate[st.XE],newstate[st.XM],newstate[st.YE],newstate[st.YM],self.const[cnst.MM]) #earth contrib
        gx=gx+gt[0];
        gy=gy+gt[1]; 
        
        #earth-mars
        gt=self.gravaccel(newstate[st.XE],newstate[st.XMA],newstate[st.YE],newstate[st.YMA],self.const[cnst.MMARS]) #mars contrib
        gx=gx+gt[0];
        gy=gy+gt[1];
        
        #earth-sun
        gt=self.gravaccel(newstate[st.XE],newstate[st.XS],newstate[st.YE],newstate[st.YS],self.const[cnst.MS]) #sun contrib
        gx=gx+gt[0];
        gy=gy+gt[1]; 
        
        #calculate vy
        newvy=newstate[st.VYE]-gy*self.control[ctl.DT];
        newvx=newstate[st.VXE]-gx*self.control[ctl.DT];
          
        #calculate x and y
        newstate[st.XE]=newstate[st.XE]+0.5*(newstate[st.VXE]+newvx)*self.control[ctl.DT];
        newstate[st.YE]=newstate[st.YE]+0.5*(newstate[st.VYE]+newvy)*self.control[ctl.DT]; 
        
        newstate[st.VXE]=newvx
        newstate[st.VYE]=newvy
        
        return newstate
        
    def runmission(self):   #playmarsmission
        print('runmission')
        #cycle through the steps and call update
        for i in range(self.control[ctl.NS]):
            #print(i)
            self.state=self.updatestate()
            self.state[st.T]=self.state[st.T]+self.control[ctl.DT]
        currentstate=self.state
        return currentstate
            
    def dist(self,x1,y1,x2,y2):
        sep=(x1-x2)**2+(y1-y2)**2
        sep=math.sqrt(sep)
        return sep
    
    def gravaccel(self,x,xs,y,ys,ms):
        #Return gravitational acceleration on body at x,y due to body of mass mds
        #located at xs,ys        
        G=6.67e-11; #gravitational constants SI units
        r2=((x-xs)**2+(y-ys)**2)
        r=math.sqrt(r2)
        g=G*ms/r2
        gx=g*(x-xs)/r
        gy=g*(y-ys)/r
        
        gravvec=(gx,gy)
        return gravvec
    
    #def orbitalspeed(self, x1,y1,vx1,vy1,x2,y2,vx2,vy2,mass,const):
    def orbitalspeed(self, x1,y1,vx1,vy1,x2,y2,vx2,vy2,mass):
        #[speed, relspeed, orbspeed] = orbitalspeed(x1,y1,vx1,vy1,x2,y2,vx2,vy2,mass,consts)
        #%% orbitalspeed
        #%   Object 1 is at x1,y1,vx1,vy1
        #%   Object 2 is at x2,y2,vx2,vy2    
        
        relspeed=math.sqrt((vx1-vx2)**2+(vy1-vy2)**2);
        speed=math.sqrt(vx1**2+vx2**2);
        sep=math.sqrt((x1-x2)**2+(y1-y2)**2);

        orbspeed=self.const[ cnst.G]*mass/sep;
        orbspeed=math.sqrt(orbspeed);
        
        #orbitalspeed=(speed,relspeed,orbspeed)
        #return orbitalspeed
        
        return speed,relspeed,orbspeed
        
    
    def orbitalangle(self,x1,y1,vx1,vy1,x2,y2,vx2,vy2):
        #function [angle] = orbitalangle(x1,y1,vx1,vy1,x2,y2,vx2,vy2)
        #%%orbital angle
        #%  for the rocket around a selected body e.g. sun, moon, earth, mars
        #%  compute the orbital angle i.e. the angle between the orbital radius
        #%  vector and the velocity vector
        #%   Object 1 is at x1,y1,vx1,vy1
        #%   Object 2 is at x2,y2,vx2,vy2

        dp=(vx1-vx2)*(x1-x2)+(vy1-vy2)*(y1-y2)
        relspeed=math.sqrt((vx1-vx2)**2+(vy1-vy2)**2)
        sep=math.sqrt((x1-x2)**2+(y1-y2)**2)

        angle=360*math.acos(dp/(relspeed*sep))/(2*math.pi)
        
        return angle
    
    def savemission(self, filename):
        status=0
        fd = open(filename,'w')
        fouts=""
        for mst in st:
            val=self.state[mst]
            fouts=fouts+repr(val)+' '
        for mctl in ctl:
            val=self.control[mctl]
            fouts=fouts+repr(val)+' '
        for rp in mmr.rck:
            val=self.rocket.rockprop[rp]
            fouts=fouts+repr(val)+' '
        for rpay in mmr.payld:
            val=self.rocket.payload[rpay]
            fouts=fouts+repr(val)+' '
        fouts=fouts+'\n'
        print(fouts)
        fd.write(fouts)
        fd.close()        
        return status
        
    def loadmission(self, filename):
        #application which reads columnar data from file
        #using matplotlib,scipy and numpy
        #load data from text file
        ind=0
        status=0
        t1a=np.loadtxt(filename)
        asz=t1a.size
        t1=t1a[0:asz]
        control={}
        state={}
        rockprop={}
        rockpayl={}
        
        for mst in st:
            state[mst]=t1[ind]
            ind=ind+1
        for mctl in ctl:
            control[mctl]=t1[ind]
            ind=ind+1
        for rp in mmr.rck:
            rockprop[rp]=t1[ind]
            #val=self.rocket.rockprop[rp]
            ind=ind+1
        for rpay in mmr.payld:
            rockpayl[rpay]=t1[ind]
            #val=self.rocket.payload[rpay]
            ind=ind+1
        self.control=control
        self.state=state
        self.rocket.payload=rockpayl
        self.rocket.rockprop=rockprop
        self.rocket.updatemass()
        return status
        
        