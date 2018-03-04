# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 16:14:14 2018

@author: mike
"""

#simple animation test
import marsmission as mmc
import animmm as mma        #marstest animation class


mm=mmc.marsmission()
print(mm.control[mmc.ctl.DT])
print(mm.state[mmc.st.VXE])
print(mm.state[mmc.st.XE])

amm=mma.animmm(mm)
mm=amm.getmarsmission()

print(mm.getallstates())

#amm.startanimation()
