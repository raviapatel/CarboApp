# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 21:27:30 2022

@author: marco
"""

import streamlit as st
import plotly.express as pex
import pandas as pd
from dataclasses import dataclass
from CarboModels import Häkkinen             #Modell01
from CarboModels import fib                  #Modell02.1
from CarboModels import fibGuiglia           #Modell02.2
from CarboModels import CECS220              #Modell03
from CarboModels import Guiglia              #Modell04
from CarboModels import Silva                #Modell05
from CarboModels import Yang                 #Modell06
from CarboModels import Hills_time           #Modell07.1
from CarboModels import Hills_fc             #Modell07.2
from CarboModels import fibGreveDierfeld     #Modell08
from CarboModels import Ta                   #Modell09
from CarboModels import Ekolu                #Modell10
from CarboModels import Possan               #Modell11

@dataclass
class app_Compare():
    
    def __post_init__(self):
        st.subheader("Choose Models to Compare:")
        compare = st.multiselect("Choose Models:", ("Model 01", "Model 02", "Model 03", "Model 04", "Model 05", "Model 06", "Model 07", "Model 08", "Model 09", "Model 10", "Model 11"), label_visibility="collapsed")
        col1, col2 = st.columns([1,1])
     
        if "Model 02" in compare or "Model 03" in compare or "Model 04" in compare or "Model 05" in compare or "Model 06" in compare or "Model 08" in compare or "Model 09" in compare or "Model 10" in compare or "Model 11" in compare: 
            with col1:
                RH = st.number_input("RH:")
        if "Model 01" in compare or "Model 05" in compare or "Model 06" in compare or "Model 08" in compare or "Model 09" in compare or "Model 11" in compare: 
            with col2:
                C = st.number_input("Clinker Content: (kg/m³)", key=("compare_C"), value=(200.0), step=(0.5))
        if "Model 01" in compare or "Model 03" in compare or "Model 06" in compare or "Model 08" in compare or "Model 09" in compare or "Model 11" in compare:
            with col2:
                FA = st.number_input("FA:")
        if "Model 01" in compare or "Model 06" in compare or "Model 08" in compare or "Model 11" in compare:
            with col2:
                SF = st.number_input("SF:")
        if "Model 01" in compare or "Model 06" in compare or "Model 08" in compare: 
            with col2:
                GGBS = st.number_input("GGBS:")
        if "Model 02" in compare or "Model 03" in compare or "Model 05" in compare or "Model 06" in compare or "Model 08" in compare or "Model 09" in compare or "Model 10" in compare or "Model 11" in compare:
            with col1:
                CO2 = st.number_input("CO2:")
        if "Model 06" in compare or "Model 09" in compare: 
            with col2:
                S = st.number_input("S:")
        if "Model 06" in compare or "Model 09" in compare: 
            with col2:
                G = st.number_input("G:")
        if "Model 01" in compare or "Model 03" in compare or "Model 06" in compare or "Model 07" in compare or "Model 10" in compare or "Model 11" in compare:
            with col1: 
                ExCo = st.radio("Choose Exosure condition:", ["Outdoor","Indoor","Exposed","Sheltered"])
        if "Model 02" in compare or "Model 07" in compare or "Model 08" in compare or "Model 09" in compare:
            with col1:
                t_c = st.number_input("t_c:")
        if "Model 02" in compare or "Model 08" in compare:
            with col1:
                p_dr = st.number_input("p_dr:")
        if "Model 02" in compare or "Model 08" in compare:
            with col1:
                ToW = st.number_input("ToW:")
        if "Model 02" in compare:
            with col2:
                choose = st.radio("Choose:", ["Set R_NAC1", "Calculate with f_c"])
        if "Model 02" in compare and choose=="Set R_NAC1":
            with col2:
                R_NAC1 = st.number_input("R_NAC1")
        if "Model 01" in compare or ("Model 02" in compare and choose=="Calculate with f_c") or "Model 03" in compare or "Model 04" in compare or "Model 05" in compare or "Model 06" in compare or "Model 07" in compare or "Model 09" in compare or "Model 10" in compare or "Model 11" in compare: 
            with col2:
                f_c = st.number_input("f_c:")
        if "Model 03" in compare:
            with col1: 
                Stress = st.radio("Stress:", ["Pressure", "Tension"])
        if "Model 03" in compare or "Model 09" in compare:
            with col1: 
                T = st.number_input("T:")
        if "Model 03" in compare:
            with col2: 
                Location = st.radio("Location:",["Corner", "Other Area"])
        if "Model 04" in compare:
            with col2:
                Building = st.selectbox("Building type:", ("Tunnel","Others"))
        if "Model 05" in compare:
            with col1: 
                ExpC = st.selectbox("Exposure class:", ("XC1","XC2","XC3","XC4")) 
        if "Model 01" in compare:
            with col2: 
                AirEntrained = st.radio("Choose if component is air entrained:", ["Air entrained","Not air entrained"])
        if "Model 06" in compare:
            with col1:
                if ExCo =="Outdoor":     Finishing = st.radio("Choose Finishing of component:", ["Nothing", "Plaster", "Paint", "Mortar", "Mortar + Plaster", "Mortar + Paint", "Tile"])
                elif ExCo =="Indoor":    Finishing = st.radio("Choose Finishing of component:", ["Nothing", "Paint", "Mortar", "Tile"])
                else:
                    Finishing = "None"
        if "Model 06" in compare or "Model 09" in compare:
            with col2:
                wc = st.number_input("wc:")
        if "Model 07" in compare: 
            with col2: 
                Mixture = st.radio("Choose content in the concrete:",["ordinary portland cement (OPC)","OPC + blast furnace slag","OPC + fly ash"])
                Depending = st.radio("Model Depending on...", ["Time", "Compressive Strength"])
        if "Model 07" in compare and Depending == "Time":
            with col1:
                Origin = st.radio("Choose origin:",["Experimental", "Structural"])
        if "Model 08" in compare:
            with col1:
                wb = st.number_input("wb:")
        if "Model 09" in compare:
            with col2:
                W = st.number_input("W:")
        if "Model 10" in compare:
            with col1: 
                CEM = st.radio("Choose Cement type:", ["Unknown", "CEM I", "CEM II/A-L", "CEM II/A-S", "CEM II/B-S", "CEM III/A", "CEM IV/A", "CEM IV/B"])
        if "Model 08" in compare:
            with col2:
                L = st.number_input("L:")
                PZ = st.number_input("PZ:")
        if "Model 09" in compare:
            with col2:
                CaO = st.number_input("Amount of Calcium Oxide per Weight of Cement: (-)", value=(0.0), step=(0.5))
                SO3 = st.number_input("Amount of Sulfur Oxide per Weight of Cement: (-)", value=(0.0), step=(0.5))
                SiO2 = st.number_input("Amount of Silicon Oxide per Weight of Cement: (-)", value=(0.0), step=(0.5))
                Al2O3 = st.number_input("Amount of Aluminium Oxide per Weight of Cement: (-)", value=(0.0), step=(0.5))
                Fe2O3 = st.number_input("Amount of Iron Oxide per Weight of Cement: (-)", value=(0.0), step=(0.5))
                p_c = st.number_input("Density of Cement: (kg/m³)", value=(0.0), step=(0.5))
                p_FA = st.number_input("Density of Fly Ash: (kg/m³)", value=(0.0), step=(0.5))
                p_w = st.number_input("Density of Water: (kg/m³)", value=(0.0), step=(0.5))
                phi_clinker = st.number_input("Cement Clinker Content: (-)", value=(0.0), step=(0.5))
                f_cem = st.number_input("fcm ? : (MPa)", value=(0.0), step=(0.5))
                S_max = st.number_input("Maximum aggregate size: (mm)", value=(0.0), step=(0.5))
        if "Model 10" in compare:
            with col1:
                FA_c = st.number_input("FA_c:")
                GGBS_c = st.number_input("GGBS_c:")
            

        t = st.number_input("Time:")
        
        if st.button("Calculate", key=("compare_button")):
            data = {"Model":[],"Carbonation Depth [mm]":[]}
            if "Model 01" in compare:
                Model01 = Häkkinen("Model 01", C, f_c, ExCo, AirEntrained, FA, SF, GGBS)
                if Model01.karbo=="NaN":
                    st.warning("Model 01 incompatible with input values!")
                else:
                    data["Model"].append(Model01.name)
                    data["Carbonation Depth [mm]"].append(Model01.x_c(t))            
            if "Model 02" in compare:
                Model02 = fib("Model 01", RH, ToW, p_dr, t_c, R_NAC1, CO2)
                Model02 = fibGuiglia("Model 02", RH, ToW, p_dr, t_c, f_c, CO2)
                if Model02.karbo=="NaN":
                    st.warning("Model 02 incompatible with input values!")
                else:
                    data["Model"].append(Model02.name)
                    data["Carbonation Depth [mm]"].append(Model02.x_c(t))
            if "Model 03" in compare:
                Model03 = CECS220("Model 03", f_c, FA, Stress, Location, T, RH, CO2)
                if Model03.karbo=="NaN":
                    st.warning("Model 03 incompatible with input values!")
                else:
                    data["Model"].append(Model03.name)
                    data["Carbonation Depth [mm]"].append(Model03.x_c(t))
            if "Model 04" in compare:
                Model04 = Guiglia("Model 04", f_c, RH, Building)
                if Model04.karbo=="NaN":
                    st.warning("Model 04 incompatible with input values!")
                else:
                    data["Model"].append(Model04.name)
                    data["Carbonation Depth [mm]"].append(Model04.x_c(t))
            if "Model 05" in compare:
                Model05 = Silva("Model 05", C, f_c, ExpC, RH, CO2)
                if Model05.karbo=="NaN":
                    st.warning("Model 05 incompatible with input values!")
                else:
                    data["Model"].append(Model05.name)
                    data["Carbonation Depth [mm]"].append(Model05.x_c(t))
            if "Model 06" in compare:
                Model06 = Yang("Model 06", t, C, S, G, FA, GGBS, SF, wc, RH, CO2, Location, Finishing)
                if Model06.karbo=="NaN":
                   st.warning("Model 06 incompatible with input values!")
                else:
                   data["Model"].append(Model06.name)
                   data["Carbonation Depth [mm]"].append(Model06.x_c(t))
            if "Model 07" in compare and Depending == "Time":
                Model07_1 = Hills_time("Model 07", Mixture, ExCo, Origin, t_c)
                if Model07_1.karbo=="NaN":
                    st.warning("Model 07 incompatible with input values!")
                else:
                    data["Model"].append(Model07_1.name)
                    data["Carbonation Depth [mm]"].append(Model07_1.x_c(t))
            if "Model 07" in compare and Depending == "Compressive Strength":
                Model07_2 = Hills_fc("Model 07", Mixture, ExCo, f_c)
                if Model07_2.karbo=="NaN":
                    st.warning("Model 07 incompatible with input values!")
                else:
                    data["Model"].append(Model07_2.name)
                    data["Carbonation Depth [mm]"].append(Model07_2.x_c(t))
            if "Model 08" in compare:
                Model08 = fibGreveDierfeld("Model 08", RH, CEM, C, FA, SF, GGBS, L, PZ, wb, CO2, ToW, p_dr, t_c)
                if Model08.karbo=="NaN":
                    st.warning("Model 08 incompatible with input values!")
                else:
                    data["Model"].append(Model08.name)
                    data["Carbonation Depth [mm]"].append(Model08.x_c(t))
            if "Model 09" in compare:
                Model09 = Ta("Model 09", C, p_c, wc, FA, p_FA, S, G, W, p_w, CaO, SO3, SiO2, Al2O3, Fe2O3, phi_clinker, S_max, f_cem, t_c, RH, T, CO2)
                if Model09.karbo=="NaN":
                    st.warning("Model 09 incompatible with input values!")
                else:
                    data["Model"].append(Model09.name)
                    data["Carbonation Depth [mm]"].append(Model09.x_c(t))
            if "Model 10" in compare: 
                Model10 = Ekolu("Model 10", f_c, RH, CO2, FA_c, GGBS_c, ExCo)
                if Model10.karbo=="NaN":
                    st.warning("Model 10 incompatible with input values!")
                else:
                    data["Model"].append(Model10.name)
                    data["Carbonation Depth [mm]"].append(Model10.x_c(t))
            if "Model 11" in compare:
                Model11 = Possan("Model 11", C, FA, SF, CEM, f_c, ExCo, CO2, RH)
                if Model11.karbo=="NaN":
                    st.warning("Model 11 incompatible with input values!")
                else:
                    data["Model"].append(Model11.name)
                    data["Carbonation Depth [mm]"].append(Model11.x_c(t))
            
            #Bar chart:       
            fig = pex.bar(data, x="Model", y="Carbonation Depth [mm]")
            #data_new=sum(data)/len(data)
            #fig.add_line(x="Model", y=data_new, name="Average")
            st.plotly_chart(fig, use_container_width=True)
            #Table:
            st.dataframe(data, use_container_width=True)
            res1=pd.DataFrame(data)
            st.download_button(("Download table"), res1.to_csv(sep=",", index=False, decimal=".", header="Compare Models"), file_name=("CompareCarbonationDepth.csv"))
            
        
        