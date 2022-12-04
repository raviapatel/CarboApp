# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 21:27:30 2022

@author: marco
"""

import streamlit as st
from dataclasses import dataclass
from CarboModels import Häkkinen             #Modell01
from CarboModels import fib                  #Modell02.1
from CarboModels import fibGuiglia           #Modell02.2
from CarboModels import CECS220              #Modell03
from CarboModels import Guiglia              #Modell04
from CarboModels import Silva                #Modell05
from CarboModels import Yang                 #Modell06
from CarboModels import Hills_time           #Modell07.1
from CarboModels import Hills_fc             #Modell07.2
from CarboModels import fibGreveDierfeld     #Modell08
from CarboModels import Ta                   #Modell09
from CarboModels import Ekolu                #Modell10
from CarboModels import Possan               #Modell11

@dataclass
class CompareModels():
    
    def __post_init__(self):
        st.subheader("Choose Models to Compare:")
        compare = st.multiselect("Choose Models:", ("Model 01", "Model 02", "Model 03", "Model 04", "Model 05", "Model 06", "Model 07", "Model 08", "Model 09", "Model 10", "Model 11"), label_visibility="collapsed")
        col1, col2 = st.columns([1,1])
        if "Model 01" in compare or "Model 02" in compare or "Model 03" in compare or "Model 04" in compare or "Model 05" in compare or "Model 06" in compare or "Model 07" in compare or "Model 09" in compare or "Model 10" in compare or "Model 11" in compare: 
            with col1:
                f_c = st.number_input("f_c:")
                
        if "Model 02" in compare or "Model 03" in compare or "Model 04" in compare or "Model 05" in compare or "Model 06" in compare or "Model 08" in compare or "Model 09" in compare or "Model 10" in compare or "Model 11" in compare: 
            with col1:
                RH = st.number_input("RH:")
            
        if st.button("Calculate"):
            if "Model 01" in compare:
                Model01 = Häkkinen(name, C, f_c, exposed, entrained, FA, SF, GGBS)
                Model01.calculate(t)
            if "Model 02" in compare:
                Model02 = fib(name, RH, ToW, p_sr, t_c, R_NAC1, C_co2)
                Model02 = fibGuiglia(name, RH, ToW, p_sr, t_c, f_c, C_co2)
            if "Model 03" in compare:
                Model03 = CECS220(name, f_c, FA, stress, location, T, RH, CO2)
            if "Model 04" in compare:
                Model04 = Guiglia(name, f_c, RH, building)
            if "Model 05" in compare:
                Model05 = Silva(name, C, f_c, ExpC, RH, CO2)
            if "Model 06" in compare:
                Model06 = Yang(name, t, C, S, G, FA, GGBS, SF, wc, RH, C_co2, Location, Finishing)
            if "Model 07" in compare:
                Model07 = Hills_time(name, mixture, ExCo, origin, age)
                Model07 = Hills_fc(name, mixture, ExCo, f_c)
            if "Model 08" in compare:
                Model08 = fibGreveDierfeld(name, RH, CEM, C, FA, SF, GGBS, L, PZ, wb, CO2, ToW, p_dr, t_c)
            if "Model 09" in compare:
                Model09 = Ta(name, C, p_c, wc, FA, p_FA, S, G, W, p_w, CaO, SO3, SiO2, Al2O3, Fe2O3, phi_clinker, S_max, f_cem, t_c, RH, T, CO2)
            if "Model 10" in compare: 
                Model10 = Ekolu(name, f_c, RH, CO2, FA_c, GGBS_c, ExCo)
            if "Model 11" in compare:
                Model11 = Possan(name, C, FA, SF, CEM, f_c, ExCo, CO2, RH)
                