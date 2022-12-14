# -*- coding: utf-8 -*-

from dataclasses import dataclass
from CarboModels.CarboModel import CarboModel 
import math
    
@dataclass
class Yang(CarboModel):
    """
    
    This is the carbonation model according to Yang.2014
        
    attributes
    ----------
    name : str
        name of cenario
    C : float
        cement content [kg/m³]
    S : float
        sand content [kg/m³]
    G : float
        gravel content [kg/m³]
    FA : float
        fly ash content [kg/m³]
    GGBS : float
        ground granulated blast furnace slag content [kg/m³]
    SF : float
        silica fume content [kg/m³]
    wb : float
        water / binder ratio [-]
    RH : float
         relative humidity around concrete surface [%] 
    CO2 : float
        peripheral concentration by weight of CO2 [%]
    ExCo : str
        exposure condition of component
    Finishing : str
         finishing material of component
    
    Methods
    -------
        Calculates self.karbo [mm/year^0.5]    
   
    """
    
    name:str 
    t:float
    C:float 
    S:float 
    G:float 
    FA:float 
    GGBS:float 
    SF:float 
    wb:float 
    RH:float 
    CO2:float 
    ExCo:str
    Finishing:str
    
    def __post_init__(self):
       
        self.CO2=0.0409*self.CO2*10000*44.01/1000000000  # [g/cm^3] = 0.0409*CO2[%]*10000*44.01*1000000000
        
        if self.ExCo=="Outdoor" or self.ExCo=="Sheltered from Rain" or self.ExCo=="Exposed to Rain":
            if self.Finishing=="Nothing":
                b_f = 1.0
            elif self.Finishing=="Plaster":
                b_f = 0.79
            elif self.Finishing=="Mortar + Plaster":
                b_f = 0.41
            elif self.Finishing=="Mortar":
                b_f = 0.29
            elif self.Finishing=="Mortar + Paint":
                b_f = 0.15
            elif self.Finishing=="Tile":
                b_f = 0.21
            elif self.Finishing=="Paint":
                b_f = 0.57
            else:
                self.karbo="NaN"
                return
            
        elif self.ExCo=="Indoor":
            if self.Finishing =="Nothing":
                b_f = 1.0
            elif self.Finishing=="Mortar":
                b_f = 0.28
            elif self.Finishing=="Paint":
                b_f = 0.8
            elif self.Finishing=="Tile":
                b_f = 0.7
            else:
                self.karbo="NaN"
                return
        
        self.b_f=b_f
        
        if  self.FA==0 and self.GGBS==0 and self.SF==0:             #no supplementary cementitious materials as FA, GGBS, SF (tab 1)
            b_s= 1.05                                               #βs is a correction factor for the replacement of SCMs,
        elif self.FA/(self.C+self.FA+self.GGBS+self.SF)<0.2 and self.GGBS==0 and self.SF==0:
            b_s=1.05
        elif self.FA/(self.C+self.FA+self.GGBS+self.SF)<0.4 and self.GGBS==0 and self.SF==0:
            self.b_s=1.1
        elif self.GGBS/(self.C+self.FA+self.GGBS+self.SF)<0.1 and self.FA==0 and self.SF==0:
            b_s=1.05
        elif self.GGBS/(self.C+self.FA+self.GGBS+self.SF)<0.2 and self.FA==0 and self.SF==0:
            b_s=1.1
        elif self.GGBS/(self.C+self.FA+self.GGBS+self.SF)<0.3 and self.FA==0 and self.SF==0:
            b_s=1.15
        elif self.GGBS/(self.C+self.FA+self.GGBS+self.SF)<0.4 and self.FA==0 and self.SF==0:
            b_s=1.2
        elif self.GGBS/(self.C+self.FA+self.GGBS+self.SF)<0.5 and self.FA==0 and self.SF==0:
            b_s=1.25
        elif self.GGBS/(self.C+self.FA+self.GGBS+self.SF)<0.8 and self.FA==0 and self.SF==0:
            b_s=1.3
        elif self.SF/(self.C+self.FA+self.GGBS+self.SF)<0.1 and self.FA==0 and self.GGBS==0:
            b_s=1.05
        elif self.SF/(self.C+self.FA+self.GGBS+self.SF)<0.2 and self.FA==0 and self.GGBS==0:
            b_s=1.1
        else:
            self.karbo="NaN"
            return
            
        self.b_s = b_s
        
        self.karbo = math.sqrt(2*self.D(self.t) * self.CO2 *365 / self.a(self.t))*10 

    def __repr__(self):
        return("Yang.2014")
       
    def D(self,t):
        b_h=(1-self.RH/100)**(0.6)  
                  # βh represents the effect of relative humidity (RH) on the CO2 diffusion rate
        e_pu = 1.5 * self.wb**2
  
        e_p=(0.1+2.62*self.wb**(4.2)*t*365)/(t*365*e_pu)
        D_co= 136.36*self.b_s* self.b_f* b_h *((self.S+self.G)/self.C)**(0.1) *(e_p)**2 #[cm^2/day]
        return D_co
        
    def a(self,t):
        M_ct=8.06* self.C *10**(-6)                     #[mol/cm^3] ???????????????????????????????????????
        a_u=1.031*self.wb/(0.194+self.wb)               # ultimate degree (α∞) of hydration
        a_h= t*365/(2+t*365)*a_u
        M_co = 44.01                            #[g/mol]
        a_co= a_h *M_ct * M_co                  #*10**(-6)     #[g/cm^3]
        return a_co
        
    
        
