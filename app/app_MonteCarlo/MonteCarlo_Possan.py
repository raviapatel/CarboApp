# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:28:42 2022

@author: Marco
"""
import streamlit as st
import numpy as np
import plotly.express as pex
from dataclasses import dataclass
from CarboModels import Possan

@dataclass
class MC_Possan(): #Model 11

    def __post_init__(self):
        col1, col2  = st.columns([1,1])
        with col1:
            f_c = st.number_input("Mean Concrete Compressive Strenght: [MPa]", min_value=(1.0), max_value=(100.0), value=(30.0), step=(0.5), key="MC_Possan_01")
            C = st.number_input("Clinker Content: [kg/m³]", min_value=(0.0), value=(350.0), step=(5.0), key="MC_Possan_02")
            FA = st.number_input("Fly Ash Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0), key="MC_Possan_03")
            SF = st.number_input("Silicia Fume Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0), key="MC_Possan_04")

        with col2:
            ExCo = st.radio("Choose Exposure Condition of component:", ["Exposed to Rain", "Sheltered from Rain", "Indoor"], key="MC_Possan_05")
            Cem = st.radio("Choose Cement type:", ["CEM I", "CEM II/A-L", "CEM II/A-S", "CEM II/B-S", "CEM III/A", "CEM IV/A", "CEM IV/B"], key="MC_Possan_06")
            CO2 = st.number_input("CO2 Density around Concrete Surface: [%]", min_value=(0.0), max_value=(100.0), value=(0.04), step=(0.005), format=("%.4f"), key="MC_Possan_07")
            RH = st.number_input("Mean Relative Air Humidity: [%]", min_value=(0.0), max_value=(100.0), value=(70.0), step=(0.5), key="MC_Possan_08")

        t = st.number_input("Service Time: [years]", min_value=(1), value=(50), step=(1), key="MC_Possan_09")
        c_nom = st.number_input("Concrete Cover: [mm]",  min_value=(0.0), value=(20.0), step=(0.5), key="MC_Possan_10")
        sample_total = st.number_input("Total of Samples: [-]", min_value=(1), value=(1000), step=(100), key="MC_Possan_11")

        if st.button("Calculate", key="MC_Possan_12"): 
            CO2 = 0.0409*CO2*44.01/100                          # [%]->[kg/m³]
            CO2_p=np.random.normal(CO2, 0.0001, sample_total)   # [kg/m³]
            CO2_p=(100*CO2_p)/(44.01*0.0409)                    # [kg/m³]->[%]
            X=[]
            bar=st.progress(0)
            for i in range(0,sample_total):
                bar.progress((1+i)/sample_total)
                Calc_MC = Possan(i, C, FA, SF, Cem, f_c, ExCo, CO2_p[i], RH)
                X.append(Calc_MC)
            counter=0
            x_cList=[]
            for i in range(0,sample_total):
                if X[i].karbo == "NaN":
                    st.warning("Model not compatible with input values!")
                    return
                else:
                    x_cList.append(X[i].x_c(t))
                    if X[i].x_c(t)>c_nom:
                        counter=counter+1
            st.warning("Probability that concrete cover is not sufficient: " + str(round(counter/sample_total*100,2)) + "%")
            #Diagramm:
            res = {"X(t) [mm]":x_cList}
            fig = pex.histogram(res, x="X(t) [mm]")
            fig.add_vline(c_nom, line_dash="dash", line_color="green") #add_line(res1, x="X(t) [mm]")
            st.plotly_chart(fig)   
            #Tabelle:
            st.dataframe(res, use_container_width=True)
