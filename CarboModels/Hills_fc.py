# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 16:53:02 2021

@author: gf5901
"""

from CarboModels.CarboModel import CarboModel 
import math
    
class Hills_fc(CarboModel):
    """
    This is the carbonation model according 
    k=konst=karbo
    Variables:
        name= Name of cenario
        f_c [MPA]
        C [kg/m^3 or %]
        GGBS [kg/m^3 or %]
        FA [kg/m^3 or %]
        Exposed [bool]
        Sheltered  [bool]
        Indoores [bool]

    """
    color="purple"
    
    def __init__(self, name,  f_c, C, GGBS,FA, Exposed, Sheltered, Indoors):

        self.name =name
    
        I_GGBS=0
        I_PFA=0
        I_cemI=0
        I_Exposed=0
        I_sheltered=0
        I_indoors=0
        
        if GGBS>0 and FA==0:
            I_GGBS=1
        elif FA>0 and GGBS==0:
            I_PFA=1
        elif C>0 and FA==0 and GGBS==0:
            I_cemI=1
        else:
            print('Error concrete mix not defined')
            self.karbo=float('NaN')
            return
            
        if Exposed==True and Sheltered ==False and Indoors==False:
            I_Exposed=1
        elif Sheltered == True and Exposed==False and Indoors==False:
            I_sheltered=1
        elif Indoors==True and Sheltered == False and Exposed==False:
            I_indoors=1
        else:
            print('Error: Exposure conditions not defined')
            self.karbo=float('NaN')
            return
            
        
        lnK=1.066+1.761*I_cemI+2.062*I_GGBS+2.061*I_PFA-0.639*I_Exposed -0.182*I_sheltered-0.648*I_indoors+(0.025-0.053*I_cemI-0.052*I_GGBS-0.05*I_PFA)*f_c
        self.karbo= math.exp(lnK)
        
    def __repr__(self):
        return("Hills.2015 f_c")
    
