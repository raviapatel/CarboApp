# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:22:18 2022

@author: Marco
"""
import streamlit as st
from dataclasses import dataclass
from CarboModels.Ta import Ta

@dataclass
class app_Ta(): #Model 09
    
    name:str
    
    def __post_init__(self):
        col1, col2  = st.columns([1,1])
        with col1:
            C = st.number_input("Clinker Content: [kg/m³]", min_value=(0.0), value=(350.0), step=(5.0))
            FA = st.number_input("Fly Ash Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0))
            W = st.number_input("Water Content: [kg/m³]", min_value=(0.0), value=(280.0), step=(5.0))
            S = st.number_input("Sand Content: [kg/m³]", min_value=(0.0), value=(1000.0), step=(5.0))
            CaO = st.number_input("Amount of Calcium Oxide per Weight of Cement: [-]", min_value=(0.0), max_value=(1.0), value=(0.645), step=(0.01), format=("%.4f"))
            SO3 = st.number_input("Amount of Sulfur Oxide per Weight of Cement: [-]", min_value=(0.0), max_value=(1.0), value=(0.035), step=(0.01), format=("%.4f"))
            SiO2 = st.number_input("Amount of Silicon Oxide per Weight of Cement: [-]", min_value=(0.0), max_value=(1.0), value=(0.205), step=(0.01), format=("%.4f"))
            Al2O3 = st.number_input("Amount of Aluminium Oxide per Weight of Cement: [-]", min_value=(0.0), max_value=(1.0), value=(0.045), step=(0.01), format=("%.4f"))
            Fe2O3 = st.number_input("Amount of Iron Oxide per Weight of Cement: [-]", min_value=(0.0), max_value=(1.0), value=(0.030), step=(0.01), format=("%.4f"))
            wb = st.number_input("Water / Binder Ratio: [-]", min_value=(0.51), value=(0.6), max_value=(0.79), step=(0.01))

        with col2:
            p_c = st.number_input("Density of Cement: [kg/m³]", value=(3140.0), min_value=(0.0), step=(0.5))
            p_FA = st.number_input("Density of Fly Ash: [kg/m³]", value=(2580.0), min_value=(0.0), step=(0.5))
            p_w = st.number_input("Density of Water: [kg/m³]", value=(1000.0), min_value=(0.0), step=(0.5))
            G = st.number_input("Gravel Content: [kg/m³]", min_value=(0.0), value=(800.0), step=(5.0))
            phi_clinker = st.number_input("Cement Clinker Content: [-]",min_value=(0.0), value=(1.0), max_value=(1.0), step=(0.01))
            S_max = st.number_input("Maximum Aggregate Size: [mm]", min_value=(8.0), value=(16.0), max_value=(31.5), step=(0.5))
            f_cem = st.number_input("Mean Cement Compressive Strenght: [N/mm²]",  min_value=(0.0), value=(42.5), max_value=(60.0), step=(0.5))
            t_c = st.number_input("Curing Time: [days]", min_value=(0), value=(3), step=(1))
            RH = st.number_input("Mean Relative Air Humidity: [%]", min_value=(0.0), max_value=(100.0), value=(70.0), step=(0.5))
            T = st.number_input("Mean Temperature: [°C]", value=(15.0), step=(0.5))
            CO2 = st.number_input("CO2 Density around Concrete Surface: [%]", min_value=(0.0), max_value=(100.0), value=(0.04), step=(0.005), format=("%.4f"))
        t = st.number_input("Service Time: [years]", min_value=(1), value=(50), step=(1))


        if st.button("Calculate "): 
            Modell09 = Ta(self.name, C, p_c, wb, FA, p_FA, S, G, W, p_w, CaO, SO3, SiO2, Al2O3, Fe2O3, phi_clinker, S_max, f_cem, t_c, RH, T, CO2)
            Modell09.calculate(t)

