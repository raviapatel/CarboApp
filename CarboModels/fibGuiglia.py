# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 08:18:38 2021

@author: gf5901
"""

from dataclasses import dataclass
from CarboModels.CarboModel import CarboModel 
import math
    
@dataclass
class fibGuiglia(CarboModel):
    """
    This is the carbonation model according to fib.2006 where the R_NAC^-1 is estimated by Guiglia.2013 Eq.16
    Funct: w(t), k(t)
    Variables:
        name= Name of cenario
        RH(%) 
        ToW(days) ime of wettness, days/year with rain > x(mm)
        p_sr(.) probabiloty of driving rain
        t_c(days) curing time
        f_c(MPa) 28Days
        C_co2(kg/m^3)peripheral concentration by weight of CO2.
    
    attributes
    ----------
    name : str
        Name of the model
    RH : float 
        Relative humidity (%)
    ToW : float 
        Time of wettness (days)
    p_sr : float 
        Probability of driving rain (-)
    t_c : float 
        Curing time (days)
    f_c : float 
        ? (mm²/year)
    C_co2 : float
        Peripheral concentration by weigth of CO2 (kg/m³)
    
    Methods
    -------
        Calculates self.karbo (mm/year^0.5)
    
    """
    color="red"

    name:str 
    RH:float 
    ToW:float 
    p_sr:float 
    t_c:float 
    f_c:float 
    C_co2:float 

    def __post_init__(self):
        #RH in (%)
        self.k_e= ((1-(self.RH/100)**5)/(1-0.65**6))**2.5
        #t_c in (days)
        self.k_c =(self.t_c/7)**(-0.567)
        #f_c in (MPa)
        self.R_NAC1= self.f_c**(-2.1)*1e7   #[mm²/year/(kg/m³)] nach Guiglia.2013 Eq.16

    def __repr__(self):
        return "fib MC SLD and Guiglia.2013"
    
    def k(self, t):
        #C_co2 in [kg/m³], t in [year]
        return math.sqrt(2*self.k_e*self.k_c*self.R_NAC1*self.C_co2)*self.W(t)
    
    def W(self, t):
        return (0.0767/t)**((self.p_sr*self.ToW/365)**0.446/2)

          

    
    
    
   