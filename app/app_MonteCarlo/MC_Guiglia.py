# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:23:23 2022

@author: Marco
"""
import streamlit as st
from scipy.stats import beta
from dataclasses import dataclass
from CarboModels.Guiglia import Guiglia

@dataclass
class MC_Guiglia():

    def __post_init__(self):
        col1, col2 = st.columns([1,1])
        with col1: 
            f_c = st.number_input("Mean Concrete Compressive Strenght: [MPa]", min_value=(1.0), max_value=(100.0), value=(30.0), step=(0.5), key="MC_Guiglia_01")
            RH = st.number_input("Mean Relative Air Humidity: [%]", min_value=(2.0), max_value=(98.0), value=(70.0), step=(0.5), key="MC_Yang_07")
        with col2:
            Building = st.radio("Building type:", ("Tunnel","Others"), key="MC_Guiglia_03")
        t = st.number_input("Service Time: [years]", min_value=(1), value=(50), step=(1), key="MC_Guiglia_04")
        c_nom = st.number_input("Concrete Cover: [mm]",  min_value=(0.0), value=(20.0), step=(0.5), key="MC_Guiglia_05")
        sample_total = st.number_input("Total of Samples: [-]", min_value=(1), value=(1000), step=(100), key="MC_Guiglia_06")

        if st.button("Calculate", key="MC_Guiglia_07"): 
            # Distribution of RH (Beta):
            m=RH; s=12.9; a=0; b=100; var=s**2                      #m=Mittelwert, s=Standardabweichung, a=Min, b=Max, var=Varianz
            alpha_input = ((a-m)*(a*b-a*m-b*m+m**2+var))/(var*(b-a))
            beta_input = -((b-m)*(a*b-a*m-b*m+m**2+var))/(var*(b-a))
            RH_p = beta.rvs(alpha_input, beta_input, scale=b-a, loc=a, size=sample_total)
            X=[]
            bar=st.progress(0)
            for i in range(0,sample_total):
                bar.progress((1+i)/sample_total)
                Calc_MC = Guiglia(i, f_c, RH_p[i], Building)
                X.append(Calc_MC)
            Calc_MC.histogram(X, t, c_nom, sample_total)

          
