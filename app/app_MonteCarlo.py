# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 11:45:48 2022

@author: marco
"""
import streamlit as st
from MonteCarlo.MonteCarlo_Häkkinen import MC_Häkkinen              # Modell 01
from MonteCarlo.MonteCarlo_fib import MC_fib                        # Modell 02
from MonteCarlo.MonteCarlo_CECS import MC_CECS                      # Modell 03
from MonteCarlo.MonteCarlo_Guiglia import MC_Guiglia                # Modell 04
from MonteCarlo.MonteCarlo_Silva import MC_Silva                    # Modell 05
from MonteCarlo.MonteCarlo_Yang import MC_Yang                      # Modell 06
from MonteCarlo.MonteCarlo_Hills import MC_Hills                    # Modell 07
from MonteCarlo.MonteCarlo_GreveDierfeld import MC_GreveDierfeld    # Modell 08
from MonteCarlo.MonteCarlo_Ta import MC_Ta                          # Modell 09
from MonteCarlo.MonteCarlo_Ekolu import MC_Ekolu                    # Modell 10
from MonteCarlo.MonteCarlo_Possan import MC_Possan                  # Modell 11



class app_MonteCarlo():
    
    def __init__(self):
        st.subheader("Choose a Model:")
        name = st.selectbox("Choose a Model:", ("Model 01", "Model 02", "Model 03", "Model 04", "Model 05", "Model 06", "Model 07", "Model 08", "Model 09", "Model 10", "Model 11"), label_visibility="collapsed", key=("MC_select"))
     
        if name == "Model 01":      # Häkkinen
            MC_Häkkinen()
                
        elif name == "Model 02":    # fib
            MC_fib()

        elif name == "Model 03":    # CECS
            MC_CECS()
                
        # elif name == "Model 04":    # Guiglia
        #     MC_Guiglia()
               
        elif name == "Model 05":    # Silva
            MC_Silva()
                
        elif name == "Model 06":    # Yang
            MC_Yang()
            
        # elif name == "Model 07":    # Hills
        #     MC_Hills()
            
        elif name == "Model 08":    # Geve-Dierfeld
            MC_GreveDierfeld()  
        
        elif name == "Model 09":    # Ta
           MC_Ta()
            
        elif name == "Model 10":    # Ekolu 
            MC_Ekolu()

        elif name == "Model 11":    # Possan
           MC_Possan()

           
           