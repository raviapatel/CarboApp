# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:22:18 2022

@author: Marco
"""
import streamlit as st
from dataclasses import dataclass
from CarboModels.fib import fib
from CarboModels.fibGuiglia import fibGuiglia

@dataclass
class app_fib():
    
    name:str
    
    def __post_init__(self):
        col1, col2 = st.columns([1,1])
        with col1: 
            RH = st.number_input("Mean Relative Air Humidity: [%]", min_value=(0.0), max_value=(100.0), value=(70.0), step=(0.5))
            CO2 = st.number_input("CO2 Density around Concrete Surface: [%]", min_value=(0.0), max_value=(100.0), value=(0.04), step=(0.005), format=("%.4f"))
            t_c = st.number_input("Curing Time: [days]", min_value=(0), value=(3), step=(1))
            p_dr = st.number_input("Probability of Driving Rain: [%]", min_value=(0.0), max_value=(100.0), value=(30.0), step=(0.5))

        with col2: 
            ToW = st.number_input("Average Number of Rainy Days per Year [days]", min_value=(0.0), max_value=(365.0), value=(130.0))
            choose_y = st.radio("Choose:",["Calculate with Safety Factors", "Calculalte without Safety Factors"])
            if choose_y == "Calculate with Safety Factors": 
                yR = 1.5; yRH = 1.3
            else:
                yR = 1.0; yRH = 1.0
            choose_R = st.radio("Choose:",["Set Inverse Effective Carbonation Resistance", "Calculalte with Compressive Strenght"])
            if choose_R == "Set Inverse Effective Carbonation Resistance":
                R_NAC = st.number_input("Inverse Effective Carbonation Resistance (NAC): [(mm²/year)/(kg/m³)]", min_value=(0.0), value=(8000.0), step=(5.0))
            else:
                f_c = st.number_input("Mean Concrete Compressive Strenght: [MPa]", min_value=(1.0), max_value=(100.0), value=(30.0), step=(0.5))
        
        t = st.number_input("Service Time: [years]", min_value=(1), max_value=(100), value=(50), step=(1))
        
        if choose_R == "Set Inverse Effective Carbonation Resistance":
            if st.button("Calculate"): 
                Modell02 = fib(self.name, RH, ToW, p_dr, t_c, R_NAC, CO2, t, yR, yRH)
                Modell02.calculate(t)
        else:
            if st.button("Calculate"):
                Modell02 = fibGuiglia(self.name, RH, ToW, p_dr, t_c, f_c, CO2, t, yR, yRH)
                Modell02.calculate(t)