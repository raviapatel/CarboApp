# -*- coding: utf-8 -*-

from dataclasses import dataclass
from CarboModels.CarboModel import CarboModel 
import math
    
@dataclass
class GreveDierfeld(CarboModel):
    """
    This is the carbonation model according to fib.2006 where the k_NAC from carboantion resistance class GreveDierfeld.2016d
    k=k(t)
    Variables:
        name= Name of cenario
        CEM (string) )["CEM I","CEM II/A", "CEM II/B", "CEM III/A", "CEM III/B", '?'] add '?' for unknwon cement type
        C (kg/m^3) cement
        FA (kg/m^3) fly ash
        SF (kg/m^3) silica fume
        GGBS (kg/m^3) slag
        L (lime stone)
        PZ (kg/m^3) puzzolan
        wb (-) water binder radio
        RH(%) 
        ToW(days) time of wettness, days/year with rain > x(mm)
        p_dr(-) probability of driving rain
        t_c(days) curing time
        C_co2[-] !!!! in Gereve-Dierfeld.2016a [kg/m^3], but C_a is only given in [Vol%]
    attributes
    ----------
    name : str 
        mame of cenario
    RH : float
        relative humidity [%]
    CEM : str
        
    wb : float 
    
    CO2 : float
    
    ToW : float 
    
    p_dr : float 
    
    t_c : float 
    
    
    Methods
    -------
        calculates self.karbo [mm/year^0.5]
        
    """
    color="olive"
    
    name:str 
    RH:float 
    Cem:str 
    wb:float 
    CO2:float
    ToW:float 
    p_dr:float 
    t_c:float 
    y_f:float = 1.0
    b_c:float = -0,567
    b_w:float = 0.446
    
    
    def __post_init__(self):
        
        
        #RH in (%)
        self.k_e= ((1-(self.RH/100)**5)/(1-0.65**6))**2.5
        
        #t_c in (days)
        self.k_c =(self.t_c/7)**(-0.567)
        
        CEM=self.Cem
        wb=self.wb

        #k_NAC from Tab 7 in GreveDierfeld.2016d -> wb value upper boundary, k_NAc conservativ
        
        if ((wb<=0.45) and (CEM =="CEM I" or CEM =="CEM II/A"))  :
            k_NAC=2
        elif (wb<=0.4) and (CEM =="CEM II/B" or CEM =="CEM III/A"):
            k_NAC=2
            
        elif (0.45<wb<=0.5) and (CEM =="CEM I" or CEM =="CEM II/A"): 
            k_NAC=3
        elif (0.4<wb<=0.45) and (CEM =="CEM II/B" or CEM =="CEM III/A"):
            k_NAC=3
        elif (wb<=0.4) and (CEM =="CEM III/B"):
            k_NAC=3

        elif (0.5<wb<=0.55) and (CEM =="CEM I" or CEM =="CEM II/A"): 
            k_NAC=4
        elif (0.45<wb<=0.5) and (CEM =="CEM II/B" or CEM =="CEM III/A"):
            k_NAC=4
        elif (0.4<wb<=0.45) and (CEM =="CEM III/B"):
            k_NAC=4
            
        elif (0.55<wb<=0.6) and (CEM =="CEM I" or CEM =="CEM II/A"): 
            k_NAC=5
        elif (0.5<wb<=0.55) and (CEM =="CEM II/B" or CEM =="CEM III/A"):
            k_NAC=5
        elif (0.45<wb<=0.5) and (CEM =="CEM III/B"):
            k_NAC=5
            
        elif (0.6<wb<=0.65) and (CEM =="CEM I" or CEM =="CEM II/A"): 
            k_NAC=6
        elif (0.55<wb<=0.6) and (CEM =="CEM II/B" or CEM =="CEM III/A"):
            k_NAC=6
        elif (0.5<wb<=0.55) and (CEM =="CEM III/B"):
            k_NAC=6
            
        elif (0.6<wb<= 0.65) and (CEM =="CEM II/B" or CEM =="CEM III/A"):
            k_NAC=7
        elif (0.55<wb<=0.6) and (CEM =="CEM III/B"):
            k_NAC=7

        else:
            self.karbo="NaN"
            return
            
        self.k_NAC=k_NAC
        
        self.k_a=self.CO2/(0.04/100)       #k_a[-] GreveDierfeld.2016a Eq. 3b 0.04 [Vol%]  /// GreveDierfeld.2016 Eq.31 k_a=1.1 (Dissertation)
        #C_co2 in [kg/m³], t in [year]
        self.karbo = self.k_NAC*math.sqrt(self.k_e*self.k_c*self.k_a) 

    def __repr__(self):
        return "fib MC SLD and GreveDierfeld.2016d"
    
    def k(self, t):
        #C_co2 in [kg/m³], t in [year]
        return self.karbo*self.W(t)
    
    def W(self, t):
        #p_dr= probability of driving rain [%], t in year
        return (0.0767/t)**((((self.p_dr/100)*self.ToW/365)**self.b_w)/2)


       

    
    
    
   