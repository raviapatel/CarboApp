# -*- coding: utf-8 -*-

from dataclasses import dataclass
from CarboModels.CarboModel import CarboModel 
    
@dataclass
class Ekolu(CarboModel):
    """
    This is the carbonation model according to Ekolu.2018
        
    attributes
    ----------
    name : str
        name of cenario
    f_c : float 
        28-day compressive strenght or long-term (field) strenght [MPa]
    RH : float 
        relative humidity [%]
    CO2 : float
        CO2 concentration [%]
    cem : str
        Cement type ['CEM I', 'CEM II/A', 'CEM II/B', 'CEM IV/A', 'CEM III/A', 'CEM IV/B'] 
    ExCo : str
        exposure conditions ['Exposed', 'Sheltered']
    
    Methods
    -------
        calculates self.karbo [mm/year^0.5]     
        
    """
    color="orange"
    
    name:str 
    f_c:float 
    RH:float 
    CO2:float 
    Cem:str
    ExCo:str 
    t:float

    
    def __post_init__(self):          # change for cement type
        self.karbo=0
        #Formula (9)
        if  self.ExCo == "Sheltered from Rain":
            self.e_s = 1
        elif self.ExCo == "Exposed to Rain" or self.ExCo == "Outdoor":
            self.e_s = self.f_c**(-0.2)
        else:
            self.karbo="NaN"
            return
        
        #Table (13)
        if self.Cem=="CEM I" or self.Cem=="CEM II/A":
            self.g=-1.5
        elif self.Cem=="CEM II/B" or self.Cem =="CEM IV/A":
            self.g=-1.4
        elif self.Cem=="CEM III/A" or self.Cem=="CEM IV/B":
            self.g=-1.4
        else:
            self.karbo="NaN"
            return
            
        #Formula (8)
        if 50<= self.RH <=80:
            self.e_h=16*((self.RH-35)/100)*(1-self.RH/100)**(1.5)    #for 50<=RH<=80
        else:
            self.karbo="NaN"
            return
        
        #Table (10)
        if self.CO2 <=0.02: #[%]
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
        else:
            self.karbo="NaN"
            return
            
        #Formula (10)
        if 20 < self.f_c <60:                #[MPa]
            self.e_co=alpha*self.f_c**r
        elif self.f_c >= 60:
            self.e_co=1
        else:
            self.e_co=1
            self.karbo="NaN"
            return
        t = self.t
        if t < 6:                             #[years] 
            a=0.35
            b= 0.6-(t**(0.5)/50)
        else:
            a=0.15*t
            b=0.5-(t**(0.5)/50)
          
        F_ct=t/(a+b*t) *self.f_c   
        cem=1000

        self.karbo = self.e_h*self.e_s*self.e_co*cem*(F_ct)**self.g 
     
    
    def __repr__(self):
        return("Ekolu.2018 f_c,28")