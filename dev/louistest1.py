# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 16:14:14 2018

@author: mike
"""
import marsmission as mmc
import animmm as mma        #marstest animation class
import rocket as mmr

mm=mmc.marsmission()
amm=mma.animmm(mm)
#mm=amm.getmarsmission()

#print(mm.getallstates())

#print(mm.control)

mm.state[mmc.ctl.DT]=2000

mm.control[mmc.ctl.FX]=-.001
mm.control[mmc.ctl.FY]=-.001

rock=mmr.rocket()

mm.rocket=rock
print(rock)
    
print(rock.payload)
print(rock.mass)
print(rock.rockprop)

mm.updaterocket()
print(rock.payload)
#print(rock.mass)



#amm.startanimation()
