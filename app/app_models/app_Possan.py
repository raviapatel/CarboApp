# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:22:18 2022

@author: Marco
"""
import streamlit as st
from dataclasses import dataclass
from CarboModels.Possan import Possan

@dataclass
class app_Possan(): #Model 11
    
    name:str
    
    def __post_init__(self):
        col1, col2  = st.columns([1,1])
        with col1:
            f_c = st.number_input("Mean Concrete Compressive Strenght: [MPa]", min_value=(1.0), max_value=(100.0), value=(30.0), step=(0.5))
            C = st.number_input("Clinker Content: [kg/m³]", min_value=(0.0), value=(350.0), step=(5.0))
            FA = st.number_input("Fly Ash Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0))
            SF = st.number_input("Silicia Fume Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0))

        with col2:
            ExCo = st.radio("Choose Exposure Condition of component:", ["Exposed to Rain", "Sheltered from Rain", "Indoor"])
            Cem = st.radio("Choose Cement type:", ["CEM I", "CEM II/A-L", "CEM II/A-S", "CEM II/B-S", "CEM III/A", "CEM IV/A", "CEM IV/B"])
            CO2 = st.number_input("CO2 Density around Concrete Surface: [%]", min_value=(0.0), max_value=(100.0), value=(0.04), step=(0.005), format=("%.4f"))
            RH = st.number_input("Mean Relative Air Humidity: [%]", min_value=(0.0), max_value=(100.0), value=(70.0), step=(0.5))

        t = st.number_input("Service Time: [years]", min_value=(1), value=(50), step=(1))

        if st.button("Calculate"):
            Modell11 = Possan(self.name, C, FA, SF, Cem, f_c, ExCo, CO2, RH)
            Modell11.calculate(t)
