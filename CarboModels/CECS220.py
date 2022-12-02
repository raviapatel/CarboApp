# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 09:05:37 2021

@author: gf5901
"""
from dataclasses import dataclass
from CarboModels.CarboModel import CarboModel 
import math
    
@dataclass
class CECS220(CarboModel):
    """
    This is the carbonation model according to CECS220.2007 from paper Sun.2020
     
     attributes
     ----------
     name : str
         Name of the Model
     f_c : float
         28-day compressive strenght (MPa)
     FA : float
         Fly ash content, weight ratio (-)
    stress : str
        Stress on conponent ('tension', 'pressure')
    location : str
        Location of component ('corner', 'other area')
    T : float
        Temperature (°C)
    RH : float
         Relative humidity around concrete surface (%)
     CO2 : float
         CO2 content around concrete surface (%)
     
     Methods
     -------
         Calculates self.karbo (mm/year^0.5)
    
    """
    
    name:str 
    f_c:float 
    FA:float 
    stress:str 
    location:str
    T:float 
    RH:float 
    CO2:float 
    
    def __post_init__(self):
        
        self.RH=self.RH/100
        self.k_CO=math.sqrt(self.CO2/0.03)
        self.k_kt=1.2
        
        if self.stress=="stress":
            self.k_ks=1.1
        else:
            self.k_ks=1.0
            
        if self.location=="corner":
                self.k_kl=1.4
        else:
                self.k_kl=1.0
                
        self.k_F=1+13.34*(self.FA)**(3.3)   #FA is the fly ash content (weight ratio).
                                            #f_c in [MPa]?, CO2 [?]=density around concrete surface
        self.karbo=3*self.k_CO*self.k_kl*self.k_kt*self.k_ks*self.k_F*self.T**(1/4)*self.RH**(1.5)*(1-self.RH)*(58/self.f_c-0.76) #*math.sqrt(365)

       
    def __repr__(self):
        return("CECS220")
