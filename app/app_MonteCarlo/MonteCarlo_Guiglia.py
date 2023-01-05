# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:23:23 2022

@author: Marco
"""
import streamlit as st
import numpy as np
import plotly.express as pex
from dataclasses import dataclass
from CarboModels import Guiglia

@dataclass
class MC_Guiglia():

    def __post_init__(self):
        col1, col2 = st.columns([1,1])
        with col1: 
            f_c = st.number_input("Mean Concrete Compressive Strenght: [MPa]", min_value=(1.0), max_value=(100.0), value=(30.0), step=(0.5), key="MC_Guiglia_01")
            RH = st.number_input("Mean Relative Air Humidity: [%]", min_value=(0.0), max_value=(100.0), value=(70.0), step=(0.5), key="MC_Guiglia_02")
        with col2:
            Building = st.radio("Building type:", ("Tunnel","Others"), key="MC_Guiglia_03")
        t = st.number_input("Service Time: [years]", min_value=(1), value=(50), step=(1), key="MC_Guiglia_04")
        c_nom = st.number_input("Concrete Cover: [mm]",  min_value=(0.0), value=(20.0), step=(0.5), key="MC_Guiglia_05")
        sample_total = st.number_input("Total of Samples: [-]", min_value=(1), value=(1000), step=(100), key="MC_Guiglia_06")

        if st.button("Calculate", key="MC_Guiglia_07"): 
            X=[]
            bar=st.progress(0)
            for i in range(0,sample_total):
                bar.progress((1+i)/sample_total)
                Calc_MC = Guiglia(i, f_c, RH, Building)
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
          
