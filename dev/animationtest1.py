# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 16:14:14 2018

@author: mike
"""
import marsmission as mmc
import animmm as mma        #marstest animation class


mm=mmc.marsmission()
amm=mma.animmm(mm)
#mm=amm.getmarsmission()

print(mm.getallstates())

amm.startanimation()
