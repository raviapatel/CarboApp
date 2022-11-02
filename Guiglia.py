# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 09:24:06 2021

@author: gf5901
"""

from CarboModels.CarboModel import CarboModel 
import math
    
class Guiglia(CarboModel):
    """
    This is the carbonation model according Guiglia.2013¶
    k=konst=karbo
    Variables:
        name= Name of cenario
        f_c(MPa) 28Days
        RH(%) 
        Tunnel (bool)
    """
    
    def __init__(self, name, f_c, RH, Tunnel):
        self.name =name
        self.f_c =f_c
        self.RH =RH
        self.Tunnel =Tunnel
        
        k_e= ((1-(RH/100)**5)/(1-0.65**5))**2.5
        
        #f_c (MPa), t in [years]
        if Tunnel==True:
            self.karbo= 206*math.sqrt(k_e*f_c**(-2.1))
        else:
            self.karbo= 163*math.sqrt(k_e*f_c**(-2.1))
        
    def __repr__(self):
        return("Guiglia.2013")

        

new =Guiglia("beispeil", 20, 60, True)
print(new.x_c(2))
print(new.x_cList([0,1,2,60])  )
