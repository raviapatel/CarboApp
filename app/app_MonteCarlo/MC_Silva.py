# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:23:53 2022

@author: Marco
"""
import streamlit as st
import numpy as np
from scipy.stats import beta
from dataclasses import dataclass
from CarboModels.Silva import Silva

@dataclass
class MC_Silva():  #Model 05

    def __post_init__(self):
        col1, col2 = st.columns([1,1])
        with col1:
            RH = st.number_input("Mean Relative Air Humidity: [%]", min_value=(2.0), max_value=(98.0), value=(70.0), step=(0.5), key="MC_Yang_07")
            CO2 = st.number_input("CO2 Density around Concrete Surface: [%]", min_value=(0.0), max_value=(100.0), value=(0.04), step=(0.005), format=("%.4f"), key="MC_Silva_02")
            f_c = st.number_input("Mean Concrete Compressive Strenght: [MPa]", min_value=(1.0), max_value=(100.0), value=(30.0), step=(0.5), key="MC_Silva_03")
          
        with col2:
            C = st.number_input("Clinker Content: [kg/m³]", min_value=(0.0), value=(350.0), step=(5.0), key="MC_Silva_04")
            ExpC = st.radio("Choose Exposure Class:", ("XC1","XC2","XC3","XC4"), key="MC_Silva_05")   
        t = st.number_input("Service Time: [years]", min_value=(1), value=(50), step=(1), key="MC_Silva_06")       
        c_nom = st.number_input("Concrete Cover: [mm]",  min_value=(0.0), value=(20.0), step=(0.5), key="MC_Silva_07")
        sample_total = st.number_input("Total of Samples: [-]", min_value=(1), value=(1000), step=(100), key="MC_Silva_08")
        
        if st.button("Calculate", key="MC_Silva_09"): 
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
                Calc_MC = Silva(i, C, f_c, ExpC, RH_p[i], CO2_p[i])
                X.append(Calc_MC)
            Calc_MC.histogram(X, t, c_nom, sample_total)
