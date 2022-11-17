# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 08:07:57 2021

@author: gf5901
"""

from CarboModels.CarboModel import CarboModel 
import math
    
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
    """
    color="green"
    
    def __init__(self, name, C, p_c, wc, FA, p_FA, S, G, W, p_w, CaO, SO3, SiO2, Al2O3, Fe2O3, phi_clinker, S_max, f_cem, t_c, RH, T, CO2):
        self.name =name
        self.karbo =0

        M_co= 44.01          #MCO2 and MCaO (g/mol) are the molar weight of CO2 and CaO respectively
        M_CaO= 56.0774       #(g/mol)
        #phi_clinker in [-], C in [kg/m³ Beton], CaO in [-] 
        self.a=0.75* phi_clinker *C* CaO * M_co/M_CaO       #[kg/m^3] the amount of CO2 absorbed per volume of completely carbonated concrete
        S_max= float(S_max)      

        #S_max in [mm]
        if 8<= S_max < 16:
            po_air= 0.035-(0.035-0.023)/(16-8)*(S_max-8)          #[-]
        elif 16 <= S_max < 31.5:
            po_air= 0.023 -(0.023-0.015)/(31.5-16) *(S_max-16)    #[-]
        else:
            print('error S_max')
            self.karbo= float('NaN')
            return
        
        f_c= (7.84*f_cem)/(1+wc*p_c/p_w+po_air*p_c/C)**2 #[]????
        
        D_co28=10**(-7)*10**(-0.025*f_c)                 #[]???
        RH=RH/100            #[-]
        f_RH = (1-RH)**2 *RH**(2.6)                      #RH in [-] ???
        
    
        f_T = math.exp((4700*((T+273.15)-293))/(293*(T+273.15)))      #Arrhenius’ law: T in [C] wird in [K] umgewandelt
        f_SGC = ((S+G)/C)**(0.1)                        #[-] with S,G,C in [kg/m³ Beton]
        
        
        po= po_air + W/p_w - (0.249*(CaO-0.7* SO3) +0.191*SiO2 +1.118*Al2O3 - 0.357*Fe2O3)*C/1000     #po_carbon (n.u.) is the carbonated concrete porosity
        if 0.5< wc<0.8:
            n=1.8       #n (n.u.) is an empirical constant: n = 1.8 for 0.5 < W/C < 0.8. 
        else:
            print("wc error: empirical constant n not defined")
            self.karbo= float('NaN')
            return
        f_wc= 2437.7* math.exp(-5.592*wc)
        f_PwcFA = f_wc *( ( (0.93-3.95*0.94**(100*wc))*po -po_air ) / (W/p_w + C/p_c +FA/p_FA)  )**(n)
        
        f_tc= (1.9*10**(-2))/(10**(-0.025*f_c)) +(1- (1.9*10**(-2))/(10**(-0.025*f_c)))*math.sqrt(28/(0.01*t_c))
        
        #print(D_co28,f_RH, f_T,f_SGC,f_PwcFA,f_tc)
        self.D=D_co28 *f_RH * f_T * f_SGC *f_PwcFA *f_tc *365*24*60*60  #[m^2/year]=[m^2/s]**365*24*60*60 
        self.karbo = math.sqrt(2*self.D*CO2/self.a) * 1000 #[mm/year^0.5]
        
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