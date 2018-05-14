# -*- coding: utf-8 -*-
"""
Created on Mon May 14 19:29:36 2018

@author: mbali
"""

#Problem 5(text)

#The code only perfom periodic and smooth boundary conditions.
#Nowhere else in the code does it check that the boundary conditions
#are set to one of these two values, so it is possible that
#one could set the boundary conditions to be an invalid type.  So,
#the boudary condition loops over legal boundary conditions; when it
#finds one, it fills in the boundary conditions and returns.  The code
#will only get to the assert statement if an unrecognized class of
#boundary conditions is specified.  Without some sort of error message,
#the code would continue to run, but with the boundary condition
#routine doing nothing, which would likely produce incorrect results
#without any warning.  

