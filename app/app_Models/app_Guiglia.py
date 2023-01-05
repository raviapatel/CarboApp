# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:22:18 2022

@author: Marco
"""
import streamlit as st
from dataclasses import dataclass
from CarboModels import Guiglia

@dataclass
class app_Guiglia():
    
    name:str
    
    def __post_init__(self):
        col1, col2 = st.columns([1,1])
        with col1: 
            f_c = st.number_input("Mean Concrete Compressive Strenght: [MPa]", min_value=(1.0), max_value=(100.0), value=(30.0), step=(0.5))
            RH = st.number_input("Mean Relative Air Humidity: [%]", min_value=(0.0), max_value=(100.0), value=(70.0), step=(0.5))
        with col2:
            Building = st.radio("Building type:", ("Tunnel","Others"))
        t = st.number_input("Service Time: [years]", min_value=(1), value=(50), step=(1))

        if st.button("Calculate"): 
            Modell04 = Guiglia(self.name, f_c, RH, Building)
            Modell04.calculate(t)
