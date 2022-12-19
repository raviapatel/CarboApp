# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:22:18 2022

@author: Marco
"""
import streamlit as st
from dataclasses import dataclass
from CarboModels import Ta

@dataclass
class app_Ta(): #Model 09
    
    name:str
    
    def __post_init__(self):
        col1, col2  = st.columns([1,1])
        with col1:
            C = st.number_input("Clinker Content: (kg/m³)", value=(200.0), step=(0.5))
            FA = st.number_input("Fly Ash Content: (kg/m³)", value=(0.0), step=(0.5))
            W = st.number_input("Water Content: (kg/m³)", value=(0.0), step=(0.5))
            S = st.number_input("Sand Content: (kg/m³)", value=(0.0), step=(0.5))
            CaO = st.number_input("Amount of Calcium Oxide per Weight of Cement: (-)", value=(0.0), step=(0.5))
            SO3 = st.number_input("Amount of Sulfur Oxide per Weight of Cement: (-)", value=(0.0), step=(0.5))
            SiO2 = st.number_input("Amount of Silicon Oxide per Weight of Cement: (-)", value=(0.0), step=(0.5))
            Al2O3 = st.number_input("Amount of Aluminium Oxide per Weight of Cement: (-)", value=(0.0), step=(0.5))
            Fe2O3 = st.number_input("Amount of Iron Oxide per Weight of Cement: (-)", value=(0.0), step=(0.5))
            wc = st.number_input("Water / Cement Ratio: (-)", value=(0.0), step=(0.5))

        with col2:
            p_c = st.number_input("Density of Cement: (kg/m³)", value=(0.0), step=(0.5))
            p_FA = st.number_input("Density of Fly Ash: (kg/m³)", value=(0.0), step=(0.5))
            p_w = st.number_input("Density of Water: (kg/m³)", value=(0.0), step=(0.5))
            G = st.number_input("Gravel Content: (kg/m³)", value=(0.0), step=(0.5))
            phi_clinker = st.number_input("Cement Clinker Content: (-)", value=(0.0), step=(0.5))
            S_max = st.number_input("Maximum aggregate size: (mm)", value=(0.0), step=(0.5))
            f_cem = st.number_input("fcm ? : (MPa)", value=(0.0), step=(0.5))
            t_c = st.number_input("Curing Period: (days)", value=(0.0), step=(0.5))
            RH = st.number_input("Relative humidity: (%)", value=(0.0), step=(0.5))
            T = st.number_input("Temperature: (°C)", value=(0.0), step=(0.5))
            CO2 = st.number_input("CO2 Concentration: (-)", value=(0.0), step=(0.5))
        t = st.number_input("Minimum Lifetime: (years)", value=(0.0), step=(0.5))


        if st.button("Calculate "): 
            Modell09 = Ta(self.name, C, p_c, wc, FA, p_FA, S, G, W, p_w, CaO, SO3, SiO2, Al2O3, Fe2O3, phi_clinker, S_max, f_cem, t_c, RH, T, CO2)
            Modell09.calculate(t)

