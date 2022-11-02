# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 14:55:34 2021

@author: gf5901
"""

from CarboModels.CarboModel import CarboModel 
import math
    
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
    """
    
    def __init__(self, name,C,S,G,wc,RH,C_co2, Finishing, FA, GGBS, SF):
        self.name =name
        self.C=C
        self.S=S
        self.G=G
        self.FA=FA
        self.GGBS=GGBS
        self.SF= SF
        self.wc=wc
        self.RH=RH
        self.C_co2=C_co2/1000 # [g/cm^3] = [kg/m^3]/1000
        self.Finishing=Finishing
        
        if Finishing==False:
            b_f = 1                           #βf represents the delayed carbonation process by finishing materials
        else:
            print("error: surface finish see Tab 2")
            b_f = input("Please enter an float for b_f:\n")
            b_f= float(b_f)
            print('You entered', b_f)
        
        self.b_f=b_f
        
        if  FA==0 and GGBS==0 and SF==0:      #no supplementary cementitious materials as FA, GGBS, SF (tab 1)
            b_s= 1.05                          #βs is a correction factor for the replacement of SCMs,
        elif FA/(C+FA+GGBS+SF)<0.2 and GGBS==0 and SF==0:
            b_s=1.05
        elif FA/(C+FA+GGBS+SF)<0.4 and GGBS==0 and SF==0:
            b_s=1.1
        elif GGBS/(C+FA+GGBS+SF)<0.1 and FA==0 and SF==0:
            b_s=1.05
        elif GGBS/(C+FA+GGBS+SF)<0.2 and FA==0 and SF==0:
            b_s=1.1
        elif GGBS/(C+FA+GGBS+SF)<0.3 and FA==0 and SF==0:
            b_s=1.15
        elif GGBS/(C+FA+GGBS+SF)<0.4 and FA==0 and SF==0:
            b_s=1.2
        elif GGBS/(C+FA+GGBS+SF)<0.5 and FA==0 and SF==0:
            b_s=1.25
        elif GGBS/(C+FA+GGBS+SF)<0.8 and FA==0 and SF==0:
            b_s=1.3
        elif SF/(C+FA+GGBS+SF)<0.1 and FA==0 and GGBS==0:
            b_s=1.05
        elif SF/(C+FA+GGBS+SF)<0.2 and FA==0 and GGBS==0:
            b_s=1.1
        else:
            print("error b_s: Substitution of SCMs not definded in Tab 1")
            b_s = input("Please enter an float for b_s:\n")
            b_s= float(b_s)
            print('You entered', b_s)
        self.b_s=b_s

    def __repr__(self):
        return("Yang.2014")
       
    def D(self,t):
        b_h=(1-self.RH/100)**(0.6)                # βh represents the effect of relative humidity (RH) on the CO2 diffusion rate
        e_pu = 1.5 * self.wc**2
        e_p=(0.1+2.62*self.wc**(4.2)*t*365)/(t*365*e_pu)
        D_co= 136.36*self.b_s* self.b_f* b_h *((self.S+self.G)/self.C)**(0.1) *(e_p)**2 #[cm^2/day]
        return D_co
        
    def a(self,t):
        M_ct=8.06* self.C *10**(-6)               #[mol/cm^3] ???????????????????????????????????????
        a_u=1.031*self.wc/(0.194+self.wc)              # ultimate degree (α∞) of hydration
        a_h= t*365/(2+t*365)*a_u
        M_co = 44.01                         #[g/mol]
        a_co= a_h *M_ct * M_co #*10**(-6)     #[g/cm^3]
        return a_co
        
    
    def k(self, t):
        return math.sqrt(2*self.D(t) * self.C_co2 *365 / self.a(t)  )*10     #mm/t^0.5
    
    def x_c(self,t):
        return self.k(t)*t**0.5
        
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
            x_c.append(round(self.k(i)*i**0.5, 2))
        return x_c            

    
        
