# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:14:34 2021

@author: gf5901
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 08:18:38 2021

@author: gf5901
"""

from CarboModels.CarboModel import CarboModel 
import math
import numpy as np
    
class fibGreveDierfeld(CarboModel):
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
        ToW(days) ime of wettness, days/year with rain > x(mm)
        p_sr(-) probabiloty of driving rain
        t_c(days) curing time
        C_co2[-] !!!! in Gereve-Dierfeld.2016a [kg/m^3], but C_a is only given in [Vol%]
    """
    color="olive"
    
    def __init__(self, name, CEM,  C, FA, SF, GGBS, L, PZ, wb, RH, ToW, p_sr, t_c, CO2):
        self.name =name
        self.RH= RH 
        self.ToW=ToW
        self.p_sr= p_sr
        self.t_c= t_c 
        
        
        #RH in (%)
        k_e= ((1-(RH/100)**5)/(1-0.65**6))**2.5
        
        #t_c in (days)
        k_c =(t_c/7)**(-0.567)
        
        if CEM == '?':
            CEM= findCEM(C, FA, SF, GGBS, L, PZ)
        
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
            k_NAC=np.nan
            
        self.k_a=CO2/(0.04/100)       #k_a[-] GreveDierfeld.2016a Eq 3b 0.04 [Vol%]/// GreveDierfeld.2016 Eq.31 k_a=1.1
        #print("k_a",k_a)
        #print("k_NAC", k_NAC)
        #C_co2 in [kg/m³], t in [year]
        self.karbo = k_NAC*math.sqrt(k_e*k_c*self.k_a) 

    def __repr__(self):
        return "fib MC SLD and GreveDierfeld.2016d"
    
    def findCEM(self, C, FA, SF, GGBS, L=0, PZ=0):
        """
        Function defines Cement according DIN 197.1 Tab. 1 with the SCMs from mixdesign
        -> in HuyVu C ='CEM I' and SCMs are added

        Parameters
        ----------
        C : TYPE
            usually clinker, but here 'CEM I'
        FA : TYPE
            Fly ash (v).
        SF : TYPE
            silika fume.
        GGBS : TYPE
            slag.
        L : TYPE, optional
            Limestone. The default is 0.
        PZ : TYPE, optional
            Puzzolan (P, Q). The default is 0.

        Returns
        -------
        str
            cement type like DIN 197.1 Tab. 1

        """
        #print('C, FA, SF, GGBS, L, PZ')
        #print(C, FA, SF, GGBS, L, PZ)
        
        ges = (C+FA+SF+GGBS+L+PZ)
        
        if C/ges >=0.95:
            return 'CEM I'
        elif 0.8 <= C/ges <= 0.97 and 0.06<= L/ges <= 0.2: #L=limestone
            return 'CEM II/A' #'-L'
        elif 0.8 <= C/ges <= 0.94 and 0.06<= GGBS/ges <= 0.2: 
            return 'CEM II/A' #'-S'
        elif 0.65 <= C/ges <= 0.79 and 0.21<= GGBS/ges <= 0.35: 
            return 'CEM II/B' #'-S'
        elif 0.8 <= C/ges <= 0.94 and 0.06<= FA/ges <= 0.2: # fly ash kieselsäurereich (V)
            return 'CEM II/A' #'-V'       
        elif 0.35 <= C/ges <= 0.64 and 0.36<= GGBS/ges <= 0.65: 
            return 'CEM III/A'  
        elif 0.65 <= C/ges <= 0.89 and 0.36<= FA+SF+PZ/ges <= 0.65: #PZ Puzzolan (P, O)
            return 'CEM IV/A'  
        elif 0.45 <= C/ges <= 0.64 and 0.36<= FA+SF+PZ/ges <= 0.55: #PZ Puzzolan (P, O)
            return 'CEM IV/B' 
        else:
            return 'unknown'
    
    def k(self, t):
        #C_co2 in [kg/m³], t in [year]
        return self.karbo*self.W(t)
    
    def W(self, t):
        #p_sr= probability of driving rain [-], t in year
        return (0.0767/t)**((self.p_sr*self.ToW/365)**0.446/2)


       

    
    
    
   