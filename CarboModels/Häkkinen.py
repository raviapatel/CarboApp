# -*- coding: utf-8 -*-

from dataclasses import dataclass
from CarboModels.CarboModel import CarboModel 
#import streamlit as st

@dataclass
class Häkkinen(CarboModel):
   
    """
    This is the carbonation model according to Häkkinen.1993 in DuraCrete.1998
    
    attributes
    ----------
    name : str
        name of cenario
    f_c : float
        28-day compressive strenght [MPa]  
    exposed : str
        if component is exposed to rain ['Exposed to rain', 'Sheltered from rain']
    entrained : str
        if component is air entrained ['Air entrained', 'Not air entrained']
    C : float
        clinker content [kg/m³]
    FA : float
        fly ash content [kg/m³] 
    SF : float
        silicia fume content [kg/m³] 
    GGBS : 
        blast furnace slag content [kg/m³] 
    
    Methods
    -------
        calculates self.karbo [mm/year^0.5]

    """
    
    name:str 
    f_c:float
    ExCo:str  
    AirEntrained:str 
    C:float 
    FA:float 
    SF:float 
    GGBS:float 
    
    def __post_init__(self):
        
        if self.ExCo == "Exposed to Rain":  #Tab A2 in DuraCRete.1998
            self.c_env = 0.5
        elif self.ExCo == "Sheltered from Rain" or self.ExCo == "Indoor":
            self.c_env = 1.0   
        else:
            self.karbo="NaN"
            return
            
        
        if self.AirEntrained == "Air Entrained":
            self.c_air = 0.7
        elif self.AirEntrained == "Not Air Entrained":
            self.c_air = 1.0
        else:
            self.karbo="NaN"
            return
        
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
            self.karbo="NaN"
            return
        
        self.karbo = self.c_env*self.c_air*self.a*self.f_c**self.b
    

    def __repr__(self):
        return("Häkkinen.1993")



    

    