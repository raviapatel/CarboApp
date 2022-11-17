# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 16:41:26 2021

@author: gf5901
"""

from CarboModels.CarboModel import CarboModel 
import math
    
class Hills_time(CarboModel):
    """
    This is the carbonation model according Hills.2015 (time-depending model)
    k(t)
    Variables:
        name= Name of cenario
        C,GGBS,FA (kg/m³ or %)
        Exposed, Sheltered, Indoors, ExpData (bool), ExpData =concrete made in Lab?

    """
    color="brown"
    
    def __init__(self, name, C,GGBS,FA, Exposed, Sheltered, Indoors, ExpData):
        self.name =name
        
        self.I_GGBS=0
        self.I_PFA=0
        self.I_cemI=0
        self.I_Exposed=0
        self.I_sheltered=0
        self.I_indoors=0
        self.I_exp=0
        
        if GGBS>0 and FA==0:
            self.I_GGBS=1
        elif FA>0 and GGBS==0:
            self.I_PFA=1
        elif C>0 and FA==0 and GGBS==0:
            self.I_cemI=1
        else:
            print('Error concrete mix not defined')
            return
            
        if Exposed==True and Sheltered ==False and Indoors==False:
            self.I_Exposed=1
        elif Sheltered == True and Exposed==False and Indoors==False:
            self.I_sheltered=1
        elif Indoors==True and Sheltered == False and Exposed==False:
            self.I_indoors=1
        else:
            print('Error: Exposure conditions not defined')
            self.I_Exposed=float('NaN')
            return
            
        if ExpData == True:
            self.I_exp=1

        
    def __repr__(self):
        return("Hills.2015 time")
    
    def k(self,t):  #t in [year]
        lnK= 0.567-0.167*self.I_cemI+0.101*self.I_GGBS+0.129*self.I_PFA+0.249*self.I_Exposed + 0.818*self.I_sheltered+0.433*self.I_indoors+(0.037-0.088*self.I_exp)*t+(-0.00046+0.0013*self.I_exp)*t**2
        #K in [mm/year^0.5])
        return math.exp(lnK)
    
    def x_c(self, t):
        """
        calculates one Carbonation depth for given time t 
        k(t)
        Parameters
        ----------
        t(years): TYPE
            Time

        Returns
        -------
        x_c(mm) : TYPE
            cabonation depth
        """
        
        x_c = self.k(t) * t**0.5
        return x_c
    
    def x_cList(self, t):
        """
        calculates Carbonation depth for time serie 
        k(t)
        Parameters
        ----------
        t(years): List
            Time

        Returns
        -------
        x_c(mm) : List with x.xx 
            cabonation depth
        """
        x_c =[]
        for i in t:
            x_c.append(round(self.k(i)* i**0.5, 2))
        return x_c
    
 