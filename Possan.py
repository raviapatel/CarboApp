# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 16:42:45 2021

@author: gf5901
"""
from CarboModels.CarboModel import CarboModel  
import math
    
class Possan(CarboModel):
    """
    This is the carbonation model according to Possan.2021
    k=konst=karbo
    Variables:    
    name (string) = name of input data set
     C (kg/m^3) =cement content
    FA (kg/m^3) = fly ash contetnt
    SF (kg/m^3) =Silica fume content
    GGBS (kg/m^3) slag
    LS (kg/m^3) lime stone
    PZ (kg/m^3) puzzolan
    CEM (string) )["CEM I","CEM II/A", "CEM II/B", "CEM III/A", "CEM III/B", '?'] add '?' for unknwon cement type
    f_c (MPa)   = comressive strength
    Exposed (bool)
    Sheltered (bool)
    Indoors (bool) 
    CO2 (-) =density around concrete surface
    RH (%)
    
    """
    color="blue"
    
    def __init__(self, name, C, FA, SF, GGBS, LS, PZ, CEM, f_c,Exposed,Sheltered,Indoors, CO2, RH):

        self.name =name
        self.C =C
        self.FA=FA
        self.SF =SF
        self.CEM=CEM
        self.f_c=f_c
        self.Exposed =Exposed
        self.Sheltered= Sheltered
        self.Indoors = Indoors
        self.CO2 = CO2*100 #(%)
        self.RH = RH/100   #(-)
        
        #for HuyVu:
        if CEM == '?':    
            self.CEM= self.findCEM(C, FA, SF, GGBS, LS, PZ)
            print('cement type defined as:', self.CEM)

        RH=RH/100 #[-]
        CO2=CO2*100 #[%]
    
        if Exposed==True and Sheltered==False and Indoors==False:
            k_ce=0.65
            
        elif Exposed==False and Sheltered==True and Indoors==False:
            k_ce=1
            
        elif Exposed==False and Sheltered==False and Indoors==True:
            k_ce=1.3
        else:
            print('Error: Exposure not defined')
            return
    
        ad= (FA+SF)/C *100 # puzzolanic addition content related to cement mass in [%] 
        
        if self.CEM=='CEM I':
            k_c=19.8
            k_fc=1.7
            k_ad=0.24
            k_CO2=18 
            k_UR=1300
        
        elif self.CEM== 'CEM II/A-L':
            k_c=21.68
            k_fc=1.5
            k_ad=0.24
            k_CO2=18
            k_UR=1100
            
        elif self.CEM== 'CEM II/A-S' or self.CEM=='CEM II/B-S':
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
            print('error: CEM not defined')
            self.karbo=float('NaN')
            return
    
        #t [year], f_c[MPa], CO2[%], RH[-]
        eq1=( k_ad*ad**(3/2)/(40+f_c) )+( k_CO2*CO2**(0.5) /(60+f_c) )-(k_UR*(RH-0.58)**2 / (100+f_c) ) 
        self.karbo = k_c *(20/f_c)**(k_fc) * math.exp(eq1)*k_ce      
        
        
    def __repr__(self):
        return ("Possan.2021 ") #"(" + self.CEM +")")
    
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
        x_c =[]
        for i in t:
            x_c.append(round(self.karbo*(i/20)**0.5, 2))
        return x_c
    
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
            return 'CEM II/A-L'
        elif 0.8 <= C/ges <= 0.94 and 0.06<= GGBS/ges <= 0.2: 
            return 'CEM II/A-S'
        elif 0.65 <= C/ges <= 0.79 and 0.21<= GGBS/ges <= 0.35: 
            return 'CEM II/B-S'
        elif 0.8 <= C/ges <= 0.94 and 0.06<= FA/ges <= 0.2: # fly ash kieselsäurereich (V)
            return 'CEM II/A-V'       
        elif 0.35 <= C/ges <= 0.64 and 0.36<= GGBS/ges <= 0.65: 
            return 'CEM III/A'  
        elif 0.65 <= C/ges <= 0.89 and 0.36<= FA+SF+PZ/ges <= 0.65: #PZ Puzzolan (P, O)
            return 'CEM IV/A'  
        elif 0.45 <= C/ges <= 0.64 and 0.36<= FA+SF+PZ/ges <= 0.55: #PZ Puzzolan (P, O)
            return 'CEM IV/B' 
        else:
            return 'unknown' 
            
        
    

    
    
    