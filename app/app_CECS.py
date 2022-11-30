# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:22:18 2022

@author: Marco
"""
import streamlit as st
from dataclasses import dataclass
from CarboModels import CECS220

@dataclass
class app_CECS():
    
    name:str
    
    def __post_init__(self):
        col1, col2 = st.columns([1,1])
        with col1:
            tension = st.radio("Stress on component:", ["pressure", "tension"])
            f_c = st.number_input("28-day compressive strenght: (MPa)", 0.5,None,25.0,step=(0.5))
            T = st.number_input("Temperature: (°C)", value=(15.0))
            RH = st.number_input("Relative humidity around concrete surface: (%)", value=(65.0))
        with col2:
            location = st.radio("Location of component:", ["corner", "other area"])
            FA = st.number_input("Fly ash content: (weight ratio)", value=(0.0))
            CO2 = st.number_input("CO2 density around concrete surface: (%)", value=(0.04))
        t = st.number_input("Minimum lifetime (years): ", min_value=1,value=50)
      
        if st.button("Calculate"): 
            Modell03 = CECS220(self.name, f_c, FA, tension, location, T, RH, CO2) 
            Modell03.calculate(t)
