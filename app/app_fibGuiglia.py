# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:22:18 2022

@author: Marco
"""
import streamlit as st
from dataclasses import dataclass
from CarboModels import fibGuiglia

@dataclass
class app_fibGuiglia():
    
    name:str
    
    def __post_init__(self):
        st.subheader("leer")
