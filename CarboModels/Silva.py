# -*- coding: utf-8 -*-

from dataclasses import dataclass
from CarboModels.CarboModel import CarboModel 

@dataclass
class Silva(CarboModel):
    
    """
    This is the carbonation model according to Silva.2014
    
    attributes
    ----------
    name : str
        name of cenario
    C : float
        clinker content [kg/m³]
    f_c : float
        28-day compressive strenght [MPa]
    ExpC : str
        exposure class [XC1-XC4]
    RH : float
        relative humidity [%]
    CO2 : float
        CO2 content [%]
    
    Methods
    -------
        calculates self.karbo [mm/year^0.5]
    
    """
    
    name:str
    C:float
    f_c:float
    ExpC:str
    RH:float
    CO2:float
    
    def __post_init__(self):
        
        if self.RH<= 70 and self.ExpC!="XC2":
            #X value for Exposure class
            if  self.ExpC=="XC1":  X=1
            elif  self.ExpC=="XC3":  X=2
            elif  self.ExpC=="XC4":  X=3

            
            #CO2 in [%], f_c in [MPa] 
            k_d=0.556*self.CO2-3.602*X-0.148*self.f_c+18.734 #[mm/year^0,5]
            self.karbo = k_d
        elif self.RH>70 or self.ExpC=="XC2":
            # CO2 in [%], C in [kg/m³] f_c in [MPa]
            k_w=3.355*self.CO2-0.019*self.C-0.042*self.f_c+10.83 #[mm/year^0,5]    
            self.karbo = k_w
        else:
            self.karbo="NaN"
            return

    def __repr__(self):
        return("Silva.2014")




