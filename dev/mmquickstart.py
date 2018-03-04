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
# 3. amm,mm,mr=mmq.mmquickstart()
# 4. amm.startanimation()
#5. import marsmission as mmc

# 6. matplotlib widow can be started and stopped and variables reset
#    before restarting animation using the amm.startanimation method

import marsmission as mmc
import animmm as mma        #marstest animation class
import rocket as mmr

def mmquickstart():
    mm=mmc.marsmission()
    mr=mmr.rocket()

    mm.control[mmc.ctl.DT]=100
    print(mm.control[mmc.ctl.DT])
    print(mm.state[mmc.st.VXE])
    print(mm.state[mmc.st.XE])

    amm=mma.animmm(mm)
    mm=amm.getmarsmission()
    mm.rocket=mr
    
    print(mr.payload)
    
    print(mm.getallstates())
    

    
    
    return amm,mm,mr

#amm.startanimation()
