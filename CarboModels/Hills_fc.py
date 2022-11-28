# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 16:53:02 2021

@author: gf5901
"""

from CarboModels.CarboModel import CarboModel 
from dataclasses import dataclass
import math
    
@dataclass
class Hills_fc(CarboModel):
    """
    This is the carbonation model according Hills.2015 
    k=konst=karbo
    Variables:
        name= Name of cenario
        f_c [MPA]
        C [kg/m^3 or %]
        GGBS [kg/m^3 or %]
        FA [kg/m^3 or %]
        ExCo [bool]
        Sheltered  [bool]
        Indoors [bool]
           
    attributes
    ----------
    name : str
        Name of the Model
    C : float
        Clinker content (kg/m³)
    f_c : float
        28-day compressive strenght (MPa)
    ExpC : str
        Exposure class (XC1-XC4)
    RH : int
        Relative humidity (%)
    CO2 : float
        CO2 content (%)
    
    Methods
    -------
        Calculates self.karbo (mm/year^0.5)
    

    """
    color="purple"
    
    name:str
    GGBS:float 
    FA:float 
    C:float 
    ExCo:str 
    f_c:float
    
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
        elif self.ExCo=="Sheltered":       #== True and self.ExCo==False and self.Indoors==False:
            self.I_Sheltered=1
        elif self.ExCo=="Indoors":            #==True and self.Sheltered == False and self.ExCo==False:
            self.I_Indoors=1
            
        self.karbo = math.exp(1.066+1.761*self.I_C+2.062*self.I_GGBS+2.061*self.I_FA-0.639*self.I_Exposed -0.182*self.I_Sheltered-0.648*self.I_Indoors+(0.025-0.053*self.I_C-0.052*self.I_GGBS-0.05*self.I_FA)*self.f_c)
        
    def __repr__(self):
        return("Hills.2015 f_c")
    
