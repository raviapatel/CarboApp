# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 09:37:39 2021

@author: gf5901
"""

from CarboModel import CarboModel 
import math
    
class Silva(CarboModel):
    """
    
    
    This is the carbonation model according Silva.2014
    k=konst=karbo
    Variables:
       name : str
           Name of the cenario (-)
       C : float
           Clinker content (kg/m³)
       f_c : float
           28-day compressive strenght (MPa)
       phi_clinker : float
           ? (-)
       ExpC : str
           Exposure class (XC1-XC4)
       RH : int
           Relative humidity (%)
       CO2 : float
           CO2 content (%)

    """
    color="pink"
    
    def __init__(self,name:str,C:float,f_c:float,phi_clinker:float,ExpC:str,RH:int,CO2:float)->None:
        """
        

        Parameters
        ----------
        name : str
            Name of the Model
        C : float
            Clinker content (kg/m³)
        f_c : float
            28-day compressive strenght (MPa)
        phi_clinker : float
            ?
        ExpC : str
            Exposure class (XC1-XC4)
        RH : int
            Relative humidity (%)
        CO2 : float
            CO2 content (%)

        Returns
        -------
        None
            Calculates Silva.karbo

        """
        self.name =name
        self.C = C
        self.f_c = f_c
        self.ExpC = ExpC
        self.RH = RH
        self.CO2 = CO2 #*100
        
        if self.RH<= 70 and self.ExpC!='XC2':
            #X value for Exposure class
            if  self.ExpC=='XC1':  X=1
            elif  self.ExpC=='XC3':  X=2
            elif  self.ExpC=='XC4':  X=3
            else:
                print('Error: exposure class')
                return
            
            #CO2 in [%], f_c in [MPa] 
            k_d=0.556*self.CO2-3.602*X-0.148*self.f_c+18.734 #[mm/year]  formel korrigiert!
            Silva.karbo = k_d
            print("Kd: " + str(k_d))
        else:
            C_clinker=self.C*phi_clinker #clinker content in [kg/m^3] with  phi_clinker[-] C in [kg/m³]
            # CO2 in [%], f_c in [MPa]
            k_w=3.355*self.CO2-0.019*C_clinker-0.042*self.f_c+10.83 #[mm/year]    
            Silva.karbo = k_w
            print("Kw: " + str(k_w))

    
    def __repr__(self):
        return("Silva.2014")




