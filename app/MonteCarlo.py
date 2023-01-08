# -*- coding: utf-8 -*-

import streamlit as st
from dataclasses import dataclass
from app.app_MonteCarlo.MC_Häkkinen import MC_Häkkinen              # Model 01
from app.app_MonteCarlo.MC_fib import MC_fib                        # Model 02
from app.app_MonteCarlo.MC_CECS import MC_CECS                      # Model 03
from app.app_MonteCarlo.MC_Guiglia import MC_Guiglia                # Model 04
from app.app_MonteCarlo.MC_Silva import MC_Silva                    # Model 05
from app.app_MonteCarlo.MC_Yang import MC_Yang                      # Model 06
from app.app_MonteCarlo.MC_Hills import MC_Hills                    # Model 07
from app.app_MonteCarlo.MC_GreveDierfeld import MC_GreveDierfeld    # Model 08
from app.app_MonteCarlo.MC_Ta import MC_Ta                          # Model 09
from app.app_MonteCarlo.MC_Ekolu import MC_Ekolu                    # Model 10
from app.app_MonteCarlo.MC_Possan import MC_Possan                  # Model 11

@dataclass
class MonteCarlo():
    
    def __post_init__(self):
        st.subheader("Choose a Model:")
        name = st.selectbox("Choose a Model:", ("Model 01", "Model 02", "Model 03", "Model 04", "Model 05", "Model 06", "Model 07", "Model 08", "Model 09", "Model 10", "Model 11"), label_visibility="collapsed", key=("MC_select"))
     
        if name == "Model 01":      # Häkkinen
            MC_Häkkinen()
                
        elif name == "Model 02":    # fib
            MC_fib()

        elif name == "Model 03":    # CECS
            MC_CECS()
                
        elif name == "Model 04":    # Guiglia
            MC_Guiglia()
               
        elif name == "Model 05":    # Silva
            MC_Silva()
                
        elif name == "Model 06":    # Yang
            MC_Yang()
            
        elif name == "Model 07":    # Hills
            MC_Hills()
            
        elif name == "Model 08":    # Geve-Dierfeld
            MC_GreveDierfeld()  
        
        elif name == "Model 09":    # Ta
           MC_Ta()
            
        elif name == "Model 10":    # Ekolu 
            MC_Ekolu()

        elif name == "Model 11":    # Possan
           MC_Possan()

           
           