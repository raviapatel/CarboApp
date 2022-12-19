# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 08:07:57 2021

@author: gf5901
"""

from dataclasses import dataclass
from CarboModels.CarboModel import CarboModel 
import math
    
@dataclass
class Ta(CarboModel):
    """
    This is the carbonation model according to Ta.2016
    a=konst, D=Konst, k=konst 
    Variables:
        name= Name of cenario
        {C, FA, S, G, W}[kg/m³] 
        {p_c,  p_FA,  p_w}[kg/m³]
         wc[-]
         CaO, SO3, SiO2, Al2O3, Fe2O3 [-] is the amount of X per weight of cement,
         phi_clinker [-] 
         S_max[mm]
         f_cem [MPa]
         t_c[days]
         RH[%] 
         T[°C] 
         CO2 [-]
         
    attributes
    ----------
    name : str
        Name of the Model
    C : float 
        Cement content (kg/m³)
    FA : float 
        Fly ash content (kg/m³)
    p_w : float 
        Density of water (kg/m³)
    p_c : float
        Density of cement (kg/m³)
    p_FA : float 
        Density of fly ash (kg/m³)
    wc : float 
        Water / cement ratio (-)
    S : float 
        Sand content (kg/m³)
    G : float 
        Gravel content (kg/m³)
    W : float 
        Water content (kg/m³)
    CaO : float 
        Amount of calcium oxide per weight of cement (-)
    SO3 : float 
        Amount of sulfur oxide per weight of cement (-)
    SiO2 : float 
        Amount of silicon oxide per weight of cement (-)
    Al2O3 : float 
        Amount of aluminium oxide per weight of cement (-)
    Fe2O3 : float 
        Amount of iron oxide per weight of cement (-)
    phi_clinker : float 
        cement clinker content (-)
    S_max : float 
        Maximum aggregate size (mm)
    f_cem : float 
        ?
    t_c : float  
        Curing period (days)
    RH : float 
        Relative humidity (%)
    T : float  
        Temperature (°C)
    CO2 : float
        CO2 concentration (-)
        
    Methods
    -------
        Calculates self.karbo (mm/year^0.5)

    """
    color="green"
    
    name:str 
    C:float 
    p_c:float 
    wc:float 
    FA:float 
    p_FA:float 
    S:float 
    G:float 
    W:float 
    p_w:float 
    CaO:float 
    SO3:float 
    SiO2:float 
    Al2O3:float 
    Fe2O3:float 
    phi_clinker:float 
    S_max:float 
    f_cem:float 
    t_c:float  
    RH:float 
    T:float  
    CO2:float
    
    def __post_init__(self):
        self.karbo = 0

        M_co= 44.01          #MCO2 and MCaO (g/mol) are the molar weight of CO2 and self.CaO respectively
        M_CaO= 56.0774       #(g/mol)
        #phi_clinker in [-], C in [kg/m³ Beton], self.CaO in [-] 
        self.a=0.75* self.phi_clinker *self.C* self.CaO * M_co/M_CaO  #Formel (5)     #[kg/m^3] the amount of CO2 absorbed per volume of completely carbonated concrete
        S_max= float(self.S_max)      

        #S_max in [mm]
        if 8<= S_max < 16:
            po_air= 0.035-(0.035-0.023)/(16-8)*(S_max-8)          #[-]
        elif 16 <= S_max < 31.5:
            po_air= 0.023 -(0.023-0.015)/(31.5-16) *(S_max-16)    #[-]
        else:
            self.karbo="NaN"
            return
        
        f_c= (7.84*self.f_cem)/(1+self.wc*self.p_c/self.p_w+po_air*self.p_c/self.C)**2 # Fig.2 (54) #[]????
        
        D_co28=10**(-7)*10**(-0.025*f_c)       #Fig.2 (25)         #[]???
        RH=self.RH/100            #[-]
        f_RH = (1-RH)**2 *RH**(2.6)            #Fig.2 (12)          #RH in [-] ???
        
    
        f_T = math.exp((4700*((self.T+273.15)-293))/(293*(self.T+273.15)))   #Fig.2 (20)   #Arrhenius’ law: T in [C] wird in [K] umgewandelt
        f_SGC = ((self.S+self.G)/self.C)**(0.1)      #Fig.2 [11]                  #[-] with S,G,C in [kg/m³ Beton]
        
        
        po= po_air + self.W/self.p_w - (0.249*(self.CaO-0.7* self.SO3) +0.191*self.SiO2 +1.118*self.Al2O3 - 0.357*self.Fe2O3)*self.C/1000     #po_carbon (n.u.) is the carbonated concrete porosity
        if 0.5< self.wc<0.8:
            n=1.8       #n (n.u.) is an empirical constant: n = 1.8 for 0.5 < W/C < 0.8. 
        else:
            self.karbo="NaN"
            return
        f_wc= 2437.7* math.exp(-5.592*self.wc)
        f_PwcFA = f_wc *( ( (0.93-3.95*0.94**(100*self.wc))*po -po_air ) / (self.W/self.p_w + self.C/self.p_c +self.FA/self.p_FA)  )**(n)
        
        f_tc= (1.9*10**(-2))/(10**(-0.025*f_c)) +(1- (1.9*10**(-2))/(10**(-0.025*f_c)))*math.sqrt(28/(0.01*self.t_c))
        
        #print(D_co28,f_RH, f_T,f_SGC,f_PwcFA,f_tc)
        self.D=D_co28 *f_RH * f_T * f_SGC *f_PwcFA *f_tc *365*24*60*60  #[m^2/year]=[m^2/s]**365*24*60*60 
        self.karbo = math.sqrt(2*self.D*self.CO2/self.a) * 1000 #[mm/year^0.5]
        
    def __repr__(self):
        return("Ta.2016")
    
    def a(self):
        """
        Returns
        -------
        float
            [kg/m^3]

        """
        return self.a
    
    def D(self):
        """
        Returns
        -------
        float 
            [m^2/year]

        """
        return self.D 