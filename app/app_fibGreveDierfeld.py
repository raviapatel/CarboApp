# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:22:18 2022

@author: Marco
"""
import streamlit as st
from dataclasses import dataclass
from CarboModels import fibGreveDierfeld

@dataclass
class app_fibGreveDierfeld(): #Model 08
    
    name:str
    
    def __post_init__(self):
        col1, col2 = st.columns([1,1])
        with col1:
            RH = st.number_input("Relative humidity: (%)", 1.0,100.0,50.0, step=0.5) 
            wb = st.number_input("wb: (kg/m³)",0.0,None,25.0,step=(0.5))
            ToW = st.slider("ToW: (years) ", 1,100,50)
            p_dr = st.number_input("p_dr: (kg/m³)",0.0,None,25.0,step=(0.5))
            t_c = st.number_input("t_c: (kg/m³)",0.0,None,25.0,step=(0.5))            
            CO2 = st.number_input("CO2 density around concrete surface: (%)",0.0,None,25.0,step=(0.5))

            
        with col2:
            CEM = st.radio("Choose CEM", ["?","CEM I"])
            if CEM == "?":
                C = st.number_input("Clinker Content: (kg/m³)", value=(200.0), step=(0.5))
                FA = st.number_input("Fly ash content: (weight ratio)", value=(0.0))
                SF = st.number_input("Silica fume content: (kg/m³)",0.0,None,25.0,step=(0.5))
                GGBS = st.number_input("Ground granulated blast furnace slag content: (kg/m³)",0.0,None,25.0,step=(0.5))
                L = st.number_input("L: (kg/m³)",0.0,None,25.0,step=(0.5))
                PZ = st.number_input("PZ: (kg/m³)",0.0,None,25.0,step=(0.5))
            else:
                C=0;FA=0;SF=0;GGBS=0;L=0;PZ=0
                
        t = st.number_input("Minimum lifetime (years): ", min_value=1,value=50)
        if st.button("Calculate"):
            Modell08 = fibGreveDierfeld(self.name, RH, CEM, C, FA, SF, GGBS, L, PZ, wb, CO2, ToW, p_dr, t_c)
            Modell08.calculate(t)

