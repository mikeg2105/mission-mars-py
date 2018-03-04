# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 16:14:14 2018

@author: mike
"""

#quick start script to use from python prompt
#to use this 
# 1. start python 
# 2. from prompt 
#        import mmquickstart as mmq
# 3. amm,mm=mmq.mmquickstart()
# 4. amm.startanimation()

# 5. matplotlib widow can be started and stopped and variables reset
#    before restarting animation using the amm.startanimation method

import marsmission as mmc
import animmm as mma        #marstest animation class


def mmquickstart():
    mm=mmc.marsmission()
    print(mm.control[mmc.ctl.DT])
    print(mm.state[mmc.st.VXE])
    print(mm.state[mmc.st.XE])

    amm=mma.animmm(mm)
    mm=amm.getmarsmission()

    print(mm.getallstates())
    
    return amm,mm

#amm.startanimation()
