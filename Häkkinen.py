# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 13:52:09 2021

@author: gf5901
"""

from CarboModels.CarboModel import CarboModel 
import math
    
class Häkkinen(CarboModel):
    """
    This is the carbonation model according Häkkinen.1993 in DuraCrete.1998
    k=konst=karbo
    Variables:
        name= Name of cenario
        Exposed (bool)
        Sheltered (bool)
        C (kg/m³) 
        FA (kg/m³) 
        SF (kg/m³) 
        GGBS (kg/m³) 
        f_c (MPa)
    """
    
    def __init__(self, name, Exposed, Sheltered, C, FA, SF, GGBS, f_c):
        self.name =name
        #self.Exposed=Exposed
        #self.Sheltered=Sheltered
        #self.C=C 
        #self.FA=FA
        #self.SF=SF
        #self.GGBS=GGBS
        self.f_c=f_c
        
        if Exposed == True and Sheltered==False :  #Tab A2 in DuraCRete.1998
            self.c_env=1
        elif Exposed == False and Sheltered==True:
            self.c_env=1
        else:
            print('Error: exposure')
            return
        
        if C>0 and  FA==0 and SF==0 and GGBS==0:   #Tab A2 in DuraCRete.1998
            self.a=1800
            self.b=-1.7
        elif C>0 and FA>0 and SF==0 and GGBS==0:
            print('recommended value FA=28%, here:', FA/(C+FA+SF+GGBS)*100)
            self.a=360
            self.b=-1.2
        elif C>0 and FA==0 and SF>0 and GGBS==0:
            print('recommended value SF=9%, here:', SF/(C+FA+SF+GGBS)*100)
            self.a=400
            self.b=-1.2
        elif C>0 and FA==0 and SF==0 and GGBS>0:
            print('recommended value GGBS=70%, here:', GGBS/(C+FA+SF+GGBS)*100)
            self.a=360
            self.b=-1.2
        else :
            print('Error: mixture')
            self.karbo=float('NaN')
            return
        
        self.karbo=self.c_env*1*self.a*self.f_c**self.b
    

    def __repr__(self):
        return("Häkkinen.1993")



    

    