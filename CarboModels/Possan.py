# -*- coding: utf-8 -*-

from dataclasses import dataclass
from CarboModels.CarboModel import CarboModel  
import math
    
@dataclass
class Possan(CarboModel):
    """
    This is the carbonation model according to Possan.2021
    
    attributes
    ----------
    name : str
        name of cenario
    CEM : str 
        cment type
    f_c : float 
        concrete compressive strenght [MPa]
    ExCo : str
        Exposure condition ['Exposed','Sheltered','Indoors']
    CO2 : float  
        CO2 content in the atmosphere [%]
    RH : float
        relative humidity [%]
    
    Methods
    -------
        calculates self.karbo [mm/year^0.5]
    
    """
    color="blue"
    
    name:str 
    C:float 
    FA:float 
    SF:float 
    CEM:str 
    f_c:float 
    ExCo:str 
    CO2:float  
    RH:float
    
    def __post_init__(self):

        self.RH=self.RH/100 #[-]
        print(self.RH)
        #Table 3b
        if self.ExCo == "Exposed to Rain":
            k_ce=0.65
            
        elif self.ExCo == "Sheltered from Rain":
            k_ce=1
            
        elif self.ExCo == "Indoor":
            k_ce=1.3
        else:
            self.karbo="NaN"
            return
    
        ad = ((self.FA+self.SF)/self.C)*100 # puzzolanic addition content related to cement mass in [%] 
        
        #Table 3a
        if self.CEM=='CEM I': #CEM IV/A, CEM IV/B
            k_c=19.8
            k_fc=1.7
            k_ad=0.24
            k_CO2=18 
            k_UR=1300
        
        elif self.CEM=='CEM II/A-L':
            k_c=21.68
            k_fc=1.5
            k_ad=0.24
            k_CO2=18
            k_UR=1100
            
        elif self.CEM=='CEM II/A-S' or self.CEM=='CEM II/B-S':
            k_c=22.48
            k_fc=1.5
            k_ad=0.32
            k_CO2=15.5
            k_UR=1300
            
        elif self.CEM=='CEM II/A-V':
            k_c=23.66
            k_fc=1.5
            k_ad=0.32
            k_CO2=15.5
            k_UR=1300
            
        elif self.CEM=='CEM III/A':
            k_c=30.5
            k_fc=1.7
            k_ad=0.32
            k_CO2=15.5
            k_UR=1300
            
        elif self.CEM=='CEM IV/A' or self.CEM=='CEM IV/B':
            k_c=33.27
            k_fc=1.7
            k_ad=0.32
            k_CO2=15.5
            k_UR=1000
        else:
            self.karbo="NaN"
            return
        
        #Formula (13)
        #t [year], f_c[MPa], CO2[%], RH[-]
        eq1=(k_ad*ad**(3/2)/(40+self.f_c))+(k_CO2*self.CO2**(0.5)/(60+self.f_c))-(k_UR*(self.RH-0.58)**2/(100+self.f_c)) 
        print(eq1)
        self.karbo = k_c *(20/self.f_c)**(k_fc) * math.exp(eq1)*k_ce 
        print(self.karbo)
        
        
    def __repr__(self):
        return ("Possan.2021 ")
    
    def x_c(self,t):
        return self.karbo*(t/20)**0.5
    
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
        t=int(t)
        x_c =[]
        for i in range(1,t+1):
            x_c.append(round(self.karbo*(i/20)**0.5, 2))
        return x_c
    
        
    

    
    
    