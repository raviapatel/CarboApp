import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as ex
import overwiew
from CarboModels import Häkkinen
from CarboModels import CECS220
from CarboModels import Silva
from CarboModels import Guiglia

#Aufbau Website:
st.title("Calculation of Carbonation Depth")

tab1, tab2, tab3, tab4 = st.tabs(["Home","Overview","Calculations","Exposure classes"])

with tab1:              # Homepage
   st. header("Welcome")
    
with tab2:              # Overview of the Models
    overwiew()
    
with tab3:              # Calculations
    st.header("Choose a Model:")
    sb = st.selectbox("Choose a Model:",("Model 01 - Häkkinen", "Model 02 - fib", "Model 03 - CECS", "Model 04 - Guiglia", "Model 05 - Silva", "Model 06 - Yang", "Model 07 - Hills", "Model 08 - Greve-Dierfeld", "Model 09 - Ta", "Model 10 - Ekolu", "Model 11 - Possan"), label_visibility="collapsed")

    if sb == "Model 01 - Häkkinen":         # Häkkinen
        col1, col2  = st.columns([1,1])
        name = "M01"
        with col1:
            Exposed = st.radio(" ", ["Sheltered from rain", "Exposed to rain"])
            f_c = st.number_input("mean compressive strength of the concrete at the age of 28 days (MPa):")
            C = st.number_input("Clinker Content (kg/m³):")
#        with col2:        
#            st.radio("  ", ["Not air entrained", "Air entrained"])
        with col2:
            FA = st.number_input("Fly ash (kg/m³):")
            SF = st.number_input("Silicia fume (kg/m³):")
            GGBS = st.number_input("Blast furnance slag (kg/m³):")
        t = int(st.slider("Minimum lifetime (years): ", 1,100,50))
       
        if st.button("Calculate "): 
            Modell01 = Häkkinen(name, C, f_c, Exposed, FA, SF, GGBS)
            print("gut")
            print(Exposed)
            st.success("Carbonation depth: " + str(round(Modell01.x_c(t),1)) + " mm")
            
    elif sb == "Model 02 - fib":            # fib
        st.subheader("leer")
    
    elif sb == "Model 03 - CECS":           # CECS
        st.subheader("Model 3")
        name = "M03"
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
            st.success("Carbonation depth: " + str(round(Modell03.x_c(t),1)) + " mm")
        
    elif sb == "Model 04 - Guiglia":        # Guiglia
        
       name = "M04"
       col1, col2 = st.columns([1,1])
       with col1: 
           building = st.selectbox("Building type:", ("Tunnel","others"))
           rh = st.number_input("Relative humidity (%):", 1,100,50)    
       with col2:
           fc = st.number_input("Concrete compressive strength fcm (N/mm²):",0.0,None,25.0,step=(0.5))
          
       t = st.slider("Minimum lifetime (years): ", 1,100,50)

       if st.button("Calculate "): 
           Modell04 = Guiglia(name, fc, rh, building) #(name, C, f_c, phi_clinker, ExpC, RH, CO2))(name, 0.5, 25, 0.5, 0.5, rh, 0.05)
           st.success("Carbonation depth: " + str(round(Modell04.x_c(t),1)) + " mm")
           st.success("k =" + str(round(Modell04.karbo,2)) + " mm/year^0.5")
           t_range = np.arange(0, t+1)
           print(t_range)
           x_clist = Modell04.x_cList(t)
           df=pd.DataFrame(data=(x_clist), index=("Year %d" % i for i in range(t+1)), dtype=(str))#, columns=("Carbonation depth"))
           a = st.dataframe(df, use_container_width=True)
           
           st.download_button("Download table", df.to_csv())
           fig = ex.line(x_clist, title=("Model 04 - Guiglia")) #, x="time (years)", y="carbontion depth (mm)")
           st.plotly_chart(fig, use_container_width=True)
           
    elif sb == "Model 05 - Silva":          # Silva
        name = "M05"
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
            st.success("Carbonation depth: " + str(round(Modell05.x_c(t),1)) + " mm")
            t_range = np.arange(0, t, 0.1)
            fig1, ax1 = plt.subplots()
            ax1.grid(True)
            ax1.set(xlabel = "Time (years)", ylabel = "Carbonation depth (mm)", title = sb)
            ax1.plot(t_range, Modell05.x_c(t_range))
            #plt.xscale("log")
            st.pyplot(fig1)    #oder: st.write(fig1)
            
    elif sb == "Model 06 - Yang":           # Yang
        st.subheader("leer")
        
    elif sb == "Model 07 - Hills":          # Hills
        st.subheader("leer")
        
    elif sb == "Model 08 - Greve-Dierfeld": # Geve-Dierfeld
        st.subheader("leer")
        
    elif sb == "Model 09 - Ta":             # Ta
        st.subheader("leer")
        
    elif sb == "Model 10 - Ekolu":          # Ekolu
        st.subheader("leer")

    elif sb == "Model 11 - Possan":         # Possan
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
