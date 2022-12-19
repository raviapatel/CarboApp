# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 11:45:48 2022

@author: marco
"""
import streamlit as st
from MonteCarlo.MonteCarlo_fibGuiglia import MC_fibGuiglia
from app.app_Häkkinen import app_Häkkinen
from app.app_fib import app_fib
from app.app_CECS import app_CECS
from app.app_Guiglia import app_Guiglia
from app.app_Silva import app_Silva
from app.app_Yang import app_Yang
from app.app_Hills import app_Hills
from app.app_fibGreveDierfeld import app_fibGreveDierfeld
from app.app_Ta import app_Ta
from app.app_Ekolu import app_Ekolu
from app.app_Possan import app_Possan

class app_MonteCarlo():
    
    def __init__(self):
        
        col1, col2 = st.columns([1,1])
        with col1: 
            RH = st.number_input("Relative Humidity: (%)", value=(65.0))
            C_co2 = st.number_input("Peripheral Concentration by Weight of CO2", value=(10.0))
            t_c = st.number_input("Curing time: (days)", value=(5.0))
            p_sr = st.number_input("Probability of Driving Rain: (-)")

        with col2: 
            ToW = st.number_input("Time of wettness: (days)")
            f_c = st.number_input("f_c")
            c_nom = st.number_input("c_nom", value=20)
            sample_total=st.number_input("sample_total", min_value=5, value=1000)
        
        t = st.number_input("Minimum lifetime: (years)", key="ABC1")
        
        if st.button("Calculate", key="CalculateMM"):
            MC_fibGuiglia(RH, ToW, p_sr, t_c, f_c, C_co2, t, c_nom, sample_total)
       
        """
        st.subheader("Choose a Model:")
        name = st.selectbox("Choose a Model:",("Model 01 - Häkkinen", "Model 02 - fib", "Model 03 - CECS", "Model 04 - Guiglia", "Model 05 - Silva", "Model 06 - Yang", "Model 07 - Hills", "Model 08 - Greve-Dierfeld", "Model 09 - Ta", "Model 10 - Ekolu", "Model 11 - Possan"), label_visibility="collapsed")
        
        if name =="Compare":
            st.subheader("switch to tab 'compare'")
        
        if name == "Model 01 - Häkkinen":         # Häkkinen
            app_Häkkinen(name)
                
        elif name == "Model 02 - fib":            # fib - leer
            app_fib(name)
        
        elif name == "Model 03 - CECS":           # CECS
            app_CECS(name)
                
        elif name == "Model 04 - Guiglia":        # Guiglia
            app_Guiglia(name)
               
        elif name == "Model 05 - Silva":          # Silva
            app_Silva(name)
                
        elif name == "Model 06 - Yang":           # Yang
            app_Yang(name)
            
        elif name == "Model 07 - Hills":          # Hills
            app_Hills(name)
            
        elif name == "Model 08 - Greve-Dierfeld": # Geve-Dierfeld
            app_fibGreveDierfeld(name)    
        
        elif name == "Model 09 - Ta":             # Ta - leer
           app_Ta(name)
            
        elif name == "Model 10 - Ekolu":          # Ekolu - leer
            app_Ekolu(name)

        elif name == "Model 11 - Possan":         # Possan - leer
           app_Possan(name)
           
           """