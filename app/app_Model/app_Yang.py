# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:22:18 2022

@author: Marco
"""
import streamlit as st
from dataclasses import dataclass
from CarboModels import Yang

@dataclass
class app_Yang():   #Model 06
    
    name:str
    
    def __post_init__(self):
        col1, col2 = st.columns([1,1])
        with col1:
            C = st.number_input("Clinker Content: [kg/m³]", min_value=(0.0), value=(350.0), step=(5.0))
            S = st.number_input("Sand Content: [kg/m³]", min_value=(0.0), value=(1000.0), step=(5.0))
            G = st.number_input("Gravel Content: [kg/m³]", min_value=(0.0), value=(800.0), step=(5.0))
            FA = st.number_input("Fly Ash Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0))
            GGBS = st.number_input("Blast Furnance Slag Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0))
            SF = st.number_input("Silicia Fume Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0))

        with col2:
            RH = st.number_input("Mean Relative Air Humidity: [%]", min_value=(0.0), max_value=(100.0), value=(70.0), step=(0.5))
            wc = st.number_input("Water / Cement Ratio: [-]", min_value=(0.0), value=(0.6), max_value=(1.0), step=(0.01))
            CO2 = st.number_input("CO2 Density around Concrete Surface: [%]", min_value=(0.0), max_value=(100.0), value=(0.04), step=(0.005), format=("%.4f"))

            ExCo = st.radio("Choose Exposure Condition of component:", ["Indoor", "Outdoor"])
            if ExCo =="Outdoor":     Finishing = st.radio("Choose Finishing of Component:", ["Nothing", "Plaster", "Paint", "Mortar", "Mortar + Plaster", "Mortar + Paint", "Tile"])
            elif ExCo =="Indoor":    Finishing = st.radio("Choose Finishing of Component:", ["Nothing", "Paint", "Mortar", "Tile"])

        t = st.number_input("Service Time: [years]", min_value=(1), value=(50), step=(1))
        
        if st.button("Calculate"): 
            Modell06 = Yang(self.name, t, C, S, G, FA, GGBS, SF, wc, RH, CO2, ExCo, Finishing)
            Modell06.calculate(t)
