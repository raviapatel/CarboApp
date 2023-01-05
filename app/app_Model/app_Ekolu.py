# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:22:18 2022

@author: Marco
"""
import streamlit as st
from dataclasses import dataclass
from CarboModels import Ekolu

@dataclass
class app_Ekolu():  #Model 10
    
    name:str
    
    def __post_init__(self):
        col1, col2  = st.columns([1,1])
        with col1:
            ExCo = st.radio("Choose Exposure Condition of Component:", ["Exposed to Rain", "Sheltered from Rain"])
            Cem = st.radio("Choose Cement Type:", ["CEM I", "CEM II/A", "CEM II/B", "CEM IV/A", "CEM III/A", "CEM IV/B"])
            
        with col2:
            f_c = st.number_input("Mean Concrete Compressive Strenght: [MPa]", min_value=(20.1), value=(30.0), step=(0.5))
            RH = st.number_input("Mean Relative Air Humidity: [%]", min_value=(50.0), max_value=(80.0), value=(70.0), step=(0.5))
            CO2 = st.number_input("CO2 Density around Concrete Surface: [%]", min_value=(0.0), max_value=(0.2), value=(0.04), step=(0.005), format=("%.4f"))


        t = st.number_input("Service Time: [years]", min_value=(1), max_value=(100), value=(50), step=(1))

        
        if st.button("Calculate"): 
            Modell10 = Ekolu(self.name, f_c, RH, CO2, Cem, ExCo, t)
            Modell10.calculate(t) 
