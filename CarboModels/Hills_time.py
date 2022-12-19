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
    mixture : str
        
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
    mixture:str
    ExCo:str 
    origin:str 
    age:float 
    
    def __post_init__(self):
        
        self.I_GGBS=0
        self.I_FA=0
        self.I_C=0
        
        if self.mixture=="ordinary portland cement (OPC)":
            self.I_C=1
        elif self.mixture=="OPC + blast furnace slag":
            self.I_GGBS=1
        elif self.mixture=="OPC + fly ash":
            self.I_FA=1
        else:
            self.karbo="NaN"
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
        else:
            self.karbo="NaN"
            return
            
        if self.origin == "Experimental":
            self.I_exp=1
        elif self.origin == "Strucutral":
            self.I_exp=0
        else:
            self.karbo="NaN"
            return

        self.karbo = math.exp(0.567-0.167*self.I_C+0.101*self.I_GGBS+0.129*self.I_FA+0.249*self.I_Exposed + 0.818*self.I_Sheltered+0.433*self.I_Indoors+(0.037-0.088*self.I_exp)*self.age+(-0.00046+0.0013*self.I_exp)*self.age**2)
        
    def __repr__(self):
        return("Hills.2015 time")
 