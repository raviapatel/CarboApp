# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:24:23 2022

@author: Marco
"""

import streamlit as st
import numpy as np
from dataclasses import dataclass
from CarboModels.Hills_time import Hills_time
from CarboModels.Hills_fc import Hills_fc

@dataclass
class MC_Hills():  #Model 07

    def __post_init__(self):
        col1, col2 = st.columns([1,1])
        with col1: 
            ExCo = st.radio("Choose Exposure Condition of Component:", ["Exposed to Rain", "Sheltered from Rain","Indoor"], key="MC_Hills_01")
            Depending = st.radio("Model depending on...", ["Time","Compressive Strength"], key="MC_Hills_02")
        with col2:
            mixture = st.radio("Choose Content in the Concrete:",["Ordinary Portland Cement (OPC)","OPC + Blast Furnace Slag","OPC + Fly Ash"], key="MC_Hills_03")
        
        if Depending=="Time":
            with col2:
                Origin = st.radio("Choose Origin of Component:",["Experimental", "Structural"], key="MC_Hills_04")
                Age = st.number_input("Age of Concrete: [years] ", min_value=(0.0),value=(5.0), step=(0.5), key="MC_Hills_05")
            t = st.number_input("Service Time: [years]", min_value=(1), value=(50), step=(1), key="MC_Hills_06")
            c_nom = st.number_input("Concrete Cover: [mm]",  min_value=(0.0), value=(20.0), step=(0.5), key="MC_Hills_07")
            sample_total = st.number_input("Total of Samples: [-]", min_value=(1), value=(1000), step=(100), key="MC_Hills_08")

            if st.button("Calculate", key="MC_Hills_09"): 
                X=[]
                bar=st.progress(0)
                for i in range(0,sample_total):
                    bar.progress((1+i)/sample_total)
                    Calc_MC = Hills_time(i, mixture, ExCo, Origin, Age)
                    X.append(Calc_MC)
                Calc_MC.histogram(X, t, c_nom, sample_total)

        elif Depending=="Compressive Strength":
            with col2:    
                f_c = st.number_input("Mean Concrete Compressive Strenght: [MPa]", min_value=(1.0), max_value=(100.0), value=(30.0), step=(0.5), key="MC_Hills_10")
            t = st.number_input("Service Time: [years]", min_value=(1), value=(50), step=(1), key="MC_Hills_11")
            c_nom = st.number_input("Concrete Cover: [mm]",  min_value=(0.0), value=(20.0), step=(0.5), key="MC_Hills_12")
            sample_total = st.number_input("Total of Samples: [-]", min_value=(1), value=(1000), step=(100), key="MC_Hills_13")

            if st.button("Calculate", key="MC_Hills_14"): 
                X=[]
                bar=st.progress(0)
                for i in range(0,sample_total):
                    bar.progress((1+i)/sample_total)
                    Calc_MC = Hills_fc(i, mixture, ExCo, f_c)
                    X.append(Calc_MC)
                Calc_MC.histogram(X, t, c_nom, sample_total)

         
