# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 16:14:14 2018

@author: mike
"""

#simple animation test - this test includes the rocket and rocket update
import marsmission as mmc
import animmm as mma        #marstest animation class
import rocket as mmr




mm=mmc.marsmission()
print(mm.control[mmc.ctl.DT])
print(mm.state[mmc.st.VXE])
print(mm.state[mmc.st.XE])

amm=mma.animmm(mm)
mm=amm.getmarsmission()

rock=mmr.rocket()
mm.setrocket(rock)

print(rock.payload)
print(rock.mass)
print(rock.rockprop)

mm.updaterocket()
print(rock.payload)
print(rock.mass)
#print(mm.getallstates())

#amm.startanimation()
