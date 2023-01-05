# -*- coding: utf-8 -*-

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
         name of cenario
     f_c : float
         concrete charasteristic compressive strength [MPa]
     FA_c : float
         fly ash content [weight ratio]
    stress : str
        stress on conponent ['tension', 'pressure']
    location : str
        location of component ['corner', 'other area']
    T : float
        temperature [°C]
    RH : float
         relative humidity around concrete surface [%]
     CO2 : float
         CO2 density around concrete surface [%]
     
     Methods
     -------
         calculates self.karbo [mm/year^0.5]
    
    """
    
    name:str 
    f_c:float 
    FA_c:float 
    stress:str 
    location:str
    T:float 
    RH:float 
    CO2:float 
    
    def __post_init__(self):
        
        self.RH=self.RH/100
        self.k_CO=math.sqrt(self.CO2/0.03)
        self.k_kt=1.2
        
        if self.stress=="Tension":
            self.k_ks=1.1
        else:
            self.k_ks=1.0
            
        if self.location=="Corner":
                self.k_kl=1.4
        else:
                self.k_kl=1.0
                
        self.k_F=1+13.34*(self.FA_c)**(3.3)   #FA is the fly ash content (weight ratio).
                                            #f_c in [MPa]?, CO2 [?]=density around concrete surface
        self.karbo=3*self.k_CO*self.k_kl*self.k_kt*self.k_ks*self.k_F*self.T**(1/4)*self.RH**(1.5)*(1-self.RH)*(58/self.f_c-0.76) #*math.sqrt(365)

       
    def __repr__(self):
        return("CECS220")
