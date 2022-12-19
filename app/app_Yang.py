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
            C = st.number_input("Cement content: (kg/m³)",0.0,None,300.0,step=(0.5))
            S = st.number_input("Sand content: (kg/m³)",0.0,None,400.0,step=(10.0))
            G = st.number_input("Gravel content: (kg/m³)",0.0,None,1000.0,step=(10.0))
            FA = st.number_input("Fly ash content: (kg/m³)",0.0,None,0.0,step=(0.5))
            GGBS = st.number_input("Ground granulated blast furnace slag content: (kg/m³)",0.0,None,0.0,step=(0.5))
            SF = st.number_input("Silica fume content: (kg/m³)",0.0,None,0.0,step=(0.5))

        with col2:
            RH = st.number_input("Relative humidity: (%)", 1.0,100.0,50.0, step=0.5) 
            wc = st.number_input("Water / cement ratio: (-)",0.0,None,0.6,step=(0.05))
            CO2 = st.number_input("CO2 density around concrete surface: (%)",0.0,None,0.040,step=(0.005))

            ExCo = st.radio("Choose location of component:", ["Outdoor","Indoor"])
            if ExCo =="Outdoor":     Finishing = st.radio("Choose Finishing of component:", ["Nothing", "Plaster", "Paint", "Mortar", "Mortar + Plaster", "Mortar + Paint", "Tile"])
            elif ExCo =="Indoor":    Finishing = st.radio("Choose Finishing of component:", ["Nothing", "Paint", "Mortar", "Tile"])

        t = st.number_input("Minimum lifetime (years): ", min_value=1,value=50)
        
        if st.button("Calculate"): 
            Modell06 = Yang(self.name, t, C, S, G, FA, GGBS, SF, wc, RH, CO2, ExCo, Finishing)
            Modell06.calculate(t)
