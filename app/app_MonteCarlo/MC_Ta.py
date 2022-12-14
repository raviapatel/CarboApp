# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:24:42 2022

@author: Marco
"""

import streamlit as st
import numpy as np
from scipy.stats import beta
from dataclasses import dataclass
from CarboModels.Ta import Ta

@dataclass
class MC_Ta(): #Model 09

    def __post_init__(self):
        col1, col2  = st.columns([1,1])
        with col1:
            C = st.number_input("Clinker Content: [kg/m³]", min_value=(0.0), value=(350.0), step=(5.0), key="MC_Ta_01")
            FA = st.number_input("Fly Ash Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0), key="MC_Ta_02")
            W = st.number_input("Water Content: [kg/m³]", min_value=(0.0), value=(280.0), step=(5.0), key="MC_Ta_03")
            S = st.number_input("Sand Content: [kg/m³]", min_value=(0.0), value=(1000.0), step=(5.0), key="MC_Ta_04")
            CaO = st.number_input("Amount of Calcium Oxide per Weight of Cement: [-]", min_value=(0.0), max_value=(1.0), value=(0.645), step=(0.01), format=("%.4f"), key="MC_Ta_05")
            SO3 = st.number_input("Amount of Sulfur Oxide per Weight of Cement: [-]", min_value=(0.0), max_value=(1.0), value=(0.035), step=(0.01), format=("%.4f"), key="MC_Ta_06")
            SiO2 = st.number_input("Amount of Silicon Oxide per Weight of Cement: [-]", min_value=(0.0), max_value=(1.0), value=(0.205), step=(0.01), format=("%.4f"), key="MC_Ta_07")
            Al2O3 = st.number_input("Amount of Aluminium Oxide per Weight of Cement: [-]", min_value=(0.0), max_value=(1.0), value=(0.045), step=(0.01), format=("%.4f"), key="MC_Ta_08")
            Fe2O3 = st.number_input("Amount of Iron Oxide per Weight of Cement: [-]", min_value=(0.0), max_value=(1.0), value=(0.030), step=(0.01), format=("%.4f"), key="MC_Ta_09")
            wb = st.number_input("Water / Binder Ratio: [-]", min_value=(0.51), value=(0.6), max_value=(0.79), step=(0.01), key="MC_Ta_10")

        with col2:
            p_c = st.number_input("Density of Cement: [kg/m³]", value=(3140.0), min_value=(0.0), step=(0.5), key="MC_Ta_11")
            p_FA = st.number_input("Density of Fly Ash: [kg/m³]", value=(2580.0), min_value=(0.0), step=(0.5), key="MC_Ta_12")
            p_w = st.number_input("Density of Water: [kg/m³]", value=(1000.0), min_value=(0.0), step=(0.5), key="MC_Ta_13")
            G = st.number_input("Gravel Content: [kg/m³]", min_value=(0.0), value=(800.0), step=(5.0), key="MC_Ta_14")
            phi_clinker = st.number_input("Cement Clinker Content: [-]",min_value=(0.0), value=(1.0), max_value=(1.0), step=(0.01), key="MC_Ta_15")
            S_max = st.number_input("Maximum Aggregate Size: [mm]", min_value=(8.0), value=(16.0), max_value=(31.5), step=(0.5), key="MC_Ta_16")
            f_cem = st.number_input("Mean Cement Compressive Strenght: [N/mm²]",  min_value=(0.0), value=(42.5), max_value=(60.0), step=(0.5), key="MC_Ta_17")
            t_c = st.number_input("Curing Time: [days]", min_value=(0), value=(3), step=(1), key="MC_Ta_18")
            RH = st.number_input("Mean Relative Air Humidity: [%]", min_value=(2.0), max_value=(98.0), value=(70.0), step=(0.5), key="MC_Yang_07")
            T = st.number_input("Mean Temperature: [°C]", value=(15.0), step=(0.5), key="MC_Ta_20")
            CO2 = st.number_input("CO2 Density around Concrete Surface: [%]", min_value=(0.0), max_value=(100.0), value=(0.04), step=(0.005), format=("%.4f"), key="MC_Ta_21")
        t = st.number_input("Service Time: [years]", min_value=(1), value=(50), step=(1), key="MC_Ta_22")
        c_nom = st.number_input("Concrete Cover: [mm]",  min_value=(0.0), value=(20.0), step=(0.5), key="MC_Ta_23")
        sample_total = st.number_input("Total of Samples: [-]", min_value=(1), value=(1000), step=(100), key="MC_Ta_24")

        if st.button("Calculate", key="MC_Ta_25"): 
            # Distribution of CO2 (Normal):
            CO2 = 0.0409*CO2*44.01/100                          # [%]->[kg/m³]
            CO2_p=np.random.normal(CO2, 0.0001, sample_total)   # [kg/m³]
            CO2_p=(100*CO2_p)/(44.01*0.0409)                    # [kg/m³]->[%]
            # Distribution of RH (Beta):
            m=RH; s=12.9; a=0; b=100; var=s**2                      #m=Mittelwert, s=Standardabweichung, a=Min, b=Max, var=Varianz
            alpha_input = ((a-m)*(a*b-a*m-b*m+m**2+var))/(var*(b-a))
            beta_input = -((b-m)*(a*b-a*m-b*m+m**2+var))/(var*(b-a))
            RH_p = beta.rvs(alpha_input, beta_input, scale=b-a, loc=a, size=sample_total)
                
            X=[]
            bar=st.progress(0)
            for i in range(0,sample_total):
                bar.progress((1+i)/sample_total)
                Calc_MC = Ta(i, C, p_c, wb, FA, p_FA, S, G, W, p_w, CaO, SO3, SiO2, Al2O3, Fe2O3, phi_clinker, S_max, f_cem, t_c, RH_p[i], T, CO2_p[i])
                X.append(Calc_MC)
            Calc_MC.histogram(X, t, c_nom, sample_total)

