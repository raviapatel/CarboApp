# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:22:18 2022

@author: Marco
"""
import streamlit as st
from dataclasses import dataclass
from CarboModels import fib
from CarboModels import fibGuiglia

@dataclass
class app_fib():
    
    name:str
    
    def __post_init__(self):
        col1, col2 = st.columns([1,1])
        with col1: 
            RH = st.number_input("Relative Humidity: (%)", value=(65.0))
            C_co2 = st.number_input("Peripheral Concentration by Weight of CO2", value=(10.0))
            t_c = st.number_input("Curing time: (days)", value=(5.0))
            p_sr = st.number_input("Probability of Driving Rain: (-)")

        with col2: 
            ToW = st.number_input("Time of wettness: (days)")
            choose = st.radio(" Choose",["Set E_NAC1", "Calculalte with f_c"])
            
            if choose == "Set E_NAC1":
                R_NAC1 = st.number_input("R_NAC1")
            else:
                f_c = st.number_input("f_c")
        t = st.number_input("Minimum lifetime: (years)")
        if choose == "Set E_NAC1":
            if st.button("Calculate"): 
                Modell02 = fib(self.name, RH, ToW, p_sr, t_c, R_NAC1, C_co2)
                Modell02.calculate(t)
        else:
            if st.button("Calculate"):
                Modell02 = fibGuiglia(self.name, RH, ToW, p_sr, t_c, f_c, C_co2)
                Modell02.calculate(t)