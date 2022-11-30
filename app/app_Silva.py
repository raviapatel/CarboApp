# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:22:18 2022

@author: Marco
"""
import streamlit as st
from dataclasses import dataclass
from CarboModels import Silva

@dataclass
class app_Silva():
    
    name:str
    
    def __post_init__(self):
        col1, col2 = st.columns([1,1])
        with col1:
            rh = st.number_input("Relative humidity: (%)", 1,100,65)    
            ExpC = st.selectbox("Exposure class:", ("XC1","XC2","XC3","XC4")) 
        with col2:
            f_c = st.number_input("28-day compressive strenght (MPa)",0.5,None,25.0,step=(0.5))
        with col1: CO2 = st.number_input("CO2 density around concrete surface: (%)",0.0,None,0.04,step=(0.01))
        with col2: C = st.number_input("C: (kg/m³)",0.0,None,220.0,step=(0.5))
        t = st.number_input("Minimum lifetime (years): ", min_value=1,value=50)
       
        if st.button("Calculate "): 
            Modell05 = Silva(self.name, C, f_c, ExpC, rh, CO2) #(name, C, f_c, phi_clinker, ExpC, RH, CO2))(name, 0.5, 25, 0.5, 0.5, rh, 0.05)
            Modell05.calculate(t)
