# -*- coding: utf-8 -*-

import streamlit as st
from app.Home import Home
from app.Overwiew import Overwiew
from app.Models import Models
from app.Compare import Compare
from app.MonteCarlo import MonteCarlo

#Page Configurations:
st.set_page_config(page_title="Carbonation Depth", page_icon="🏗️", layout="centered", initial_sidebar_state="auto", menu_items=None)

#Carbo App:

st.title("Calculation of Carbonation Depth")

tab1, tab2, tab3, tab4 , tab5 = st.tabs(["Home","Overview","Models","Compare Models","Monte Carlo"])

with tab1:              # Home
     Home()
    
with tab2:              # Overview of Models
    Overwiew()
  
with tab3:              # Models 
    Models()

with tab4:              # Compare Models
    Compare()
    
with tab5:              # Monte Carlo
    MonteCarlo()
