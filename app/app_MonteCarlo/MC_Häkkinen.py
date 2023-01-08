# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:22:25 2022

@author: Marco
"""
import streamlit as st
import numpy as np
from dataclasses import dataclass
from CarboModels.Häkkinen import Häkkinen

@dataclass
class MC_Häkkinen():
    
    def __post_init__(self):
        col1, col2  = st.columns([1,1])
        with col1:
            ExCo = st.radio("Choose Exposure Condition of Component:", ["Sheltered from Rain", "Exposed to Rain"], key="MC_Häkkinen_01")
            f_c = st.number_input("Mean Concrete Compressive Strenght: [MPa]", min_value=(1.0), max_value=(100.0), value=(30.0), step=(0.5), key="MC_Häkkinen_02")
            C = st.number_input("Clinker Content: [kg/m³]", min_value=(0.0), value=(350.0), step=(5.0), key="MC_Häkkinen_03")
        with col2:
            AirEntrained = st.radio("Choose if Component is Air Entrained:", ["Air Entrained","Not Air Entrained"], key="MC_Häkkinen_04")
            optional = st.radio("Choose optional mixture:", ["None","Fly ash", "Silicia fume", "Blast furnance slag"], key="MC_Häkkinen_05")
            if optional == "None": 
                FA = 0.0;  SF = 0.0; GGBS = 0.0
            if optional == "Fly ash": 
                FA = st.number_input("Fly Ash Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0), help=("Recommended Value: 28% of Binder Content"), key="MC_Häkkinen_06"); SF = 0.0; GGBS = 0.0
            if optional == "Silicia fume": 
                SF = st.number_input("Silicia Fume Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0), help=("Recommended Value: 9% of Binder Content"), key="MC_Häkkinen_07"); FA = 0.0; GGBS = 0.0
            if optional == "Blast furnance slag": 
                GGBS = st.number_input("Blast Furnance Slag Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0), help=("Recommended Value: 70% of Binder Content"), key="MC_Häkkinen_08"); FA = 0.0; SF = 0.0
        t = st.number_input("Service Time: [years]", min_value=(1), value=(50), step=(1), key="MC_Häkkinen_09")
        c_nom = st.number_input("Concrete Cover: [mm]",  min_value=(0.0), value=(20.0), step=(0.5), key="MC_Häkkinen_10")
        sample_total = st.number_input("Total of Samples: [-]", min_value=(1), value=(1000), step=(100), key="MC_Häkkinen_11")

        if st.button("Calculate", key="MC_Häkkinen_12"): 
            X=[]
            bar=st.progress(0)
            for i in range(0,sample_total):
                bar.progress((1+i)/sample_total)
                Calc_MC = Häkkinen(i, f_c, ExCo, AirEntrained, C, FA, SF, GGBS)
                X.append(Calc_MC)
            Calc_MC.histogram(X, t, c_nom, sample_total)
