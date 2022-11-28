# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 09:37:39 2021

@author: gf5901
"""
from dataclasses import dataclass
from CarboModels.CarboModel import CarboModel 

@dataclass
class Silva(CarboModel):
    
    """
    
    attributes
    ----------
    name : str
        Name of the Model
    C : float
        Clinker content (kg/m³)
    f_c : float
        28-day compressive strenght (MPa)
    ExpC : str
        Exposure class (XC1-XC4)
    RH : float
        Relative humidity (%)
    CO2 : float
        CO2 content (%)
    
    Methods
    -------
        Calculates self.karbo (mm/year^0.5)
    
    """
    
    name:str
    C:float
    f_c:float
    ExpC:str
    RH:float
    CO2:float
    
    def __post_init__(self):
        
        if self.RH<= 70 and self.ExpC!='XC2':
            #X value for Exposure class
            if  self.ExpC=='XC1':  X=1
            elif  self.ExpC=='XC3':  X=2
            elif  self.ExpC=='XC4':  X=3
            else:
                print('Error: exposure class')
                return
            
            #CO2 in [%], f_c in [MPa] 
            k_d=0.556*self.CO2-3.602*X-0.148*self.f_c+18.734 #[mm/year]
            self.karbo = k_d
            print("Kd: " + str(k_d))
        else:
            # CO2 in [%], f_c in [MPa]
            k_w=3.355*self.CO2-0.019*self.C-0.042*self.f_c+10.83 #[mm/year]    
            self.karbo = k_w
            print("Kw: " + str(k_w))

    def __repr__(self):
        return("Silva.2014")




