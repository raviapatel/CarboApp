# -*- coding: utf-8 -*-

from CarboModels.CarboModel import CarboModel 
from dataclasses import dataclass
import math
    
@dataclass
class Hills_fc(CarboModel):
    """
    This is the carbonation model according to Hills.2015 (strenght-depending model)
           
    attributes
    ----------
    name : str
        name of cenario
    mixture : str
        content of concrete ['Ordinary Portland Cement (OPC)','OPC + Blast Furnace Slag','OPC + Fly Ash']
    f_c : float
        28-day compressive strenght [MPa]
    ExCo : str
        exposure condition ['Exposed to Rain','Sheltered to Rain','Indoors']
    RH : float
        relative humidity [%]
    CO2 : float
        CO2 content [%]
    
    Methods
    -------
        calculates self.karbo [mm/year^0.5]
    

    """
    color="purple"
    
    name:str
    mixture:str
    ExCo:str 
    f_c:float
    
    def __post_init__(self):
        
        self.I_GGBS=0
        self.I_FA=0
        self.I_C=0
        
        if self.mixture=="Ordinary Portland Cement (OPC)":
            self.I_C=1
        elif self.mixture=="OPC + Blast Furnace Slag":
            self.I_GGBS=1
        elif self.mixture=="OPC + Fly Ash":
            self.I_FA=1
        else:
            self.karbo="NaN"
            return
            
        self.I_Exposed=0
        self.I_Sheltered=0
        self.I_Indoors=0
        
        if self.ExCo=="Exposed to Rain":         #==True and self.Sheltered ==False and self.Indoors==False:
            self.I_Exposed=1
        elif self.ExCo=="Sheltered from Rain":       #== True and self.ExCo==False and self.Indoors==False:
            self.I_Sheltered=1
        elif self.ExCo=="Indoor":            #==True and self.Sheltered == False and self.ExCo==False:
            self.I_Indoors=1
        else:
            self.karbo="NaN"
            return
            
        self.karbo = math.exp(1.066+1.761*self.I_C+2.062*self.I_GGBS+2.061*self.I_FA-0.639*self.I_Exposed -0.182*self.I_Sheltered-0.648*self.I_Indoors+(0.025-0.053*self.I_C-0.052*self.I_GGBS-0.05*self.I_FA)*self.f_c)
        
    def __repr__(self):
        return("Hills.2015 f_c")
    
