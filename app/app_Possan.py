# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:22:18 2022

@author: Marco
"""
import streamlit as st
from dataclasses import dataclass
from CarboModels import Possan

@dataclass
class app_Possan():
    
    name:str
    
    def __post_init__(self):
        col1, col2  = st.columns([1,1])
        with col1:
            f_c = st.number_input("28-day compressive strenght: (MPa)", min_value=(20.0), value=(25.0), step=(0.5))

            C = st.number_input("C: (weight ratio)", value=(0.0), max_value=(1.0))
            FA = st.number_input("Fly ash content: (weight ratio)", value=(0.0), max_value=(1.0))
            SF = st.number_input("SF: (weight ratio)", value=(0.0), max_value=(1.0))

        with col2:
            ExCo = st.radio("Choose location of component:", ["Exposed", "Sheltered"])
            CEM = st.radio("Choose Cement type:", ["Unknown", "CEM I", "CEM II/A-L", "CEM II/A-S", "CEM II/B-S", "CEM III/A", "CEM IV/A", "CEM IV/B"])
            CO2 = st.number_input("CO2 density around concrete surface: (%)", value=(0.04))
            RH = st.number_input("Relative humidity around concrete surface: (%)", min_value=(50.0), value=(65.0), max_value=(80.0), step=(0.5))

        t = st.number_input("Minimum lifetime (years): ", min_value=1, value=50)

        if st.button("Calculate"):
            Modell11 = Possan(self.name, C, FA, SF, CEM, f_c, ExCo, CO2, RH)
            Modell11.calculate(t)
