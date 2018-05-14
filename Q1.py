# -*- coding: utf-8 -*-
"""
Created on Mon May 14 17:56:25 2018

@author: mbali
"""


from __future__ import division, print_function
import numpy

n= 101
xfin= 2*numpy.pi
dx= xfin/(n-1)
k= numpy.arange(n)
y= numpy.sinc(dx*k)
fy= numpy.fft.fft(y)
wps= numpy.linspace(0,2*numpy.pi,n+1)[:-1]
basis= 1.0/n*numpy.exp(1.0j * wps * k[:,numpy.newaxis])
recon_y= numpy.dot(basis,fy)
yerr= numpy.max(numpy.abs(y-recon_y))

print('yerr:',yerr)

lin_fy= numpy.linalg.solve(basis,y)
fyerr= numpy.max(numpy.abs(fy-lin_fy))

print('fyerr',fyerr)