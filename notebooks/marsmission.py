from enum import Enum

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

    
    def __init__(self, control, state):
        self.control = control
        self.state = state    
    
    def __init__(self):        
        control={}
        control[ctl.DT]=1
        control[ctl.NS]=10 
        control[ctl.SINT]=100000
        control[ctl.FX]=0 #FX FY forces in x and Y direction
        control[ctl.FY]=0
        control[ctl.MR]=1  #mass of rocket        
        
        state={}
        state[st.T]=0
        state[st.XE]=0
        state[st.YE]=0
        state[st.VXE]=30000
        
        self.control = control
        self.state = state
        
    def updatestate(self):
        #print('hello')
        self.state[st.XE]=self.state[st.XE]+10
        print(self.state[st.XE])
        #print('goodbye')
        
    def runmission(self):   #playmarsmission
        print('runmission')
        #cycle through the steps and call update
        for i in range(self.control[ctl.NS]):
            print(i)
            self.updatestate()
            
    def dist(x1,y1,x2,y2):
        sep=(x1-x2)^2+(y1-y2)^2
        sep=sqrt(sep)
        return sep
    
    def gravaccel(x,xs,y,ys,ms):
        
        gx=1
        gy=1
        
        gravvec=(gx,gy)
        return gravvec
    
    def orbitalspeed(x1,y1,vx1,vy1,x2,y2,vx2,vy2,mass,consts):
        #[speed, relspeed, orbspeed] = orbitalspeed(x1,y1,vx1,vy1,x2,y2,vx2,vy2,mass,consts)
        #%% orbitalspeed
        #%   Object 1 is at x1,y1,vx1,vy1
        #%   Object 2 is at x2,y2,vx2,vy2
    
        speed=1
        relspeed=1
        orbspeed=1
        
        orbitalspeed=(speed,relspeed,orbspeed)
        return orbitalspeed