# -*- coding: utf-8 -*-

import streamlit as st
from dataclasses import dataclass
from app.app_Models.app_Häkkinen import app_Häkkinen                # Model 01 - Häkkinen
from app.app_Models.app_fib import app_fib                          # Model 02 - fib Model Code
from app.app_Models.app_CECS import app_CECS                        # Model 03 - CECS
from app.app_Models.app_Guiglia import app_Guiglia                  # Model 04 - Guiglia, Taliano
from app.app_Models.app_Silva import app_Silva                      # Model 05 - Silva et al.
from app.app_Models.app_Yang import app_Yang                        # Model 06 - Yang et al.
from app.app_Models.app_Hills import app_Hills                      # Model 07 - Hills et al.      
from app.app_Models.app_GreveDierfeld import app_GreveDierfeld      # Model 08 - Greve-Dierfeld, Gehlen
from app.app_Models.app_Ta import app_Ta                            # Model 09 - Ta et al.
from app.app_Models.app_Ekolu import app_Ekolu                      # Model 10 - Ekolu
from app.app_Models.app_Possan import app_Possan                    # Model 11 - Possan et al.

@dataclass
class Models:
        
    def __post_init__(self):
        st.subheader("Choose a Model:")
        name = st.selectbox("Choose a Model:", ("Häkkinen", "fib Model Code", "CECS", "Guiglia, Taliano", "Silva et al.", "Yang et al.", "Hills et al.", "Greve-Dierfeld, Gehlen", "Ta et al.", "Ekolu", "Possan et al."), label_visibility="collapsed")
        
        if name == "Häkkinen":            # Häkkinen
            app_Häkkinen(name)
                
        elif name == "fib Model Code":    # fib
            app_fib(name)
        
        elif name == "CECS":    # CECS
            app_CECS(name)
                
        elif name == "Guiglia, Taliano":    # Guiglia
            app_Guiglia(name)
               
        elif name == "Silva et al.":    # Silva
            app_Silva(name)
                
        elif name == "Yang et al.":    # Yang
            app_Yang(name)
            
        elif name == "Hills et al.":    # Hills
            app_Hills(name)
            
        elif name == "Greve-Dierfeld, Gehlen":    # Geve-Dierfeld
            app_GreveDierfeld(name)    
        
        elif name == "Ta et al.":    # Ta
           app_Ta(name)
            
        elif name == "Ekolu":    # Ekolu
            app_Ekolu(name)
    
        elif name == "Possan et al.":    # Possan
           app_Possan(name)