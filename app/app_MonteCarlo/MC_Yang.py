# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:29:03 2022

@author: Marco
"""
import streamlit as st
import numpy as np
from scipy.stats import beta
from dataclasses import dataclass
from CarboModels.Yang import Yang

@dataclass
class MC_Yang():   #Model 06

    def __post_init__(self):
        col1, col2 = st.columns([1,1])
        with col1:
            C = st.number_input("Clinker Content: [kg/m³]", min_value=(0.0), value=(350.0), step=(5.0), key="MC_Yang_01")
            S = st.number_input("Sand Content: [kg/m³]", min_value=(0.0), value=(1000.0), step=(5.0), key="MC_Yang_02")
            G = st.number_input("Gravel Content: [kg/m³]", min_value=(0.0), value=(800.0), step=(5.0), key="MC_Yang_03")
            FA = st.number_input("Fly Ash Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0), key="MC_Yang_04")
            GGBS = st.number_input("Blast Furnance Slag Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0), key="MC_Yang_05")
            SF = st.number_input("Silicia Fume Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0), key="MC_Yang_06")

        with col2:
            RH = st.number_input("Mean Relative Air Humidity: [%]", min_value=(2.0), max_value=(98.0), value=(70.0), step=(0.5), key="MC_Yang_07")
            wb = st.number_input("Water / Binder Ratio: [-]", min_value=(0.0), value=(0.6), max_value=(1.0), step=(0.01), key="MC_Yang_08")
            CO2 = st.number_input("CO2 Density around Concrete Surface: [%]", min_value=(0.0), max_value=(100.0), value=(0.04), step=(0.005), format=("%.4f"), key="MC_Yang_09")
            ExCo = st.radio("Choose Exposure Condition of component:", ["Indoor", "Outdoor"], key="MC_Yang_10")
            if ExCo =="Outdoor":     Finishing = st.radio("Choose Finishing of Component:", ["Nothing", "Plaster", "Paint", "Mortar", "Mortar + Plaster", "Mortar + Paint", "Tile"], key="MC_Yang_11")
            elif ExCo =="Indoor":    Finishing = st.radio("Choose Finishing of Component:", ["Nothing", "Paint", "Mortar", "Tile"], key="MC_Yang_12")

        t = st.number_input("Service Time: [years]", min_value=(1), value=(50), step=(1), key="MC_Yang_13")
        c_nom = st.number_input("Concrete Cover: [mm]",  min_value=(0.0), value=(20.0), step=(0.5), key="MC_Yang_14")
        sample_total = st.number_input("Total of Samples: [-]", min_value=(1), value=(1000), step=(100), key="MC_Yang_15")

        if st.button("Calculate", key="MC_Yang_16"): 
            # Distribution of CO2 (Normal):
            CO2 = 0.0409*CO2*44.01/100                          # [%]->[kg/m³]
            CO2_p=np.random.normal(CO2, 0.0001, sample_total)   # [kg/m³]
            CO2_p=(100*CO2_p)/(44.01*0.0409)                    # [kg/m³]->[%]
            # Distribution of RH (Beta):
            m=RH; s=12.9; a=0; b=100; var=s**2                      #m=Mittelwert, s=Standardabweichung, a=Min, b=Max, var=Varianz
            alpha_input = ((a-m)*(a*b-a*m-b*m+m**2+var))/(var*(b-a))
            beta_input = -((b-m)*(a*b-a*m-b*m+m**2+var))/(var*(b-a))
            RH_p = beta.rvs(alpha_input, beta_input, scale=b-a, loc=a, size=sample_total)

            X=[]
            bar=st.progress(0)
            for i in range(0,sample_total):
                bar.progress((1+i)/sample_total)
                Calc_MC = Yang(i, t, C, S, G, FA, GGBS, SF, wb, RH_p[i], CO2_p[i], ExCo, Finishing)
                X.append(Calc_MC)
            Calc_MC.histogram(X, t, c_nom, sample_total)
