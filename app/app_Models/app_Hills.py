# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:22:18 2022

@author: Marco
"""
import streamlit as st
from dataclasses import dataclass
from CarboModels import Hills_time
from CarboModels import Hills_fc

@dataclass
class app_Hills():  #Model 07
    
    name:str
    
    def __post_init__(self):
        col1, col2 = st.columns([1,1])
        with col1: 
            ExCo = st.radio("Choose Exposure Condition of Component:", ["Exposed to Rain", "Sheltered from Rain","Indoor"])
            Depending = st.radio("Model depending on...", ["Time","Compressive Strength"])
        with col2:
            mixture = st.radio("Choose Content in the Concrete:",["Ordinary Portland Cement (OPC)","OPC + Blast Furnace Slag","OPC + Fly Ash"])
        
        if Depending=="Time":
            with col2:
                Origin = st.radio("Choose Origin of Component:",["Experimental", "Structural"])
                Age = st.number_input("Age of Concrete: [years] ", min_value=(0.0),value=(5.0), step=(0.5))
            t = st.number_input("Service Time: [years]", min_value=(1), value=(50), step=(1))
            if st.button("Calculate"):
                Modell07 = Hills_time(self.name, mixture, ExCo, Origin, Age)
                Modell07.calculate(t)
                
        elif Depending=="Compressive Strength":
            with col2:    
                f_c = st.number_input("Mean Concrete Compressive Strenght: [MPa]", min_value=(1.0), max_value=(100.0), value=(30.0), step=(0.5))
            t = st.number_input("Service Time: [years]", min_value=(1), value=(50), step=(1))
            if st.button("Calculate"):
                Modell07 = Hills_fc(self.name, mixture, ExCo, f_c)
                Modell07.calculate(t)
