# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:11:10 2022

@author: Marco
"""
import streamlit as st
from dataclasses import dataclass
from CarboModels import Häkkinen

@dataclass
class app_Häkkinen():   #Modell01
    
    name:str
    
    def __post_init__(self):
        col1, col2  = st.columns([1,1])
        with col1:
            ExCo = st.radio("Choose location of the component:", ["Sheltered from rain", "Exposed to rain"])
            f_c = st.number_input("28-day compressive strenght: (MPa)", 0.5,None,25.0,step=(0.5))
            C = st.number_input("Clinker Content: (kg/m³)", value=(200.0), step=(0.5))
        with col2:
            AirEntrained = st.radio("Choose if component is air entrained:", ["Air entrained","Not air entrained"])
            optional = st.radio("Choose optional mixture:", ["None","Fly ash", "Silicia fume", "Blast furnance slag"])
            if optional == "None": FA = 0.0;  SF = 0.0; GGBS = 0.0
            if optional == "Fly ash": FA = st.number_input("Fly ash content: (kg/m³)", help="recommended value 28%", step=(0.5)); SF = 0.0; GGBS = 0.0
            if optional == "Silicia fume": SF = st.number_input("Silicia fume content: (kg/m³)", help="recommended value 9%", step=(0.5)); FA = 0.0; GGBS = 0.0
            if optional == "Blast furnance slag": GGBS = st.number_input("Blast furnance slag content: (kg/m³)", help="recommended value 70%", step=(0.5)); FA = 0.0; SF = 0.0
        t = st.number_input("Minimum lifetime (years): ", min_value=1,value=50)
       
        if st.button("Calculate"): 
            Modell01 = Häkkinen(self.name, C, f_c, ExCo, AirEntrained, FA, SF, GGBS)
            Modell01.calculate(t)