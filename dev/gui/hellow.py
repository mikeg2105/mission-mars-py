# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 03:46:15 2018

@author: mike
"""

import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

pause = False

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        
        self.bpause = tk.Button(self)
        self.bpause["text"] = "pause\n(click me)"
        self.bpause["command"] = self.pause_now
        self.bpause.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def animate(self, i):
        if not pause:
            self.line.set_ydata(np.sin(self.x + i/10.0))  # update the data
        return self.line,

    def onClick(self, event):
        global pause
        pause ^= True  
        
    def pause_now(self):      
        print('pause')

    def say_hi(self):
        print("hi there, everyone!")
        
        self.fig, self.ax = plt.subplots()

        self.x = np.arange(0, 2*np.pi, 0.01)
        self.line, = self.ax.plot(self.x, np.sin(self.x))
        self.fig.canvas.mpl_connect('button_press_event', self.onClick)        
        
        self.ani = animation.FuncAnimation(self.fig, self.animate, np.arange(1, 20), init_func=self.init,
                              interval=25, blit=True)
        plt.show()
        

        
        # Init only required for blitting to give a clean slate.
    def init(self):
        self.line.set_ydata(np.ma.array(self.x, mask=True))
        return self.line,
        
  


root = tk.Tk()
app = Application(master=root)
app.mainloop()