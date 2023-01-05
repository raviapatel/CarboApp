import streamlit as st
from app.app_Home import app_home
from app.app_Overwiew import app_overwiew
from app.app_Compare import app_Compare
from app.app_MonteCarlo import app_MonteCarlo
from app.app_Models import app_Models

#Aufbau Website:
st.set_page_config(page_title="Carbonation Depth", page_icon="🏗️", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.title("Calculation of Carbonation Depth")

tab1, tab2, tab3, tab4 , tab5 = st.tabs(["Home","Overview","Models","Compare Models","Monte Carlo"])

with tab1:              # Home
     app_home()
    
with tab2:              # Overview
    app_overwiew()
  
with tab3:              # Models
    app_Models()

with tab4:              # Compare Models
    app_Compare()
    
with tab5:              # Monte Carlo
    app_MonteCarlo()
