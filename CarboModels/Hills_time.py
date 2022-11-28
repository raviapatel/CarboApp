# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 16:41:26 2021

@author: gf5901
"""
from dataclasses import dataclass
from CarboModels.CarboModel import CarboModel 
import math
    
@dataclass
class Hills_time(CarboModel):
    """
    This is the carbonation model according Hills.2015 (time-depending model)
    k(t)
    Variables:
        name= Name of cenario
        C,GGBS,FA (kg/m³ or %)
        Exposed, Sheltered, Indoors, origin (bool), origin =concrete made in Lab?

   
    attributes
    ----------
    name : str
        Name of the Model
    GGBS : 
        
    FA : 
        
    C : 
        
    ExCo : str
        Exposure condition ('Exposed','Sheltered','Indoors','Other')
    origin : str
        Origin of the concrete ('Structural', 'Experimental')
    age : float
        Age of concrete (years)
        
    
    Methods
    -------
        Calculates self.karbo (mm/year^0.5)
    
    """
    color="brown"
    
    name:str 
    GGBS:float 
    FA:float 
    C:float 
    ExCo:str 
    origin:str 
    age:float 
    
    def __post_init__(self):
        
        self.I_GGBS=0
        self.I_FA=0
        self.I_C=0
        
        if self.GGBS>0 and self.FA==0:
            self.I_GGBS=1
        elif self.FA>0 and self.GGBS==0:
            self.I_FA=1
        elif self.C>0 and self.FA==0 and self.GGBS==0:
            self.I_C=1
        else:
            print('Error concrete mix not defined')
            return
            
        self.I_Exposed=0
        self.I_Sheltered=0
        self.I_Indoors=0
        
        if self.ExCo=="Exposed":         #==True and self.Sheltered ==False and self.Indoors==False:
            self.I_Exposed=1
        elif self.ExCo=="Sheltered":       #== True and self.Exposed==False and self.Indoors==False:
            self.I_Sheltered=1
        elif self.ExCo=="Indoors":            #==True and self.Sheltered == False and self.Exposed==False:
            self.I_Indoors=1

            
        if self.origin == "Experimental":
            self.I_exp=1
        else:
            self.I_exp=0

        self.karbo = math.exp(0.567-0.167*self.I_C+0.101*self.I_GGBS+0.129*self.I_FA+0.249*self.I_Exposed + 0.818*self.I_Sheltered+0.433*self.I_Indoors+(0.037-0.088*self.I_exp)*self.age+(-0.00046+0.0013*self.I_exp)*self.age**2)
        
    def __repr__(self):
        return("Hills.2015 time")
    
  #  def k(self,t):  #t in [year]
        
        #K in [mm/year^0.5])
    
    
 #  def x_c(self, t):
        """
        calculates one Carbonation depth for given time t 
        k(t)
        Parameters
        ----------
        t(years): TYPE
            Time

        Returns
        -------
        x_c(mm) : TYPE
            cabonation depth
        """
        
  #      x_c = self.k(t) * t**0.5
   #     return x_c
    
 #   def x_cList(self, t):
        """
        calculates Carbonation depth for time serie 
        k(t)
        Parameters
        ----------
        t(years): List
            Time

        Returns
        -------
        x_c(mm) : List with x.xx 
            cabonation depth
        """
   #     x_c =[]
    #    for i in t:
  #          x_c.append(round(self.k(i)* i**0.5, 2))
     #   return x_c
    
 