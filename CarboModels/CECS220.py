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
    k=konst=karbo
    Variables:
        name= Name of cenario
        FA_c(-) is the fly ash content (weight ratio).
        f_c(MPa) 28Days
        load("tensile", "compressiv")
        T (°C)
        CO2 (-) =density around concrete surface
        RH(%) 
    """
    
    name:str 
    f_c:float 
    FA:float 
    tension:str 
    location:str
    T:float 
    RH:float 
    CO2:float 
    
    def __post_init__(self):
        
        self.k_CO=math.sqrt(self.CO2/0.03)
        self.k_kt=1.2
        
        
        if self.tension=="tension":
            self.k_ks=1.1
        else:
            self.k_ks=1
            
        if self.location=="corner":
                self.k_kl=1.4
        else:
                self.k_kl=1
                
        self.k_F=1+13.34*(self.FA)**(3.3)   #FA_c is the fly ash content (weight ratio).
        #f_c in [MPa]?, CO2 [?]=density around concrete surface
        self.karbo=3*self.k_CO*self.k_kl*self.k_kt*self.k_ks*self.k_F*self.T**(1/4)*self.RH**(1.5)*(1-self.RH)*(58/self.f_c-0.76)*math.sqrt(365)

       
    def __repr__(self):
        return("CECS220")

    
    
#    def x_c(self, t):
        """
        Carbonation depth

        Parameters
        ----------
        t(years): TYPE
            Time

        Returns
        -------
        x_c(mm) : TYPE
            cabonation depth
        """
                #p_sr= probability of driving rain [-], t in year
        #t [days]??????????????
#       x_c=self.k()*math.sqrt(t)
   #     return x_c
    
    def x_cList(self, t):
        """
        Carbonation depth
    
        Parameters
        ----------
        t(years): List
            Time
    
        Returns
        -------
        x_c(mm) : List with x.xx 
            cabonation depth
        """
        x_c =[]
        for i in t:
            x_c.append(round(self.k()*math.sqrt(i),2))
        return x_c    
        