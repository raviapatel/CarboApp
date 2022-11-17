# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 13:32:52 2021

@author: gf5901
"""

from CarboModels.CarboModel import *


#to get the infos write "Hills_fc?" in commande line

a=[20,50,100]
t=5

H=Hills_fc("Sample", 30, 320, 0,0, True, False, False)
print("Hills_fc")
H.k()
print(f"The carbonation factor according to Hills_fc is {H.k()}mm/sqrt(year)")
H.x_c(t)
print(f"Carbonation depth x_c according to Hills_fc after {t} years is {H.x_c(t)} mm ")
H.x_cList(a)
print(f"Several carbonation depths according to Hills_fc can be calculated: {a} years -> x_c={H.x_cList(a)}mm \n")

fibG=fibGuiglia(name="Sample", RH=60, ToW=100, p_sr=0.5, t_c=2, f_c=30, C_co2=0.00057 )
print("fibGuiglia")
print(f"The carbonation factor after {t} years according to fibGuiglia is {fibG.k(t)}mm/sqrt(year)")
print(f"Carbonation depth x_c according to fibGuiglia after {t} years is {fibG.x_c(t)} mm")
print(f"Several carbonation depths according to fibGuiglia can be calculated: {a} years -> x_c={fibG.x_cList(a)}mm \n")

