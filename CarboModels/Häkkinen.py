# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 13:52:09 2021

@author: gf5901
"""
from dataclasses import dataclass
from CarboModels.CarboModel import CarboModel 
import streamlit as st

@dataclass
class Häkkinen(CarboModel):
   
    """
    This is the carbonation model according Häkkinen.1993 in DuraCrete.1998
    
    attributes
    ----------
    name : str
        name of the model
    C : float
        clinker content (kg/m³)
    f_c : float
        28-day compressive strenght (MPa)
    FA : float
        fly ash (kg/m³) 
    SF : float
        silicia fume (kg/m³) 
    GGBS : 
        blast furnace slag (kg/m³) 
    
    Methods
    -------
        Calculates self.karbo (mm/year^0.5)
    
    This is the carbonation model according Häkkinen.1993 in DuraCrete.1998
    k=konst=karbo
    Variables:
        name= Name of cenario
        Exposed (bool)
        Sheltered (bool)
        C (kg/m³) 
        FA (kg/m³) 
        SF (kg/m³) 
        GGBS (kg/m³) 
        f_c (MPa)
    """
    
    name:str 
    C:float 
    f_c:float
    exposed:str  
    entrained:str
    FA:float 
    SF:float 
    GGBS:float 
    
    def __post_init__(self):
        
        if self.exposed == "Exposed to rain":  #Tab A2 in DuraCRete.1998
            self.c_env = 0.5
        elif self.exposed == "Sheltered from rain":
            self.c_env = 1.0   
        else:
            print('Error: exposure')
            return
        
        if self.entrained == "Air entrained":
            self.c_air = 0.7
        elif self.entrained == "Not air entrained":
            self.c_air = 1.0
        
        if self.C>0 and  self.FA==0 and self.SF==0 and self.GGBS==0:   #Tab A2 in DuraCRete.1998
            self.a=1800
            self.b=-1.7
        elif self.C>0 and self.FA>0 and self.SF==0 and self.GGBS==0:
            #print('recommended value FA=28%, here:', FA/(C+FA+SF+GGBS)*100)
            self.a=360
            self.b=-1.2
        elif self.C>0 and self.FA==0 and self.SF>0 and self.GGBS==0:
            #print('recommended value SF=9%, here:', SF/(C+FA+SF+GGBS)*100)
            self.a=400
            self.b=-1.2
        elif self.C>0 and self.FA==0 and self.SF==0 and self.GGBS>0:
            #print('recommended value GGBS=70%, here:', GGBS/(C+FA+SF+GGBS)*100)
            self.a=360
            self.b=-1.2
        else:
            print('Error: mixture')
            st.error("Error: Mixture")
            self.karbo=float('NaN')
            return
        
        self.karbo = self.c_env*self.c_air*self.a*self.f_c**self.b
    

    def __repr__(self):
        return("Häkkinen.1993")



    

    