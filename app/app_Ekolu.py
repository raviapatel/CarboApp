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
            ExCo = st.radio("Choose location of component:", ["Exposed", "Sheltered"])
            FA_c = st.number_input("Fly ash content: (weight ratio)", value=(0.0), max_value=(1.0))
            GGBS_c = st.number_input("Blast furnance slag content: (weight ratio)", value=(0.0), max_value=(1.0))

            
        with col2:
            f_c = st.number_input("28-day compressive strenght: (MPa)", min_value=(20.0), value=(25.0), step=(0.5))
            RH = st.number_input("Relative humidity around concrete surface: (%)", min_value=(50.0), value=(65.0), max_value=(80.0), step=(0.5))
            CO2 = st.number_input("CO2 density around concrete surface: (%)", value=(0.04), max_value=(0.2))


        t = st.number_input("Minimum lifetime (years): ", min_value=1,value=50)

        
        if st.button("Calculate "): 
            Modell10 = Ekolu(self.name, f_c, RH, CO2, FA_c, GGBS_c, ExCo)
            Modell10.calculate(t) 
