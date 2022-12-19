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
            ExCo = st.radio("Choose location of component:", ["Exposed", "Sheltered","Indoor"])

        with col2:
            Mixture = st.radio("Choose content in the concrete:",["ordinary portland cement (OPC)","OPC + blast furnace slag","OPC + fly ash"])
        Depending = st.radio("Model depending on...", ["time","compressive strength"])
        if Depending=="time":
            Origin = st.radio("Choose origin:",["Experimental", "Structural"])
            Age = st.number_input("Age of concrete (years): ", min_value=1,value=50)
            t = st.number_input("Minimum lifetime (years): ", min_value=1,value=50)

            if st.button("Calculate"):
                Modell07 = Hills_time(self.name, Mixture, ExCo, Origin, Age)
                Modell07.calculate(t)
                
        elif Depending=="compressive strength":
            f_c = st.number_input("Concrete compressive strength fcm: (N/mm²)",0.0,None,25.0,step=(0.5))
            t = st.number_input("Minimum lifetime (years): ", min_value=1,value=50)

            if st.button("Calculate"):
                Modell07 = Hills_fc(self.name, Mixture, ExCo, f_c)
                Modell07.calculate(t)
