# -*- coding: utf-8 -*-

import streamlit as st
import plotly.express as pex
import pandas as pd
import numpy as np
from dataclasses import dataclass
from CarboModels.Häkkinen import Häkkinen             #Modell01 - Häkkinen
from CarboModels.fib import fib                       #Modell02.1 - fib Model Code
from CarboModels.fibGuiglia import fibGuiglia         #Modell02.2 - fib Model Code (R_NAC nach Guiglia)
from CarboModels.CECS220 import CECS220               #Modell03 - CECS
from CarboModels.Guiglia import Guiglia               #Modell04 - Guiglia, Taliano
from CarboModels.Silva import Silva                   #Modell05 - Silva et al.
from CarboModels.Yang import Yang                     #Modell06 - Yang et al.
from CarboModels.Hills_time import Hills_time         #Modell07.1 - Hills et al. (time)
from CarboModels.Hills_fc import Hills_fc             #Modell07.2 - Hills et al. (compressive strength)
from CarboModels.GreveDierfeld import GreveDierfeld   #Modell08 - Greve-Dierfeld, Gehlen
from CarboModels.Ta import Ta                         #Modell09 - Ta et al.
from CarboModels.Ekolu import Ekolu                   #Modell10 - Ekolu
from CarboModels.Possan import Possan                 #Modell11 - Possan et al.

@dataclass
class Compare():
    
    def __post_init__(self):
        st.subheader("Choose Models to Compare:")
        compare = st.multiselect("Choose Models:", ("Häkkinen", "fib Model Code", "CECS", "Guiglia, Taliano", "Silva et al.", "Yang et al.", "Hills et al.", "Greve-Dierfeld, Gehlen", "Ta et al.", "Ekolu", "Possan et al."), label_visibility="collapsed")
        col1, col2 = st.columns([1,1])
     
        if "fib Model Code" in compare or "CECS" in compare or "Guiglia, Taliano" in compare or "Silva et al." in compare or "Yang et al." in compare or "Greve-Dierfeld, Gehlen" in compare or "Ta et al." in compare or "Ekolu" in compare or "Possan et al." in compare: 
            with col1:
                RH = st.number_input("Mean Relative Air Humidity: [%]", min_value=(0.0), max_value=(100.0), value=(70.0), step=(0.5), key="compare_01")
        if "Häkkinen" in compare or "Silva et al." in compare or "Yang et al." in compare or "Greve-Dierfeld, Gehlen" in compare or "Ta et al." in compare or "Possan et al." in compare: 
            with col2:
                C = st.number_input("Clinker Content: [kg/m³]", min_value=(0.0), value=(350.0), step=(5.0), key="compare_02")
        if "Häkkinen" in compare or "Yang et al." in compare or "Greve-Dierfeld, Gehlen" in compare or "Ta et al." in compare or "Possan et al." in compare:
            with col2:
                FA = st.number_input("Fly Ash Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0), key="compare_03")
        if "Häkkinen" in compare or "Yang et al." in compare or "Greve-Dierfeld, Gehlen" in compare or "Possan et al." in compare:
            with col2:
                SF = st.number_input("Silicia Fume Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0), key="compare_04")
        if "Häkkinen" in compare or "Yang et al." in compare or "Greve-Dierfeld, Gehlen" in compare: 
            with col2:
                GGBS = st.number_input("Blast Furnance Slag Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0), key="compare_05")
        if "fib Model Code" in compare or "CECS" in compare or "Silva et al." in compare or "Yang et al." in compare or "Greve-Dierfeld, Gehlen" in compare or "Ta et al." in compare or "Ekolu" in compare or "Possan et al." in compare:
            with col1:
                CO2 = st.number_input("CO2 Density around Concrete Surface: [%]", min_value=(0.0), max_value=(100.0), value=(0.04), step=(0.005), format=("%.4f"), key="compare_06")
        if "Yang et al." in compare or "Ta et al." in compare: 
            with col2:
                S = st.number_input("Sand Content: [kg/m³]", min_value=(0.0), value=(1000.0), step=(5.0), key="compare_07")
        if "Yang et al." in compare or "Ta et al." in compare: 
            with col2:
                G = st.number_input("Gravel Content: [kg/m³]", min_value=(0.0), value=(800.0), step=(5.0), key="compare_08")
        if "Häkkinen" in compare or "Yang et al." in compare or "Hills et al." in compare or "Ekolu" in compare or "Possan et al." in compare:
            with col1: 
                ExCo = st.radio("Choose Exposure Condition of Component:", ["Indoor", "Outdoor", "Exposed to Rain", "Sheltered from Rain"], key="compare_09")
        if "fib Model Code" in compare or "Greve-Dierfeld, Gehlen" in compare or "Ta et al." in compare:
            with col1:
                t_c = st.number_input("Curing Time: [days]", min_value=(0), value=(3), step=(1), key="compare_10")
        if "fib Model Code" in compare or "Greve-Dierfeld, Gehlen" in compare:
            with col1:
                p_dr = st.number_input("Probability of Driving Rain: [%]", min_value=(0.0), max_value=(100.0), value=(30.0), step=(0.5), key="compare_11")
        if "fib Model Code" in compare or "Greve-Dierfeld, Gehlen" in compare:
            with col1:
                ToW = st.number_input("Average Number of Rainy Days per Year [days]", min_value=(0.0), max_value=(365.0), value=(130.0), key="compare_12")
        if "fib Model Code" in compare:
            with col2:
                choose = st.radio("Choose:",["Set Inverse Effective Carbonation Resistance", "Calculate with Compressive Strenght"], key="compare_13")
        if "fib Model Code" in compare and choose=="Set Inverse Effective Carbonation Resistance":
            with col2:
                R_NAC = st.number_input("Inverse Effective Carbonation Resistance (NAC): [(mm²/years)/(kg/m³)]", min_value=(0.0), value=(8000.0), step=(0.5), key="compare_14")
        if "CECS" in compare:
            with col1: 
                Stress = st.radio("Choose Stress on Component:", ["Pressure", "Tension"], key="compare_15")
        if "CECS" in compare or "Ta et al." in compare:
            with col1: 
                T = st.number_input("Mean Temperature: [°C]", value=(15.0), step=(0.5), key="compare_16")
        if "CECS" in compare:
            with col2: 
                Location = st.radio("Choose Location of Component:", ["Corner", "Other Area"], key="compare_17")
        if "Guiglia, Taliano" in compare:
            with col1:
                Building = st.radio("Building Type:", ("Tunnel","Others"), key="compare_18")
        if "Silva et al." in compare:
            with col1: 
                ExpC = st.radio("Choose Exposure Class:", ("XC1","XC2","XC3","XC4"), key="compare_19") 
        if "Häkkinen" in compare:
            with col2: 
                AirEntrained = st.radio("Choose if Component is Air Entrained:", ["Air Entrained","Not Air Entrained"], key="compare_20")
        if "Yang et al." in compare:
            with col1:
                if ExCo =="Indoor": 
                    Finishing = st.radio("Choose Finishing of Component:", ["Nothing", "Paint", "Mortar", "Tile"], key="compare_21")
                else: 
                    Finishing = st.radio("Choose Finishing of Component:", ["Nothing", "Plaster", "Paint", "Mortar", "Mortar + Plaster", "Mortar + Paint", "Tile"], key="compare_22")
        if "Hills et al." in compare: 
            with col1: 
                mixture = st.radio("Choose Content in the Concrete:",["Ordinary Portland Cement (OPC)","OPC + Blast Furnace Slag","OPC + Fly Ash"], key="compare_24")
                Depending = st.radio("Model depending on...", ["Time","Compressive Strength"], key="compare_25")
        if "Häkkinen" in compare or ("fib Model Code" in compare and choose=="Calculate with Compressive Strenght") or "CECS" in compare or "Guiglia, Taliano" in compare or "Silva et al." in compare or "Yang et al." in compare or ("Hills et al." in compare and Depending=="Compressive Strength") or "Ta et al." in compare or "Ekolu" in compare or "Possan et al." in compare: 
            with col2:
                f_c = st.number_input("Mean Concrete Compressive Strenght: [MPa]", min_value=(1.0), max_value=(100.0), value=(30.0), step=(0.5), key="compare_26")
        if "Hills et al." in compare and Depending == "Time":
            with col1:
                Origin = st.radio("Choose Origin of Component:",["Experimental", "Structural"], key="compare_27")
                Age = st.number_input("Age of Concrete: [years] ", min_value=(0.0),value=(5.0), step=(0.5), key="compare_28")                
        if "Yang et al." in compare or "Greve-Dierfeld, Gehlen" in compare or "Ta et al." in compare :
            with col1:
                wb = st.number_input("Water / Binder Ratio: [-]", min_value=(0.0), value=(0.6), max_value=(1.0), step=(0.01), key="compare 29")
        if "Greve-Dierfeld, Gehlen" in compare or "Ekolu" in compare or "Possan et al." in compare:
            with col1: 
                Cem = st.radio("Choose Cement Type:", ["CEM I", "CEM II/A","CEM II/A-L", "CEM II/A-S", "CEM II/B", "CEM II/B-S", "CEM III/A", "CEM IV/A", "CEM IV/B"], key="compare_30")
        if "Ta et al." in compare:
            with col2:
                W = st.number_input("Water Content: [kg/m³]", min_value=(0.0), value=(280.0), step=(5.0), key="compare_31")
                CaO = st.number_input("Amount of Calcium Oxide per Weight of Cement: [-]", min_value=(0.0), max_value=(1.0), value=(0.645), step=(0.01), format=("%.4f"), key="compare_32")
                SO3 = st.number_input("Amount of Sulfur Oxide per Weight of Cement: [-]", min_value=(0.0), max_value=(1.0), value=(0.035), step=(0.01), format=("%.4f"), key="compare_33")
                SiO2 = st.number_input("Amount of Silicon Oxide per Weight of Cement: [-]", min_value=(0.0), max_value=(1.0), value=(0.205), step=(0.01), format=("%.4f"), key="compare_34")
                Al2O3 = st.number_input("Amount of Aluminium Oxide per Weight of Cement: [-]", min_value=(0.0), max_value=(1.0), value=(0.045), step=(0.01), format=("%.4f"), key="compare_35")
                Fe2O3 = st.number_input("Amount of Iron Oxide per Weight of Cement: [-]", min_value=(0.0), max_value=(1.0), value=(0.030), step=(0.01), format=("%.4f"), key="compare_36")
                p_c = st.number_input("Density of Cement: [kg/m³]", value=(3140.0), min_value=(0.0), step=(0.5), key="compare_37")
                p_FA = st.number_input("Density of Fly Ash: [kg/m³]", value=(2580.0), min_value=(0.0), step=(0.5), key="compare_38")
                p_w = st.number_input("Density of Water: [kg/m³]", value=(1000.0), min_value=(0.0), step=(0.5), key="compare_39")
                phi_clinker = st.number_input("Cement Clinker Content: [-]",min_value=(0.0), value=(1.0), max_value=(1.0), step=(0.01), key="compare_40")
                f_cem = st.number_input("Mean Cement Compressive Strenght: [N/mm²]",  min_value=(0.0), value=(42.5), max_value=(60.0), step=(0.5), key="compare_41")
                S_max = st.number_input("Maximum Aggregate Size: [mm]", min_value=(8.0), value=(16.0), max_value=(31.5), step=(0.5), key="compare_42")
        if "CECS" in compare:
            with col2:
                FA_c = st.number_input("Fly Ash Content: [weight ratio]", min_value=(0.0), value=(0.0), max_value=(1.0), step=(0.01), key="compare_43")

        t = st.number_input("Service Time: [years]", min_value=(1), max_value=(100), value=(50), step=(1), key="compare_44")
        
        if st.button("Calculate", key=("compare_button")):
            data = {"Model":[],"Carbonation Depth [mm]":[]}
            if "Häkkinen" in compare:
                Model01 = Häkkinen("Häkkinen", f_c, ExCo, AirEntrained, C, FA, SF, GGBS)
                if Model01.karbo=="NaN":
                    st.warning("Model 'Häkkinen' incompatible with input values!")
                else:
                    data["Model"].append(Model01.name)
                    data["Carbonation Depth [mm]"].append(round(Model01.x_c(t),2))            
            if "fib Model Code" in compare and choose=="Set Inverse Effective Carbonation Resistance":
                Model02_1 = fib("fib Model Code", RH, ToW, p_dr, t_c, R_NAC, CO2, t)
                if Model02_1.karbo=="NaN":
                    st.warning("fib Model Code incompatible with input values!")
                else:
                    data["Model"].append(Model02_1.name)
                    data["Carbonation Depth [mm]"].append(round(Model02_1.x_c(t),2))           
            if "fib Model Code" in compare and choose=="Calculate with Compressive Strenght":
                Model02_2 = fibGuiglia("fib Model Code", RH, ToW, p_dr, t_c, f_c, CO2, t)
                if Model02_2.karbo=="NaN":
                    st.warning("fib Model Code incompatible with input values!")
                else:
                    data["Model"].append(Model02_2.name)
                    data["Carbonation Depth [mm]"].append(round(Model02_2.x_c(t),2))
            if "CECS" in compare:
                Model03 = CECS220("CECS", f_c, FA_c, Stress, Location, T, RH, CO2)
                if Model03.karbo=="NaN":
                    st.warning("Model 'CECS' incompatible with input values!")
                else:
                    data["Model"].append(Model03.name)
                    data["Carbonation Depth [mm]"].append(round(Model03.x_c(t),2))
            if "Guiglia, Taliano" in compare:
                Model04 = Guiglia("Guiglia, Taliano", f_c, RH, Building)
                if Model04.karbo=="NaN":
                    st.warning("Model 'Guiglia, Taliano' incompatible with input values!")
                else:
                    data["Model"].append(Model04.name)
                    data["Carbonation Depth [mm]"].append(round(Model04.x_c(t),2))
            if "Silva et al." in compare:
                Model05 = Silva("Silva et al.", C, f_c, ExpC, RH, CO2)
                if Model05.karbo=="NaN":
                    st.warning("Model 'Silva et al.' incompatible with input values!")
                else:
                    data["Model"].append(Model05.name)
                    data["Carbonation Depth [mm]"].append(round(Model05.x_c(t),2))
            if "Yang et al." in compare:
                Model06 = Yang("Yang et al.", t, C, S, G, FA, GGBS, SF, wb, RH, CO2, ExCo, Finishing)
                if Model06.karbo=="NaN":
                   st.warning("Model 'Yang et al.' incompatible with input values!")
                else:
                   data["Model"].append(Model06.name)
                   data["Carbonation Depth [mm]"].append(round(Model06.x_c(t),2))
            if "Hills et al." in compare and Depending == "Time":
                Model07_1 = Hills_time("Hills et al.", mixture, ExCo, Origin, Age)
                if Model07_1.karbo=="NaN":
                    st.warning("Hills et al. incompatible with input values!")
                else:
                    data["Model"].append(Model07_1.name)
                    data["Carbonation Depth [mm]"].append(round(Model07_1.x_c(t),2))
            if "Hills et al." in compare and Depending == "Compressive Strength":
                Model07_2 = Hills_fc("Hills et al.", mixture, ExCo, f_c)
                if Model07_2.karbo=="NaN":
                    st.warning("Model 'Hills et al.' incompatible with input values!")
                else:
                    data["Model"].append(Model07_2.name)
                    data["Carbonation Depth [mm]"].append(round(Model07_2.x_c(t),2))
            if "Greve-Dierfeld, Gehlen" in compare:
                Model08 = GreveDierfeld("Greve-Dierfeld, Gehlen", RH, Cem, wb, CO2, ToW, p_dr, t_c)
                if Model08.karbo=="NaN":
                    st.warning("Model 'Greve-Dierfeld, Gehlen' incompatible with input values!")
                else:
                    data["Model"].append(Model08.name)
                    data["Carbonation Depth [mm]"].append(round(Model08.x_c(t),2))
            if "Ta et al." in compare:
                Model09 = Ta("Ta et al.", C, p_c, wb, FA, p_FA, S, G, W, p_w, CaO, SO3, SiO2, Al2O3, Fe2O3, phi_clinker, S_max, f_cem, t_c, RH, T, CO2)
                if Model09.karbo=="NaN":
                    st.warning("Model 'Ta et al.' incompatible with input values!")
                else:
                    data["Model"].append(Model09.name)
                    data["Carbonation Depth [mm]"].append(round(Model09.x_c(t),2))
            if "Ekolu" in compare: 
                Model10 = Ekolu("Ekolu", f_c, RH, CO2, Cem, ExCo, t)   
                if Model10.karbo=="NaN":
                    st.warning("Model 'Ekolu' incompatible with input values!")
                else:
                    data["Model"].append(Model10.name)
                    data["Carbonation Depth [mm]"].append(round(Model10.x_c(t),2))
            if "Possan et al." in compare:
                Model11 = Possan("Possan et al.", C, FA, SF, Cem, f_c, ExCo, CO2, RH)
                if Model11.karbo=="NaN":
                    st.warning("Model 'Possan et al.' incompatible with input values!")
                else:
                    data["Model"].append(Model11.name)
                    data["Carbonation Depth [mm]"].append(round(Model11.x_c(t),2))
            
            average = round(np.mean(data["Carbonation Depth [mm]"]),2)
            
            #Bar chart:       
            fig = pex.bar(data, x="Model", y="Carbonation Depth [mm]", color="Model")
            fig.add_hline(y=average, line_dash="dash", line_color="red")
            st.plotly_chart(fig, use_container_width=True)
            
            data["Model"].append("Average of Models")
            data["Carbonation Depth [mm]"].append(average)
            
            #Table:
            st.dataframe(data, use_container_width=True)
            res1=pd.DataFrame(data)
            st.download_button(("Download table"), res1.to_csv(sep=",", index=False, decimal=".", header="Compare Models"), file_name=("CompareCarbonationDepth.csv"))
            
        
        