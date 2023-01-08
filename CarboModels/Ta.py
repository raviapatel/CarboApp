# -*- coding: utf-8 -*-

from dataclasses import dataclass
from CarboModels.CarboModel import CarboModel 
import math
    
@dataclass
class Ta(CarboModel):
    """
    This is the carbonation model according to Ta.2016
         
    attributes
    ----------
    name : str
        name of cenario
    C : float 
        cement content [kg/m³]
    FA : float 
        fly ash content [kg/m³]
    p_w : float 
        density of water [kg/m³]
    p_c : float
        density of cement [kg/m³]
    p_FA : float 
        density of fly ash [kg/m³]
    wb : float 
        water / binder ratio [-]
    S : float 
        sand content [kg/m³]
    G : float 
        gravel content [kg/m³]
    W : float 
        water content [kg/m³]
    CaO : float 
        amount of calcium oxide per weight of cement [-]
    SO3 : float 
        amount of sulfur oxide per weight of cement [-]
    SiO2 : float 
        amount of silicon oxide per weight of cement [-]
    Al2O3 : float 
        amount of aluminium oxide per weight of cement [-]
    Fe2O3 : float 
        amount of iron oxide per weight of cement [-]
    phi_clinker : float 
        cement clinker content [-]
    S_max : float 
        maximum aggregate size [mm]
    f_cem : float 
        standard strenght class of cement [MPa]
    t_c : float  
        curing period [days]
    RH : float 
        relative humidity [%]
    T : float  
        temperature [°C]
    CO2 : float
        CO2 concentration jetzt in [%] ?   [-] [oder [kg/m³]?]
        
    Methods
    -------
        calculates self.karbo [mm/year^0.5]

    """
    color="green"
    
    name:str 
    C:float 
    p_c:float 
    wb:float 
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
        self.CO2=0.0409*self.CO2*10000*44.01/1000000
        
        M_co = 44.01          #MCO2 and MCaO (g/mol) are the molar weight of CO2 and self.CaO respectively
        M_CaO = 56.0774       #(g/mol)
        #phi_clinker in [-], C in [kg/m³ Beton], self.CaO in [-] 
        self.a = 0.75* self.phi_clinker *self.C* self.CaO * M_co/M_CaO  #Formel (5)     #[kg/m^3] the amount of CO2 absorbed per volume of completely carbonated concrete
        S_max = self.S_max      

        #S_max in [mm]
        if 8 <= S_max < 16:
            po_air= 0.035-(0.035-0.023)/(16-8)*(S_max-8)          #[-]
        elif 16 <= S_max <= 31.5:
            po_air= 0.023 -(0.023-0.015)/(31.5-16) *(S_max-16)    #[-]
        else:
            self.karbo="NaN"
            return
        
        f_c = (7.84*self.f_cem)/((1+self.wb*self.p_c/self.p_w+po_air*self.p_c/self.C)**2) # Fig.2 (54) #[]????
        
        D_co28 = (10**(-7))*10**(-0.025*f_c)       #Fig.2 (25)         #[]???
        RH=self.RH/100            #[-]
        f_RH = (1-RH)**2 *RH**(2.6)            #Fig.2 (12)          #RH in [-] ???
        
    
        f_T = math.exp((4700*((self.T+273.15)-293))/(293*(self.T+273.15)))   #Fig.2 (20)   #Arrhenius’ law: T in [C] wird in [K] umgewandelt
        f_SGC = ((self.S+self.G)/self.C)**(0.1)      #Fig.2 [11]                  #[-] with S,G,C in [kg/m³ Beton]
        
        
        po = po_air + self.W/self.p_w - (0.249*(self.CaO-0.7* self.SO3) +0.191*self.SiO2 +1.118*self.Al2O3 - 0.357*self.Fe2O3)*self.C/1000     #po_carbon (n.u.) is the carbonated concrete porosity
        if 0.5< self.wb<0.8:
            n=1.8       #n (n.u.) is an empirical constant: n = 1.8 for 0.5 < W/C < 0.8. 
        else:
            self.karbo="NaN"
            return
        f_wb = 2437.7* math.exp(-5.592*self.wb)
        f_PwbFA = f_wb *( ( (0.93-3.95*0.94**(100*self.wb))*po -po_air ) / (self.W/self.p_w + self.C/self.p_c +self.FA/self.p_FA)  )**(n)
        
        f_tc = (1.9*10**(-2))/(10**(-0.025*f_c)) +(1-(1.9*10**(-2))/(10**(-0.025*f_c)))*math.sqrt(28/(0.01*self.t_c))

        self.D=D_co28 *f_RH * f_T * f_SGC *f_PwbFA *f_tc *365*24*60*60 #[m^2/year]=[m^2/s]**365*24*60*60 

        self.karbo = math.sqrt(2*self.D*self.CO2/self.a)*1000 #[mm/year^0.5]
        
    def __repr__(self):
        return("Ta.2016")
    