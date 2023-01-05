# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:22:18 2022

@author: Marco
"""
import streamlit as st
from dataclasses import dataclass
from CarboModels import GreveDierfeld

@dataclass
class app_GreveDierfeld(): #Model 08
    
    name:str
    
    def __post_init__(self):
        col1, col2 = st.columns([1,1])
        with col1:
            RH = st.number_input("Mean Relative Air Humidity: [%]", min_value=(0.0), max_value=(100.0), value=(70.0), step=(0.5))
            wb = st.number_input("Water / Binder Ratio: [-]",min_value=(0.0), value=(0.5), max_value=(0.65),step=(0.01))
            t_c = st.number_input("Curing Time: [days]", min_value=(0), value=(3), step=(1))
            CO2 = st.number_input("CO2 Density around Concrete Surface: [%]", min_value=(0.0), max_value=(100.0), value=(0.04), step=(0.005), format=("%.4f"))

        with col2:
            Cem = st.radio("Choose CEM", ["CEM I", "CEM II/A", "CEM II/B", "CEM II/A", "CEM III/B"])
            ToW = st.number_input("Average Number of Rainy Days per Year [days]", min_value=(0.0), max_value=(365.0), value=(130.0))
            p_dr = st.number_input("Probability of Driving Rain: [%]", min_value=(0.0), max_value=(100.0), value=(30.0), step=(0.5))
                
        t = st.number_input("Service Time: [years]", min_value=(1), max_value=(100), value=(50), step=(1))
        
        if st.button("Calculate"):
            Modell08 = GreveDierfeld(self.name, RH, Cem, wb, CO2, ToW, p_dr, t_c)
            Modell08.calculate(t)

