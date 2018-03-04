# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 16:57:01 2018

@author: mike
"""

#https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot
#animation class for mars mission
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import marsmission as mmc

pause = False


class animmm(object):   
    
        def __init__(self):
            self.mm=mmc.marsmission()
            
        #initialise with a world provided   
        def __init__(self,mm):
            self.mm=mm

        def animater(self, i):
            global satsr
            newstate=self.mm.updatestate()
            self.mm.updaterocket()
            self.mm.state[mmc.st.T]=self.mm.state[mmc.st.T]+self.mm.control[mmc.ctl.DT]
            self.mm.state=newstate
            
            #print(self.mm.state[mmc.st.XE],'  ',self.mm.state[mmc.st.YE],'\n')
            self.xr= self.mm.state[mmc.st.X] 
            self.yr= self.mm.state[mmc.st.Y] 
            satsr=self.satsr
            self.matr.set_data(self.xr, self.yr)
            #self.matr
            return self.matr,
    
        def animate(self, i):                        
            global sats
            self.sats = set([(self.mm.state[mmc.st.XE], self.mm.state[mmc.st.YE]), (self.mm.state[mmc.st.XM], self.mm.state[mmc.st.YM]),  (self.mm.state[mmc.st.XMA], self.mm.state[mmc.st.YMA])])

            sats=self.sats
            self.x, self.y = zip(*self.sats)
            #self.x[0]=self.mm.state[mmc.st.XE]
            #self.y[0]=self.mm.state[mmc.st.YE]
            #self.x[1]=self.mm.state[mmc.st.XM]
            #self.y[1]=self.mm.state[mmc.st.YM]
            #self.x[2]=self.mm.state[mmc.st.XMA]
            #self.y[2]=self.mm.state[mmc.st.YMA]
            self.mat.set_data(self.x, self.y)
            #self.mat
            return self.mat,
        
        
        def getmarsmission(self):
            return self.mm
        
 #       def init(self):
 #           #self.line.set_ydata(np.ma.array(self.x, mask=True))
 #           
 #           self.earthp.set_xdata(self.mm.state[mmc.st.XE])                
 #           self.earthp.set_ydata(self.mm.state[mmc.st.YE])
 #           self.moonp.set_xdata(self.mm.state[mmc.st.XM])                
 #           self.moonp.set_ydata(self.mm.state[mmc.st.YM])
 #           self.rockp.set_xdata(self.mm.state[mmc.st.X])                
 #           self.rockp.set_ydata(self.mm.state[mmc.st.Y])
 #           return self.points,
   
        def onClick(self, event):
            global pause
            pause ^= True
     
        def startanimation(self):
            print("hi there, everyone!")

            self.sats = set([(self.mm.state[mmc.st.XE], self.mm.state[mmc.st.YE]), (self.mm.state[mmc.st.XM], self.mm.state[mmc.st.YM]),  (self.mm.state[mmc.st.XMA], self.mm.state[mmc.st.YMA])])
            self.satsr = set([(self.mm.state[mmc.st.X], self.mm.state[mmc.st.Y])])

            self.fig, self.ax = plt.subplots()

            self.x, self.y = zip(*self.sats)
            self.xr, self.yr = zip(*self.satsr)
            print(self.x[0])
            print(self.y[0])
            #self.mat, = self.ax.plot(self.x[0], self.y[0], 'bo',self.x[1], self.y[1], 'go',self.x[2], self.y[2], 'ro',self.x[3], self.y[3], 'yo')
            #self.mat, =self.ax.plot(self.x[0],self.y[0],'bo')
            #self.mat, =self.ax.plot(self.x[1],self.y[1],'ro')
            #self.mat, =self.ax.plot(self.x[2],self.y[2],'ro')
            
            self.mat, =self.ax.plot(self.x,self.y,'ro')
            
            
            self.matr, =self.ax.plot(self.x[0],self.y[0],'go')
            
            self.ax.plot(self.mm.state[mmc.st.XS], self.mm.state[mmc.st.YS],'yo')
            
            self.ax.axis([-4e11,4e11,-3e11,5e11])
            self.fig.canvas.mpl_connect('button_press_event', self.onClick) 
            self.ani = animation.FuncAnimation(self.fig, self.animate, interval=50)
            self.anir = animation.FuncAnimation(self.fig, self.animater, interval=50)
            plt.show()


            
            
            
            
            
            