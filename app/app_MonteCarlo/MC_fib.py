# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 11:43:35 2022

@author: marco
"""
import streamlit as st
import numpy as np
from scipy.stats import beta
from dataclasses import dataclass
from CarboModels.fib import fib
from CarboModels.fibGuiglia import fibGuiglia


@dataclass
class MC_fib():
    
    def __post_init__(self):
        
        col1, col2 = st.columns([1,1])
        with col1: 
            RH = st.number_input("Mean Relative Air Humidity: [%]", min_value=(2.0), max_value=(98.0), value=(70.0), step=(0.5), key="MC_Yang_07")
            CO2 = st.number_input("CO2 Density around Concrete Surface: [%]", min_value=(0.0), max_value=(100.0), value=(0.04), step=(0.005), format=("%.4f"), key="MC_fib_02")
            t_c = st.number_input("Curing Time: [days]", min_value=(0), value=(3), step=(1), key="MC_fib_03")
            p_dr = st.number_input("Probability of Driving Rain: [%]", min_value=(0.0), max_value=(100.0), value=(30.0), step=(0.5), key="MC_fib_04")

        with col2: 
            ToW = st.number_input("Average Number of Rainy Days per Year [days]", min_value=(0.0), max_value=(365.0), value=(130.0), key="MC_fib_05")
            choose = st.radio("Choose:",["Set Inverse Effective Carbonation Resistance", "Calculalte with Compressive Strenght"], key="MC_fib_06")
            
            if choose == "Set Inverse Effective Carbonation Resistance":
                R_NAC = st.number_input("Inverse Effective Carbonation Resistance (NAC): [(mm²/year)/(kg/m³)]", min_value=(0.0), value=(8000.0), step=(0.5), key="MC_fib_07")
            else:
                f_c = st.number_input("Mean Concrete Compressive Strenght: [MPa]", min_value=(1.0), max_value=(100.0), value=(30.0), step=(0.5), key="MC_fib_08")

        t = st.number_input("Service Time: [years]", min_value=(1), max_value=(100), value=(50), step=(1), key="MC_fib_09")
        c_nom = st.number_input("Concrete Cover: [mm]",  min_value=(0.0), value=(20.0), step=(0.5), key="MC_fib_10")
        sample_total = st.number_input("Total of Samples: [-]", min_value=(1), value=(1000), step=(100), key="MC_fib_11")

        if choose == "Set Inverse Effective Carbonation Resistance":
            if st.button("Calculate", key="MC_fib_12"): 
                # Distribution of CO2 (Normal):
                CO2 = 0.0409*CO2*44.01/100                          # [%]->[kg/m³]
                CO2_p=np.random.normal(CO2, 0.0001, sample_total)   # [kg/m³]
                CO2_p=(100*CO2_p)/(44.01*0.0409)                    # [kg/m³]->[%]
                # Distribution of RH (Beta):
                m=RH; s=12.9; a=0; b=100; var=s**2                      #m=Mittelwert, s=Standardabweichung, a=Min, b=Max, var=Varianz
                alpha_input = ((a-m)*(a*b-a*m-b*m+m**2+var))/(var*(b-a))
                beta_input = -((b-m)*(a*b-a*m-b*m+m**2+var))/(var*(b-a))
                RH_p = beta.rvs(alpha_input, beta_input, scale=b-a, loc=a, size=sample_total)
                #Distribution of b_c (Normal):
                b_c_p=np.random.normal(-0.567, 0.024, sample_total) 
                #Distribution of b_w (Normal):
                b_w_p=np.random.normal(0.446, 0.163, sample_total)   

                X=[]
                bar=st.progress(0)
                for i in range(0,sample_total):
                    bar.progress((1+i)/sample_total)
                    Calc_MC = fib(i, RH_p[i], ToW, p_dr, t_c, R_NAC, CO2_p[i], t, b_c=b_c_p[i], b_w=b_w_p[i])
                    X.append(Calc_MC)
                Calc_MC.histogram(X, t, c_nom, sample_total)

        else:
            if st.button("Calculate", key="MC_fib_13"):
                # Distribution of CO2 (Normal):
                CO2 = 0.0409*CO2*44.01/100                          # [%]->[kg/m³]
                CO2_p=np.random.normal(CO2, 0.0001, sample_total)   # [kg/m³]
                CO2_p=(100*CO2_p)/(44.01*0.0409)                    # [kg/m³]->[%]
                # Distribution of RH (Beta):
                m=RH; s=12.9; a=0; b=100; var=s**2                      #m=Mittelwert, s=Standardabweichung, a=Min, b=Max, var=Varianz
                alpha_input = ((a-m)*(a*b-a*m-b*m+m**2+var))/(var*(b-a))
                beta_input = -((b-m)*(a*b-a*m-b*m+m**2+var))/(var*(b-a))
                RH_p = beta.rvs(alpha_input, beta_input, scale=b-a, loc=a, size=sample_total)
                #Distribution of b_c (Normal):
                b_c_p=np.random.normal(-0.567, 0.024, sample_total) 
                #Distribution of b_w (Normal):
                b_w_p=np.random.normal(0.446, 0.163, sample_total)                   

                X=[]
                bar=st.progress(0)
                for i in range(0,sample_total):
                    bar.progress((1+i)/sample_total)
                    Calc_MC = fibGuiglia(i, RH_p[i], ToW, p_dr, t_c, f_c, CO2_p[i], t, b_c=b_c_p[i], b_w=b_w_p[i])
                    X.append(Calc_MC)
                Calc_MC.histogram(X, t, c_nom, sample_total)

           
            #RH=weibull_max.rvs(1.9121868702795919, 100, 100-73.28635048229631, size = sample_total) #[%] Kann auch verteilt werden s. Gehlen st. 76 und 103 Weibull_max
          
            #p_sr=0.3 # Tabelle Gehlen st. 32 // Hamburg
            