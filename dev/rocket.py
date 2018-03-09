#Define a class for a rocket
#Determine what payload is carried  so that deliveries can be made to remote system

from enum import Enum



#enumeration for rocket cargo types
#note to be consistent with blocks and 
#structural units on minecraft

#e.g. see for block ids http://minecraft-ids.grahamedgecombe.com/
class payld(Enum):
    OXY=0
    H2O=1    
    FOOD=2
    PLNT=3
    HAB=4
    FUEL=5
    CREW=6
    ROV=7  #MARS ROVER
    EXTRAS=8
    
#enumeration for rocket properties   
class rck(Enum):
    NE=0  #number of engines
    EP=1  #engine power  


def setrocket(numeng, engpower):
    rockprop={}
    rockprop[rck.NE]=numeng #e.g. 4
    rockprop[rck.EP]=engpower  #e.g.500
    #rockprop[rck.MF]=engpower*numeng
    
    return rockprop

class rocket(object):
    rockprop=setrocket(12,250000)
    payload={}
    mass=1
    
    def __init__(self, payload):
        self.payload = payload
        tmass=updatemass(payload)
        setmass(tmass)
        
    def __init__(self):
        payload = {}
        payload[payld.OXY]=100
        payload[payld.H2O]=100
        payload[payld.FOOD]=100
        payload[payld.PLNT]=50
        payload[payld.HAB]=2
        payload[payld.FUEL]=100000
        payload[payld.CREW]=3
        payload[payld.ROV]=1
        payload[payld.EXTRAS]=50
        
        self.payload=payload
        tmass=self.updatemass()
        self.setmass(tmass)
               
    def updatemass(self):
        tmass=0
        tmass=tmass+(self.payload[payld.OXY])
        tmass=tmass+5*(self.payload[payld.H2O])   
        tmass=tmass+3*(self.payload[payld.FOOD])
        tmass=tmass+4*(self.payload[payld.PLNT])
        tmass=tmass+3*(self.payload[payld.HAB])   
        tmass=tmass+8*(self.payload[payld.FUEL])
        tmass=tmass+0.5*(self.payload[payld.CREW])   
        tmass=tmass+6*(self.payload[payld.ROV])
        tmass=tmass+3*(self.payload[payld.ROV])
        self.mass=tmass
        return tmass
    
    def setmass(self,tmass):
        self.mass=tmass
        
    def setfuel(self):
        #compute remaining fuel depends on force power etc
        tmass=self.updatemass()
        self.setmass(tmass)
        
    def seth2o(self,dt):
        #update water after time dt  depends on number of passengers
        tmass=self.updatemass()
        self.setmass(tmass)        
        
        
    def seto2(self,dt):
        #update oxygen after time dt  depends on number of passengers
        tmass=self.updatemass()
        self.setmass(tmass)
        
    def setfood(self,dt):
        #update oxygen after time dt depends on number of passengers
        tmass=self.updatemass()
        self.setmass(tmass)
        
    def setpayloadobj(self,payloadobj,val):
        #update oxygen after time dt depends on number of passengers
        #for example payloadobj could be payld.OXY
        self.payload[payloadobj]=val
        tmass=self.updatemass()
        self.setmass(tmass)
     
        
    
    
    
    