
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
    MR=8

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
    
    

def initmarsmission():
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
#const.mr=1.0; %mass of rocket
    const={}
    const[ cnst.G]=6.67e-11
    const[cnst.re]=6.3781e6 
    const[cnst.de]=2*6.3781e6
    #5.97237e24, 7.342e22,1.99e30,6.42e23,381.5e6,1.0)
	
	
	
    
    
#%%state vars

#state.time=0; %time hours
#state.xe=0; %x position of earth
#state.ye=0; %y position of earth
#state.vxe=30000;% x-speed of the earth
#state.vye=0;%y-speed of the earth
#state.xm=381.5e6; %xpos moon
#state.ym=0; %ypos moon
#state.vxm=+state.vxe; %moon speed in orbit x-direction
#state.vym=state.vye+1023.1;
#state.vxs=0.0;
#state.vys=0.0;
#state.xs=0; %x position of sun
#state.ys=149.6e9; %y position of sun    
    
#state.xma=0; %xpos mars
#state.yma=225e9+state.ys; %ypos mars (note added sun distance on)
#state.vxma=-24130;
#state.vyma=0;
    
#%initial conds for rocket
#state.u=9000; %initial speed%metres per second;
#state.y=const.re+50000;
#state.x=0;
#%convert theta to radians
#state.theta=0;
#state.theta=state.theta*2*pi/360;
#state.vx=state.u*cos(state.theta);
#state.vy=state.u*sin(state.theta);   
    
    
    
    
    state=(1.0, 2.0)
 


#control vars
#control.nsteps=500000;
#control.dt=1; %time step
#control.theta=0;
#control.box=800e6; %include moon
#control.saveinterval=control.nsteps;
#control.fx=0; %fx and fy force on rocket (thrust from motors)
#control.fy=0;
   

    
    
    
    control= (1.0, 2.0)

    marsmission = (state, control,const)

    return marsmission	