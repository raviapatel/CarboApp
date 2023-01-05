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
            ExCo = st.radio("Choose Exposure Condition of Component:", ["Sheltered from Rain", "Exposed to Rain"])
            f_c = st.number_input("Mean Concrete Compressive Strenght: [MPa]", min_value=(1.0), max_value=(100.0), value=(30.0), step=(0.5))
            C = st.number_input("Clinker Content: [kg/m³]", min_value=(0.0), value=(350.0), step=(5.0))
        with col2:
            AirEntrained = st.radio("Choose if Component is Air Entrained:", ["Air Entrained","Not Air Entrained"])
            optional = st.radio("Choose optional mixture:", ["None","Fly ash", "Silicia fume", "Blast furnance slag"])
            if optional == "None": 
                FA = 0.0;  SF = 0.0; GGBS = 0.0
            if optional == "Fly ash": 
                FA = st.number_input("Fly Ash Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0), help=("Recommended Value: 28% of Binder Content")); SF = 0.0; GGBS = 0.0
            if optional == "Silicia fume": 
                SF = st.number_input("Silicia Fume Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0), help=("Recommended Value: 9% of Binder Content")); FA = 0.0; GGBS = 0.0
            if optional == "Blast furnance slag": 
                GGBS = st.number_input("Blast Furnance Slag Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0), help=("Recommended Value: 70% of Binder Content")); FA = 0.0; SF = 0.0
        t = st.number_input("Service Time: [years]", min_value=(1), value=(50), step=(1))
       
        if st.button("Calculate"): 
            Modell01 = Häkkinen(self.name, f_c, ExCo, AirEntrained, C, FA, SF, GGBS)
            Modell01.calculate(t)