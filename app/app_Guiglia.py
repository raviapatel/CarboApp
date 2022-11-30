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
            building = st.selectbox("Building type:", ("Tunnel","others"))
            rh = st.number_input("Relative humidity around concrete surface: (%)", 1,100,65)    
        with col2:
            fc = st.number_input("Concrete compressive strength fcm: (N/mm²)",0.5,None,25.0,step=(0.5))
           
        t = st.number_input("Minimum lifetime (years): ", min_value=1,value=50)

        if st.button("Calculate "): 
            Modell04 = Guiglia(self.name, fc, rh, building) #(name, C, f_c, phi_clinker, ExpC, RH, CO2))(name, 0.5, 25, 0.5, 0.5, rh, 0.05)
            Modell04.calculate(t)
