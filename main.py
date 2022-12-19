import streamlit as st
from app.app_overwiew import app_overwiew
from app.app_compare import app_Compare
from app.app_MonteCarlo import app_MonteCarlo
from app.app_Häkkinen import app_Häkkinen
from app.app_fib import app_fib
from app.app_CECS import app_CECS
from app.app_Guiglia import app_Guiglia
from app.app_Silva import app_Silva
from app.app_Yang import app_Yang
from app.app_Hills import app_Hills
from app.app_fibGreveDierfeld import app_fibGreveDierfeld
from app.app_Ta import app_Ta
from app.app_Ekolu import app_Ekolu
from app.app_Possan import app_Possan


#Aufbau Website:
st.set_page_config(page_title="Carbonation Depth", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("Calculation of Carbonation Depth")

tab1, tab2, tab3, tab4 , tab5 = st.tabs(["Home","Overview","Models","Compare Models","Monte Carlo"])

with tab1:              # Home
   st. header("Welcome")
    
with tab2:              # Overview
    app_overwiew()
  
    
with tab3:              # Models
    st.subheader("Choose a Model:")
    name = st.selectbox("Choose a Model:",("Model 01 - Häkkinen", "Model 02 - fib", "Model 03 - CECS", "Model 04 - Guiglia", "Model 05 - Silva", "Model 06 - Yang", "Model 07 - Hills", "Model 08 - Greve-Dierfeld", "Model 09 - Ta", "Model 10 - Ekolu", "Model 11 - Possan"), label_visibility="collapsed")
    
    if name =="Compare":
        st.subheader("switch to tab 'compare'")
    
    if name == "Model 01 - Häkkinen":         # Häkkinen
        app_Häkkinen(name)
            
    elif name == "Model 02 - fib":            # fib - leer
        app_fib(name)
    
    elif name == "Model 03 - CECS":           # CECS
        app_CECS(name)
            
    elif name == "Model 04 - Guiglia":        # Guiglia
        app_Guiglia(name)
           
    elif name == "Model 05 - Silva":          # Silva
        app_Silva(name)
            
    elif name == "Model 06 - Yang":           # Yang
        app_Yang(name)
        
    elif name == "Model 07 - Hills":          # Hills
        app_Hills(name)
        
    elif name == "Model 08 - Greve-Dierfeld": # Geve-Dierfeld
        app_fibGreveDierfeld(name)    
    
    elif name == "Model 09 - Ta":             # Ta - leer
       app_Ta(name)
        
    elif name == "Model 10 - Ekolu":          # Ekolu - leer
        app_Ekolu(name)

    elif name == "Model 11 - Possan":         # Possan - leer
       app_Possan(name)

with tab4:              # Compare Models
    app_Compare()
    
with tab5:
    app_MonteCarlo()
