import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as ex
from app.overwiew import overwiew
#import button
from CarboModels import Häkkinen
from CarboModels import CECS220
from CarboModels import Silva
from CarboModels import Guiglia
from CarboModels import Yang

#Aufbau Website:
st.set_page_config(page_title="Carbonation Depth", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("Calculation of Carbonation Depth")

tab1, tab2, tab3, tab4 = st.tabs(["Home","Overview","Calculations","Exposure classes"])

with tab1:              # Homepage
   st. header("Welcome")
    
with tab2:              # Overview of the Models
    overwiew()
    
with tab3:              # Calculations
    st.header("Choose a Model:")
    name = st.selectbox("Choose a Model:",("Model 01 - Häkkinen", "Model 02 - fib", "Model 03 - CECS", "Model 04 - Guiglia", "Model 05 - Silva", "Model 06 - Yang", "Model 07 - Hills", "Model 08 - Greve-Dierfeld", "Model 09 - Ta", "Model 10 - Ekolu", "Model 11 - Possan"), label_visibility="collapsed")

    if name == "Model 01 - Häkkinen":         # Häkkinen
        col1, col2  = st.columns([1,1])
        with col1:
            exposed = st.radio("Choose location of the component:", ["Sheltered from rain", "Exposed to rain"])
            f_c = st.number_input("Mean compressive strength of the concrete at the age of 28 days (MPa):", value=(25.0) , step=(0.5))
            C = st.number_input("Clinker Content (kg/m³):", value=(200.0), step=(0.5))
#        with col2:        
#            st.radio("  ", ["Not air entrained", "Air entrained"])
        with col2:
            entrained = st.radio("Choose if component is air entrained:", ["Air entrained","Not air entrained"])
            optional = st.radio("Choose optional mixture:", ["None","Fly ash", "Silicia fume", "Blast furnance slag"])
            if optional == "None": FA = 0.0;  SF = 0.0; GGBS = 0.0
            if optional == "Fly ash": FA = st.number_input("Fly ash (kg/m³):", help="recommended value 28%", step=(0.5)); SF = 0.0; GGBS = 0.0
            if optional == "Silicia fume": SF = st.number_input("Silicia fume (kg/m³):", help="recommended value 9%", step=(0.5)); FA = 0.0; GGBS = 0.0
            if optional == "Blast furnance slag": GGBS = st.number_input("Blast furnance slag (kg/m³):", help="recommended value 70%", step=(0.5)); FA = 0.0; SF = 0.0
        t = int(st.slider("Minimum lifetime (years): ", 1,100,50))
       
        if st.button("Calculate "): 
            Modell01 = Häkkinen(name, C, f_c, exposed, entrained, FA, SF, GGBS)
            Modell01.calculate(t)
            
    elif name == "Model 02 - fib":            # fib
        st.subheader("leer")
    
    elif name == "Model 03 - CECS":           # CECS
        st.subheader("Model 3")
        col1, col2 = st.columns([1,1])
        with col1:
            tension = st.radio("Stress:", ["pressure", "tension"])
            f_c = st.number_input("concrete characteristic compression strength (MPa):")
            T = st.number_input("Temperature: (°C)")
            RH = st.number_input("Relative humidity (%):")
        with col2:
            location = st.radio("Location of component:", ["corner", "other area"])
            FA = st.number_input("Fly ash content (weight ratio):")
            CO2 = st.number_input("CO2density around concrete surface:")
        t = int(st.slider("Minimum lifetime (years): ", 1,100,50))
      
        if st.button("Calculate "): 
            Modell03 = CECS220(name, f_c, FA, tension, location, T, RH, CO2) 
            Modell03.calculate(t)
            
    elif name == "Model 04 - Guiglia":        # Guiglia
       col1, col2 = st.columns([1,1])
       with col1: 
           building = st.selectbox("Building type:", ("Tunnel","others"))
           rh = st.number_input("Relative humidity (%):", 1,100,50)    
       with col2:
           fc = st.number_input("Concrete compressive strength fcm (N/mm²):",0.0,None,25.0,step=(0.5))
          
       t = st.slider("Minimum lifetime (years): ", 1,100,50)

       if st.button("Calculate "): 
           Modell04 = Guiglia(name, fc, rh, building) #(name, C, f_c, phi_clinker, ExpC, RH, CO2))(name, 0.5, 25, 0.5, 0.5, rh, 0.05)
           Modell04.calculate(t)
       
           
    elif name == "Model 05 - Silva":          # Silva
        col1, col2 = st.columns([1,1])
        with col1:
            rh = st.number_input("Relative humidity (%):", 1,100,50)    
            ExpC = st.selectbox("Exposure class:", ("XC1","XC2","XC3","XC4")) 
        with col2:
            fc = st.number_input("Concrete compressive strength fcm (N/mm²):",0.0,None,25.0,step=(0.5))
        with col1: CO2 = st.number_input("CO2: (%)",0.0,None,0.04,step=(0.01))
        with col2: C = st.number_input("C: (kg/m³)",0.0,None,220.0,step=(0.5))
        t = st.slider("Minimum lifetime (years): ", 1,100,50)
       
        if st.button("Calculate "): 
            Modell05 = Silva(name, C, fc, ExpC, rh, CO2) #(name, C, f_c, phi_clinker, ExpC, RH, CO2))(name, 0.5, 25, 0.5, 0.5, rh, 0.05)
            Modell05.calculate(t)
            
    elif name == "Model 06 - Yang":           # Yang
        col1, col2 = st.columns([1,1])
        with col1:
            C = st.number_input("Cement content (kg/m³):",0.0,None,25.0,step=(0.5))
            S = st.number_input("S ? (kg/m³):",0.0,None,25.0,step=(0.5))
            G = st.number_input("G ? (kg/m³):",0.0,None,25.0,step=(0.5))
            FA = st.number_input("Fly ash content (kg/m³):",0.0,None,25.0,step=(0.5))
            GGBS = st.number_input("Ground granulated blast-furnace slag content (kg/m³):",0.0,None,25.0,step=(0.5))
            SF = st.number_input("Silica fume content (kg/m³):",0.0,None,25.0,step=(0.5))

        with col2:
            RH = st.number_input("Relative humidity (%):", 1.0,100.0,50.0, step=0.5) 
            wc = st.number_input("Water / Cement ratio (-):",0.0,None,0.5,step=(0.05))
            C_co2 = st.number_input("CO2 (%):",0.0,None,25.0,step=(0.5))

            Location = st.radio("Choose location of component:", ["Outdoor","Indoor"])
            print(Location)
            if Location=="Outdoor":     Finishing = st.radio("Choose Finishing of component:", ["Nothing", "Plaster", "Paint", "Mortar", "Mortar + Plaster", "Mortar + Paint", "Tile"])
            elif Location=="Indoor":    Finishing = st.radio("Choose Finishing of component:", ["Nothing", "Paint", "Mortar", "Tile"])

        t = st.slider("Minimum lifetime (years): ", 1,100,50)
        
        if st.button("Calculate "): 
            Modell06 = Yang(name, t, C, S, G, FA, GGBS, SF, wc, RH, C_co2, Location, Finishing)
            Modell06.calculate(t)
        
    elif name == "Model 07 - Hills":          # Hills
        st.subheader("leer")
        
    elif name == "Model 08 - Greve-Dierfeld": # Geve-Dierfeld
        st.subheader("leer")
        
    elif name == "Model 09 - Ta":             # Ta
        st.subheader("leer")
        
    elif name == "Model 10 - Ekolu":          # Ekolu
        st.subheader("leer")

    elif name == "Model 11 - Possan":         # Possan
        st.subheader("leer")

with tab4:              # Exposure classes
    st.header("Exposure classes:")
    col1, col2 = st.columns([1,3])
    col1.write("XC1")
    col2.write("Dry or permanently wet")
    col1, col2 = st.columns([1,3])
    col1.write("XC2")
    col2.write("Wet, rarely dry")
    col1, col2 = st.columns([1,3])
    col1.write("XC3")
    col2.write("Moderate humidity")
    col1, col2 = st.columns([1,3])
    col1.write("XC4")
    col2.write("Cyclic wet and dry")
    

#    df = pd.DataFrame((("64","84"),("67","104"),("75","64")),index=("1","2","3"),columns=("relative humidity (%)","number of rainy days (-)"))
#   st.table(df)
#   t_range = np.arange(0, t+1)
 #  print(t_range)
 # x_clist = Modell04.x_cList(t)
 #  df=pd.DataFrame(data=(x_clist), index=("Year %d" % i for i in range(t+1)), dtype=(str))#, columns=("Carbonation depth"))
  # a = st.dataframe(df, use_container_width=True)
  #st.download_button("Download table", df.to_csv())
