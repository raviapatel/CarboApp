# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 11:45:13 2022

@author: marco
"""

from CarboModels.CarboModel import CarboModel 
import math
    
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
    """
    color="red"

    def __init__(self, name, RH, ToW, p_sr, t_c, f_c, C_co2):
        self.name =name
        self.RH= RH 
        self.ToW=ToW
        self.p_sr= p_sr
        #self.t_c= t_c 
        #self.f_c=f_c 
        self.C_co2=C_co2
        
        #RH in (%)
        self.k_e= ((1-(RH/100)**5)/(1-0.65**6))**2.5
        #t_c in (days)
        self.k_c =(t_c/7)**(-0.567)
        #f_c in (MPa)
        self.R_NAC1= f_c**(-2.1)*1e7   #[mm²/year/(kg/m³)] nach Guiglia.2013 Eq.16
    

    def __repr__(self):
        return "fib MC SLD and Guiglia.2013"
    
    def k(self, t):
        #C_co2 in [kg/m³], t in [year]
        return math.sqrt(2*self.k_e*self.k_c*self.R_NAC1*self.C_co2)*self.W(t)
    
    def W(self, t):
        return (0.0767/t)**((self.p_sr*self.ToW/365)**0.446/2)