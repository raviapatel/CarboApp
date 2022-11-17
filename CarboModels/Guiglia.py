# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 09:24:06 2021

@author: gf5901
"""
from dataclasses import dataclass 
from CarboModels.CarboModel import CarboModel 
import math
  
@dataclass  
class Guiglia(CarboModel):
    
    """
    
    attributes
    ----------
    name : str
        Name of the Model
    f_c : float
        28-day compressive strenght (MPa)
    RH : int
        Relative humidity (%)
    building : str
        Tunnel or other buildings
        
    Methods
    -------
        Calculates self.karbo (mm/year^0.5)
        
    """
    
    name:str 
    f_c:float 
    RH:float 
    building:str 
    
    def __post_init__(self):
        
        k_e= ((1-(self.RH/100)**5)/(1-0.65**5))**2.5
        
        #f_c (MPa), t in [years]
        if self.building=="Tunnel":
            self.karbo= 206*math.sqrt(k_e*self.f_c**(-2.1))
        else:
            self.karbo= 163*math.sqrt(k_e*self.f_c**(-2.1))
        
    def __repr__(self):
        return("Guiglia.2013")
