# -*- coding: utf-8 -*-

from dataclasses import dataclass
from CarboModels.CarboModel import CarboModel 
import math
    
@dataclass
class fibGuiglia(CarboModel):
    """
    This is the carbonation model according to fib.2006 where the R_NAC^-1 is estimated by Guiglia.2013 Eq.16
    
    attributes
    ----------
    name : str
        name of cenario
    RH : float 
        relative humidity of the carbonated layer [%]
    ToW : float 
        time of wettness (number of days with h_Nd>=2.5mm in a year) [days per year]
    p_dr : float 
        probability of driving rain [-]
    t_c : float 
        curing time [days]    
    f_c : float 
        mean value of the concrete compressive cylinder at 28 days [MPa]
    R_NAC1 : float 
        inverse effective carbonation resistance (with normal carbonation test NAC) [(mm²/year)/(kg/m³)]
    C_co2 : float
        peripheral concentration by weigth of CO2 [%]
    
    Methods
    -------
        calculates self.karbo [mm/year^0.5]

    
    """
    color="red"

    name:str 
    RH:float 
    ToW:float 
    p_dr:float 
    t_c:float 
    f_c:float 
    CO2:float 
    t:float
    y_R:float = 1.0
    y_RH:float = 1.0
    b_c:float = -0,567
    b_w:float = 0,446

    def __post_init__(self):
        self.CO2=0.0409*self.CO2*10000*44.01/1000000
        #RH in (%)
        self.k_e= ((1-(self.RH/(self.y_RH*100))**5)/(1-0.65**6))**2.5
        #t_c in (days)
        self.k_c =(self.t_c/7)**(self.b_c)
        #f_c in (MPa)
        self.R_NAC1= self.f_c**(-2.1)*1e7   #[(mm²/year)/(kg/m³)] nach Guiglia.2013 Eq.16
        #C_co2 in [kg/m³], t in [year]
        self.karbo = math.sqrt(2*self.k_e*self.k_c*self.y_R*self.R_NAC1*self.CO2)*self.W(self.t)
    
    def W(self, t):
        return (0.0767/t)**((((self.p_dr/100)*self.ToW/365)**self.b_w)/2)

    def __repr__(self):
        return "fib MC SLD and Guiglia.2013"          

    
    
    
   