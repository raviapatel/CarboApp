# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:25:49 2022

@author: Marco
"""
import streamlit as st
import numpy as np
import plotly.express as pex
from dataclasses import dataclass
from CarboModels import GreveDierfeld

@dataclass
class MC_GreveDierfeld(): #Model 08

    def __post_init__(self):
        col1, col2 = st.columns([1,1])
        with col1:
            RH = st.number_input("Mean Relative Air Humidity: [%]", min_value=(0.0), max_value=(100.0), value=(70.0), step=(0.5), key="MC_GD_01")
            wb = st.number_input("Water / Binder Ratio: [-]",min_value=(0.0), value=(0.5), max_value=(0.65),step=(0.01), key="MC_GD_02")
            t_c = st.number_input("Curing Time: [days]", min_value=(0), value=(3), step=(1), key="MC_GD_03")
            CO2 = st.number_input("CO2 Density around Concrete Surface: [%]", min_value=(0.0), max_value=(100.0), value=(0.04), step=(0.005), format=("%.4f"), key="MC_GD_04")

        with col2:
            Cem = st.radio("Choose CEM", ["CEM I", "CEM II/A", "CEM II/B", "CEM II/A", "CEM III/B"], key="MC_GD_05")
            ToW = st.number_input("Average Number of Rainy Days per Year [days]", min_value=(0.0), max_value=(365.0), value=(130.0), key="MC_GD_06")
            p_dr = st.number_input("Probability of Driving Rain: [%]", min_value=(0.0), max_value=(100.0), value=(30.0), step=(0.5), key="MC_GD_07")
                
        t = st.number_input("Service Time: [years]", min_value=(1), max_value=(100), value=(50), step=(1), key="MC_GD_08")
        c_nom = st.number_input("Concrete Cover: [mm]",  min_value=(0.0), value=(20.0), step=(0.5), key="MC_GD_09")
        sample_total = st.number_input("Total of Samples: [-]", min_value=(1), value=(1000), step=(100), key="MC_GD_10")
        
        if st.button("Calculate", key="MC_GD_11"): 
            #Distribution of CO2, b_c, b_w according to fib.2006
            CO2 = 0.0409*CO2*44.01/100                          # [%]->[kg/m³]
            CO2_p=np.random.normal(CO2, 0.0001, sample_total)   # [kg/m³]
            CO2_p=(100*CO2_p)/(44.01*0.0409)                    # [kg/m³]->[%]
            b_c_p=np.random.normal(-0.567, 0.024, sample_total)   
            b_w_p=np.random.normal(0.446, 0.163, sample_total)   

            X=[]
            bar=st.progress(0)
            for i in range(0,sample_total):
                bar.progress((1+i)/sample_total)
                Calc_MC = GreveDierfeld(i, RH, Cem, wb, CO2_p[i], ToW, p_dr, t_c, b_c=b_c_p[i], b_w=b_w_p[i])
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