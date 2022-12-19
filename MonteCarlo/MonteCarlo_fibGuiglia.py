# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 11:43:35 2022

@author: marco
"""
import streamlit as st
from dataclasses import dataclass
from CarboModels import fibGuiglia
import numpy as np
import plotly.express as pex
from scipy.stats import weibull_max 

@dataclass
class MC_fibGuiglia():
    
    RH:float 
    ToW:float 
    p_sr:float 
    t_c:float 
    f_c:float 
    C_co2:float 
    t:float 
    c_nom:float 
    sample_total:int 
    
    def __post_init__(self):
        
        #sample_total = 100000
        #RH=weibull_max.rvs(1.9121868702795919, 100, 100-73.28635048229631, size = sample_total) #[%] Kann auch verteilt werden s. Gehlen st. 76 und 104 Weibull_max
        # plt.hist(RH, bins=100)
        # plt.show()
        self.C_co2=np.random.normal(6.2e-4, 0.1e-3, self.sample_total) # [kg/m³]
      
        #p_sr=0.3 # Tabelle Gehlen st. 32 // Hamburg
        
        
        
        #inizialisierung des fib-model in sample_total varianten
        test=[]
        for i in range(0,self.sample_total):
            test1=fibGuiglia(i, self.RH, self.ToW, self.p_sr, self.t_c, self.f_c, float(self.C_co2[i]))
            test.append(test1)
        #fibGuiglia(name, RH, ToW, p_sr, t_c, f_c, C_co2)
        #print(test[1])
        #Wenn RH auch probalistisch: self.RH[i]
        
        #wie häuftig überschreitet die Karboantisierungstiefe y_c die betondeckung c_nom
        #t=50 #year
        #c_nom=30 #cm
        
        
        counter=0
        x_cList=[]
        for i in range(0,self.sample_total):
            x_cList.append(test[i].x_c(self.t))
            if test[i].x_c(self.t)>self.c_nom:
                counter=counter+1
                #print('fail')
        st.warning("Probability: " + str(round(counter/self.sample_total*100,2)) + "%")
        #Diagramm:
        #res1 = {"X(t) [mm]:":self.c_nom}
        res = {"X(t) [mm]":x_cList}
        fig = pex.histogram(res, x="X(t) [mm]")
        fig.add_vline(self.c_nom) #add_line(res1, x="X(t) [mm]")
        st.plotly_chart(fig)   
        #Tabelle:
        st.dataframe(res, use_container_width=True)
 
        
        #fig = plt.hist(x_cList, bins=100, label='calculated x_c')
        #st.pyplot(fig)
        
        #print('Probability of failiure:', counter/ self.sample_total*100)
        
        #fig = plt.hist(x_cList, bins=100, label='calculated x_c')
        #plt.vlines(self.c_nom, 0, 2000, 'r', label='c_nom')
        #plt.legend()
        #plt.show()
        