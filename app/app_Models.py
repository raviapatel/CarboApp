# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 18:09:21 2023

@author: marco
"""
import streamlit as st
from dataclasses import dataclass
from app.app_models.app_Häkkinen import app_Häkkinen
from app.app_models.app_fib import app_fib
from app.app_models.app_CECS import app_CECS
from app.app_models.app_Guiglia import app_Guiglia
from app.app_models.app_Silva import app_Silva
from app.app_models.app_Yang import app_Yang
from app.app_models.app_Hills import app_Hills
from app.app_models.app_GreveDierfeld import app_GreveDierfeld
from app.app_models.app_Ta import app_Ta
from app.app_models.app_Ekolu import app_Ekolu
from app.app_models.app_Possan import app_Possan


class app_Models:
        
    def __init__(self):
        st.subheader("Choose a Model:")
        name = st.selectbox("Choose a Model:",("Model 01", "Model 02", "Model 03", "Model 04", "Model 05", "Model 06", "Model 07", "Model 08", "Model 09", "Model 10", "Model 11"), label_visibility="collapsed")
        
        if name =="Compare":
            st.subheader("switch to tab 'compare'")
        
        if name == "Model 01":         # Häkkinen
            app_Häkkinen(name)
                
        elif name == "Model 02":            # fib - leer
            app_fib(name)
        
        elif name == "Model 03":           # CECS
            app_CECS(name)
                
        elif name == "Model 04":        # Guiglia
            app_Guiglia(name)
               
        elif name == "Model 05":          # Silva
            app_Silva(name)
                
        elif name == "Model 06":           # Yang
            app_Yang(name)
            
        elif name == "Model 07":          # Hills
            app_Hills(name)
            
        elif name == "Model 08": # Geve-Dierfeld
            app_GreveDierfeld(name)    
        
        elif name == "Model 09":             # Ta - leer
           app_Ta(name)
            
        elif name == "Model 10":          # Ekolu - leer
            app_Ekolu(name)
    
        elif name == "Model 11":         # Possan - leer
           app_Possan(name)