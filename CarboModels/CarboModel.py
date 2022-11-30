# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 16:05:10 2021

@author: gf5901
"""
import numpy as np
import pandas as pd
import plotly.express as pex
import streamlit as st

class CarboModel:
    """
    This is the standart Carbonation model.
    Variables:
    name = name of input data set (string)
    """
    def __init__(self, name):
        self.name = name
        
    def k(self,t):
        """
        returns carbonation coefficent k, which gets calculated in __init__ function
        Returns
        -------
        k(mm/year^0.5)
            carbonation coefficent 

        """
        return float(self.karbo)


    def x_c(self, t):
        """
        calculates one Carbonation depth for given time t 
        Parameters
        ----------
        t(years): TYPE
            Time

        Returns
        -------
        x_c(mm) : TYPE
            cabonation depth
        """
        x_c = self.karbo * t**0.5
        return x_c
    
    def x_cList(self, t):
        """
        calculates Carbonation depth for time serie

        Parameters
        ----------
        t(years): List
            Time

        Returns
        -------
        x_c(mm) : List with x.xx 
            cabonation depth
        """
        t = int(t)
        x_c = []
        for i in range(0,t+1):
            x_c.append(round(self.k(i)* i**0.5, 2))
        return x_c
    
    def calculate(self, t):
        """
        

        Parameters
        ----------
        t : float
            time (years)

        Methods
        -------
        Shows carbonation depth, k-factor, table and chart of calculated carbonation depths (with download options)

        """
        
        st.success("Carbonation depth: " + str(round(self.x_c(t),1)) + " mm")
        st.success("k =" + str(round(self.karbo,2)) + " mm/year^0.5")
        
        t_range = np.arange(0,t+1)
        xc_list = self.x_cList(t)
        res = {"time [years]":t_range, "X(t) [mm]":xc_list}
        #Table:
        st.dataframe(res, use_container_width=True)
        res1=pd.DataFrame(res)
        st.download_button(("Download table"), res1.to_csv(sep=",", index=False, decimal=".", header=self.name), file_name=("CarbonationDepth.csv"))
        #Chart:
        fig = pex.line(res, y="X(t) [mm]", x="time [years]", title=(self.name))
        st.plotly_chart(fig, use_container_width=True)
        
        
        
        
        
        
        
        
        
        
        
        