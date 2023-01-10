# -*- coding: utf-8 -*-

import streamlit as st
from dataclasses import dataclass
from app.app_MonteCarlo.MC_Häkkinen import MC_Häkkinen              # Model 01 - Häkkinen
from app.app_MonteCarlo.MC_fib import MC_fib                        # Model 02 - fib Model Code
from app.app_MonteCarlo.MC_CECS import MC_CECS                      # Model 03 - CECS
from app.app_MonteCarlo.MC_Guiglia import MC_Guiglia                # Model 04 - Guiglia, Taliano
from app.app_MonteCarlo.MC_Silva import MC_Silva                    # Model 05 - Silva et al.
from app.app_MonteCarlo.MC_Yang import MC_Yang                      # Model 06 - Yang et al.
from app.app_MonteCarlo.MC_Hills import MC_Hills                    # Model 07 - Hills et al.
from app.app_MonteCarlo.MC_GreveDierfeld import MC_GreveDierfeld    # Model 08 - Greve-Dierfeld, Gehlen
from app.app_MonteCarlo.MC_Ta import MC_Ta                          # Model 09 - Ta et al.
from app.app_MonteCarlo.MC_Ekolu import MC_Ekolu                    # Model 10 - Ekolu
from app.app_MonteCarlo.MC_Possan import MC_Possan                  # Model 11 - Possan et al.

@dataclass
class MonteCarlo():
    
    def __post_init__(self):
        st.subheader("Choose a Model:")
        name = st.selectbox("Choose a Model:", ("Häkkinen", "fib Model Code", "CECS", "Guiglia, Taliano", "Silva et al.", "Yang et al.", "Hills et al.", "Greve-Dierfeld, Gehlen", "Ta et al.", "Ekolu", "Possan et al."), label_visibility="collapsed", key=("MC_select"))
     
        if name == "Häkkinen":      # Häkkinen
            MC_Häkkinen()
                
        elif name == "fib Model Code":    # fib
            MC_fib()

        elif name == "CECS":    # CECS
            MC_CECS()
                
        elif name == "Guiglia, Taliano":    # Guiglia
            MC_Guiglia()
               
        elif name == "Silva et al.":    # Silva
            MC_Silva()
                
        elif name == "Yang et al.":    # Yang
            MC_Yang()
            
        elif name == "Hills et al.":    # Hills
            MC_Hills()
            
        elif name == "Greve-Dierfeld, Gehlen":    # Geve-Dierfeld
            MC_GreveDierfeld()  
        
        elif name == "Ta et al.":    # Ta
           MC_Ta()
            
        elif name == "Ekolu":    # Ekolu 
            MC_Ekolu()

        elif name == "Possan et al.":    # Possan
           MC_Possan()

           
           