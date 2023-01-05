# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 18:09:21 2023

@author: marco
"""
import streamlit as st
from dataclasses import dataclass
from app_Models.app_Häkkinen import app_Häkkinen                        # Model 01
from app_Models.app_fib import app_fib                                  # Model 02
from app_Models.app_CECS import app_CECS                                # Model 03
from app_Models.app_Guiglia import app_Guiglia                          # Model 04
from app_Models.app_Silva import app_Silva                              # Model 05
from app_Models.app_Yang import app_Yang                                # Model 06
from app_Models.app_Hills import app_Hills                              # Model 07      
from app_Models.app_GreveDierfeld import app_GreveDierfeld              # Model 08
from app_Models.app_Ta import app_Ta                                    # Model 09
from app_Models.app_Ekolu import app_Ekolu                              # Model 10
from app_Models.app_Possan import app_Possan                            # Model 11

@dataclass
class Models:
        
    def __post_init__(self):
        st.subheader("Choose a Model:")
        name = st.selectbox("Choose a Model:", ("Model 01", "Model 02", "Model 03", "Model 04", "Model 05", "Model 06", "Model 07", "Model 08", "Model 09", "Model 10", "Model 11"), label_visibility="collapsed")
        
        if name == "Model 01":      # Häkkinen
            app_Häkkinen(name)
                
        elif name == "Model 02":    # fib
            app_fib(name)
        
        elif name == "Model 03":    # CECS
            app_CECS(name)
                
        elif name == "Model 04":    # Guiglia
            app_Guiglia(name)
               
        elif name == "Model 05":    # Silva
            app_Silva(name)
                
        elif name == "Model 06":    # Yang
            app_Yang(name)
            
        elif name == "Model 07":    # Hills
            app_Hills(name)
            
        elif name == "Model 08":    # Geve-Dierfeld
            app_GreveDierfeld(name)    
        
        elif name == "Model 09":    # Ta
           app_Ta(name)
            
        elif name == "Model 10":    # Ekolu
            app_Ekolu(name)
    
        elif name == "Model 11":    # Possan
           app_Possan(name)