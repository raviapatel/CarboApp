# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 08:27:48 2021

@author: gf5901
"""

from CarboModels.CarboModel import CarboModel 
import math
    
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
    """
    color="orange"
    
    def __init__(self, name,  f_c, RH, CO2, FA_c, GGBS_c, Sheltered, Exposed): # change for cement type
    
        self.name = name
        self.f_c  = f_c
        
         
        if  Sheltered == True:
            self.e_s=1
        elif Exposed == True:
            self.e_s= f_c**(-0.2)
        else:
            print("Exposure not defined")
            self.e_s=float('NaN')
            return
        
        #Table 'Cement factors'

        if FA_c + GGBS_c <=0.2:
            self.g=-1.5
        elif FA_c<=0.3:
            print("FA_c is ", FA_c, 'reccomened is 0.3')
            self.g=-1.4
        elif GGBS_c<=0.5:
            print("GGBS_c is ", GGBS_c, 'reccomened is 0.5')
            self.g=-1.4
        else:
            print('SCM not fitted')
            return
            
        if 50 <= RH <=80:                             #[%]
            self.e_h=16*((RH-35)/100)*(1-RH/100)**(1.5)    
        else:
            print("Error RH")
            self.e_h=float('NaN')
            return
        
        if CO2 <=200/1000000: #ppm
            alpha= 1.4
            r=-1/4
        elif CO2 <= 300/1000000:
            alpha= 1
            r=0
        elif CO2 <= 500/1000000:
            alpha= 2.5
            r=-1/4
        elif CO2 <= 1000/1000000:
            alpha= 4.5
            r=-2/5
        elif CO2 <= 2000/1000000:
            alpha= 14
            r=-2/3
        else:
            print("Error in CO2 concentration (is > 2000ppm)")
            return
            
        
        if 20 < self.f_c <60:                              #[MPa]
            self.e_co=alpha*f_c**r
        elif f_c >= 60:
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
        return self.e_h*self.e_s*self.e_co*cem*(F_ct)**self.g 
    
    def x_c(self, t):
        """
        calculates one Carbonation depth for given time t 
        Parameters
        ----------
        t(years): TYPE
            Time

        Returns
        -------
        x_c(mm) : TYPE
            cabonation depth
        """
        x_c = self.k(t) * t**0.5
        return x_c
    
    def x_cList(self, t):
        """
        calculates Carbonation depth for time serie

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
            x_c.append(round(self.k(i)* i**0.5, 2))
        return x_c
    