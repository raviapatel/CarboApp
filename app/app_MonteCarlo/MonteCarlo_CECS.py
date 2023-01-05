# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:23:12 2022

@author: Marco
"""
import streamlit as st
import numpy as np
import plotly.express as pex
from dataclasses import dataclass
from CarboModels import CECS220

@dataclass
class MC_CECS():
    def __post_init__(self):
        col1, col2 = st.columns([1,1])
        with col1:
            Stress = st.radio("Choose Stress on Component:", ["Pressure", "Tension"], key="MC_CECS_01")
            f_c = st.number_input("Mean Concrete Compressive Strenght: [MPa]", min_value=(1.0), max_value=(100.0), value=(30.0), step=(0.5), key="MC_CECS_02")
            T = st.number_input("Mean Temperature: [°C]", value=(15.0), step=(0.5), key="MC_CECS_03")
            RH = st.number_input("Mean Relative Air Humidity: [%]", min_value=(0.0), max_value=(100.0), value=(70.0), step=(0.5), key="MC_CECS_04")
        with col2:
            Location = st.radio("Choose Location of Component:", ["Corner", "Other Area"], key="MC_CECS_05")
            FA_c = st.number_input("Fly Ash Content: [weight ratio]", min_value=(0.0), value=(0.0), max_value=(1.0), step=(0.01), key="MC_CECS_06")
            CO2 = st.number_input("CO2 Density around Concrete Surface: [%]", min_value=(0.0), max_value=(100.0), value=(0.04), step=(0.005), format=("%.4f"), key="MC_CECS_07")
        t = st.number_input("Service Time: [years]", min_value=(1), max_value=(100), value=(50), step=(1), key="MC_CECS_08")
        c_nom = st.number_input("Concrete Cover: [mm]",  min_value=(0.0), value=(20.0), step=(0.5), key="MC_CECS_09")
        sample_total = st.number_input("Total of Samples: [-]", min_value=(1), value=(1000), step=(100), key="MC_CECS_10")

        if st.button("Calculate", key="MC_CECS_11"): 
            CO2 = 0.0409*CO2*44.01/100                          # [%]->[kg/m³]
            CO2_p=np.random.normal(CO2, 0.0001, sample_total)   # [kg/m³]
            CO2_p=(100*CO2_p)/(44.01*0.0409)                    # [kg/m³]->[%]
            X=[]
            bar=st.progress(0)
            for i in range(0,sample_total):
                bar.progress((1+i)/sample_total)
                Calc_MC = CECS220(i, f_c, FA_c, Stress, Location, T, RH, CO2_p[i])
                X.append(Calc_MC)
            counter=0
            x_cList=[]
            for i in range(0,sample_total):
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
