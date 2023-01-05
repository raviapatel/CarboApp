# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:22:18 2022

@author: Marco
"""
import streamlit as st
from dataclasses import dataclass
from CarboModels import CECS220

@dataclass
class app_CECS():   #Model 03
    
    name:str
    
    def __post_init__(self):
        col1, col2 = st.columns([1,1])
        with col1:
            Stress = st.radio("Choose Stress on Component:", ["Pressure", "Tension"])
            f_c = st.number_input("Mean Concrete Compressive Strenght: [MPa]", min_value=(1.0), max_value=(100.0), value=(30.0), step=(0.5))
            T = st.number_input("Mean Temperature: [°C]", value=(15.0), step=(0.5))
            RH = st.number_input("Mean Relative Air Humidity: [%]", min_value=(0.0), max_value=(100.0), value=(70.0), step=(0.5))
        with col2:
            Location = st.radio("Choose Location of Component:", ["Corner", "Other Area"])
            FA_c = st.number_input("Fly Ash Content: [weight ratio]", min_value=(0.0), value=(0.0), max_value=(1.0), step=(0.01))
            CO2 = st.number_input("CO2 Density around Concrete Surface: [%]", min_value=(0.0), max_value=(100.0), value=(0.04), step=(0.005), format=("%.4f"))
        t = st.number_input("Service Time: [years]", min_value=(1), max_value=(100), value=(50), step=(1))
      
        if st.button("Calculate"): 
            Modell03 = CECS220(self.name, f_c, FA_c, Stress, Location, T, RH, CO2) 
            Modell03.calculate(t)
