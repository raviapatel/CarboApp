# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 14:55:34 2021

@author: gf5901
"""
from dataclasses import dataclass
from CarboModels.CarboModel import CarboModel 
import streamlit as st
import math
    
@dataclass
class Yang(CarboModel):
    """
    
    This is the carbonation model according Yang.2014
    Funct: D(t), a(t), k(t)
    Variables:
        name= Name of cenario
        {C,S,G, FA, GGBS, SF}[kg/m³]
        wc(-)
        RH(%),
        C_co2,[kg/m^3] is the peripheral concentration by weight of CO2.
        Finishing(bool)
        
    attributes
    ----------
    name : str
        Name of the Model
    C : float
        Cement content (kg/m³)
    S : float
        Sand content (kg/m³)
    G : float
        Gravel content (kg/m³)
    FA : float
        Fly ash content (?)
    GGBS : float
        Ground granulated blast furnace slag content (kg/m³)
    SF : float
        Silica fume content (kg/m³)
    wc : float
        Water / cement ratio (-)
    RH : float
         Relative humidity around concrete surface (%) 
    C_co2 : float
    
    Location : str
    
    Finishing : str
     
    
    Methods
    -------
        Calculates self.karbo (mm/year^0.5)    
   
    """
    
    name:str 
    t:float
    C:float 
    S:float 
    G:float 
    FA:float 
    GGBS:float 
    SF:float 
    wc:float 
    RH:float 
    C_co2:float 
    Location:str
    Finishing:str
    
    def __post_init__(self):
       
        self.C_co2=self.C_co2/1000                                  # [g/cm^3] = [kg/m^3]/1000
        
        if self.Location=="Outdoor":
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
        elif self.Location=="Indoor":
            if self.Finishing =="Nothing":
                b_f = 1.0
            elif self.Finishing=="Mortar":
                b_f = 0.28
            elif self.Finishing=="Paint":
                b_f = 0.8
            elif self.Finishing=="Tile":
                b_f = 0.7
        
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
            st.warning("Calculation could not be executed! Mixture design not included in the model!")
            self.karbo = 0
            b_s = 0
            
        self.b_s = b_s
        
        self.karbo = math.sqrt(2*self.D(self.t) * self.C_co2 *365 / self.a(self.t))*10 

    def __repr__(self):
        return("Yang.2014")
       
    def D(self,t):
        b_h=(1-self.RH/100)**(0.6)  
        print(self.wc)                    # βh represents the effect of relative humidity (RH) on the CO2 diffusion rate
        e_pu = 1.5 * self.wc**2
        print(e_pu)
        e_p=(0.1+2.62*self.wc**(4.2)*t*365)/(t*365*e_pu)
        D_co= 136.36*self.b_s* self.b_f* b_h *((self.S+self.G)/self.C)**(0.1) *(e_p)**2 #[cm^2/day]
        return D_co
        
    def a(self,t):
        M_ct=8.06* self.C *10**(-6)                     #[mol/cm^3] ???????????????????????????????????????
        a_u=1.031*self.wc/(0.194+self.wc)               # ultimate degree (α∞) of hydration
        a_h= t*365/(2+t*365)*a_u
        M_co = 44.01                            #[g/mol]
        a_co= a_h *M_ct * M_co                  #*10**(-6)     #[g/cm^3]
        return a_co
        
    
   # def k(self, t):
    #    return math.sqrt(2*self.D(t) * self.C_co2 *365 / self.a(t)  )*10     #mm/t^0.5
    
   # def x_c(self,t):
    #    return self.k(t)*t**0.5
        
#    def x_cList(self, t):
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
 #       x_c =[]
  #      for i in t:
   #         x_c.append(round(self.k(i)*i**0.5, 2))
    #    return x_c            

    
        
