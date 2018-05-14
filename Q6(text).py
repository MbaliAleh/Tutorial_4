# -*- coding: utf-8 -*-
"""
Created on Mon May 14 19:32:38 2018

@author: mbali
"""

#The factor of 2 comes from the fact that we are calculating the derivative
#from the left to right.Since each point is dx
#away from the center point, the total distance between the left and
#right neighbours is 2dx, so when calculating the numerical derivative,
#we shold multiply by a factor of half(1/2*dx) not dx.