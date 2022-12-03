# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 08:27:48 2021

@author: gf5901
"""

from dataclasses import dataclass
from CarboModels.CarboModel import CarboModel 
    
@dataclass
class Ekolu(CarboModel): #Model of Eklou.2018
    """
    This is the carbonation model according Ekolu.2018
    k(t)
    Variables:
        name= Name of cenario
        f_c (MPa) >20Mpa
        RH(%)
        CO2(-)
        FA_c, (-)
        GGBS_c (-)
        Sheltered (bool)
        Exposed (bool)
        
    attributes
    ----------
    name : str
        Name of the model
    f_c : float 
        28-day compressive strenght (MPa)
    RH : float 
        Relative humidity (%)
    CO2 : float
        CO2 concentration (%)
    FA_c : float
        Fly ash content (-) 
    GGBS_c : float 
        Blast furnace slag content (-) 
    ExCo : str
        Exposure conditions ('Exposed', 'Sheltered')
    
    Methods
    -------
        Calculates self.karbo (mm/year^0.5)     
        
    """
    color="orange"
    
    name:str 
    f_c:float 
    RH:float 
    CO2:float 
    FA_c:float 
    GGBS_c:float 
    ExCo:str 

    
    def __post_init__(self):          # change for cement type
    
        #Formula (9)
        if  self.ExCo == "Sheltered":
            self.e_s = 1
        else:
            self.e_s = self.f_c**(-0.2)
        
        #Table (13)
        if self.FA_c + self.GGBS_c <=0.2:
            self.g=-1.5
        elif self.FA_c<=0.3:
            print("FA_c is ", self.FA_c, 'reccomened is 0.3')
            self.g=-1.4
        elif self.GGBS_c<=0.5:
            print("GGBS_c is ", self.GGBS_c, 'reccomened is 0.5')
            self.g=-1.4
        else:
            print('SCM not fitted')
            return
            
        #Formula (8)
        self.e_h=16*((self.RH-35)/100)*(1-self.RH/100)**(1.5)    #for 50<=RH<=80

        
        #Table (10)
        if self.CO2 <=0.02: #ppm
            alpha= 1.4
            r=-1/4
        elif self.CO2 <= 0.03:
            alpha= 1
            r=0
        elif self.CO2 <= 0.05:
            alpha= 2.5
            r=-1/4
        elif self.CO2 <= 0.1:
            alpha= 4.5
            r=-2/5
        elif self.CO2 <= 0.2:
            alpha= 14
            r=-2/3
            
        #Formula (10)
        if 20 < self.f_c <60:                              #[MPa]
            self.e_co=alpha*self.f_c**r
        elif self.f_c >= 60:
            self.e_co=1
        else:
            print("Error f_c")
            self.e_co=float('NaN')
            return None

    def __repr__(self):
        return("Ekolu.2018 f_c,28")
    
    def k(self,t):
        
        #with f_c,28 strenght
        if t < 6:                                      #[years] 
            a=0.35
            b= 0.6-(t**(0.5)/50)
        else:
            a=0.15*t
            b=0.5-(t**(0.5)/50)
            
        F_ct=t/(a+b*t) *self.f_c   
        cem=1000
        
        self.karbo = self.e_h*self.e_s*self.e_co*cem*(F_ct)**self.g 
        return self.karbo
    
    