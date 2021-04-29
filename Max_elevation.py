# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 00:22:31 2021

@author: koshv
"""
## A function to give the maximum elevation of the star from the horizon 
## telescope in southern hemisphere to be given negative latitude

import numpy as np
import matplotlib.pyplot as plt

a1 , b1, c1= input('declination (deg min sec), Star : ').split()
a2 , b2, c2= input('latitude (deg min sec), telescope :').split()

a1 = float(a1)
a2 =float(a2)
b1 = float(b1)
b2 = float(b2)
c1= float(c1)
c2 = float(c2)

if a1<0:
    star= -((-a1)*3600 + b1*60 +c1)
else : 
    star = a1*3600 + b1*60 +c1
    
if a2<0:
    tele = -((-a2)*3600 +b2*60 + c2)
else : 
    tele= a2*3600 + b2*60 + c2
    
x = 90*3600
max_ele = x + star - tele  # Maximum elevation of the star in arcseconds

if divmod(max_ele,3600)[0] < 90 :
    l = divmod(max_ele,3600)
    m = divmod(l[1],60)
else :
    max_ele = 180*3600 - max_ele
    l = divmod(max_ele,3600)
    m = divmod(l[1],60)

print('Max_elevation',l[0],'deg',m[0],'min',m[1],'sec')

