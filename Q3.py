# -*- coding: utf-8 -*-
"""
Created on Mon May 14 19:35:36 2018

@author: mbali
"""

import numpy as np
from matplotlib import pyplot as plt
class advect:
    def __init__(self,npart=300,p=1.0,dy=1.0):
        y=np.zeros(npart)
        y[npart/3:2*npart/3]=1.0;
        self.y=y
        self.p=p
        self.dy=dy
    def get_bc_periodic(self):
        self.y[0]=self.y[-2]
        self.y[-1]=self.y[1]
    def update(self,dt=1.0):
        self.get_bc_periodic()
        delt=self.y[1:]-self.y[0:-1]
        self.y[1:-1]+=self.p*dt/self.dy*delt[1:]

if __name__=='__main__':
    stuff=advect()
    plt.ion()
    plt.plot(stuff.y)
    plt.show()
    for i in range(0,300):
        stuff.update()
        plt.clf()
        plt.plot(stuff.y)
plt.draw()