# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 13:27:45 2023

@author: marco
"""
import streamlit as st
from dataclasses import dataclass

@dataclass
class Home:
    
    def __post_init__(self):
        st.subheader("Overwiew")
        st.markdown("""
Hier finden Sie eine Übersicht der Modelle 
                    """)
        st.subheader("Models")
        st.markdown("""
Hier können Sie die einzelnen Modelle berechnen
                    """)
        st.subheader("Compare Models")
        st.markdown("""
Hier können Sie die Ergebnisse der verschiedenen Modelle vergleichen. 
Achtung: Nicht alle Modelle sind aufgrund der verschiedenen Anwendungsbereiche miteinander vergleichbar!
                    """)
        st.subheader("Monte Carlo")
        st.markdown("""
Hier können die Modelle probabilistisch angewendet werden.
Die Parameter, die probabilistisch nach fib [.] angenommen wurden, finden Sie hier:
                    """)
        