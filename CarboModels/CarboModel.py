# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import plotly.express as pex
import plotly.graph_objects as go
import streamlit as st
from scipy.stats import beta


class CarboModel():
    """
    This is the standard carbonation model.
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
        return self.karbo


    def x_c(self, t):
        """
        
        calculates carbonation depth for given time t 
        
        Parameters
        ----------
        t : float
            time [years]

        Returns
        -------
        x_c : float
            cabonation depth [mm]
            
        """
        x_c = self.k(t) * t**0.5
        return x_c
    
    def x_cList(self, t):
        """
        
        calculates Carbonation depth for time serie

        Parameters
        ----------
        t : list 
            time [years]

        Returns
        -------
        x_c : list 
            carbonation depth [mm]
            
        """
        t = int(t)
        x_c = []
        for i in range(1,t+1):
            x_c.append(round(self.k(i)* i**0.5, 2))
        return x_c
    
    def calculate(self, t):
        """
        
        Parameters
        ----------
        t : float
            time [years]

        Methods
        -------
        Shows carbonation depth, k-factor, table and chart of calculated carbonation depths (with download options)

        """
        # checks if nodel is compatible:
        if self.karbo=="NaN":
            st.warning(self.name + " incompatible with input values!")
        else:
            # output of x_c and k:
            st.latex("\sf Carbonation \, depth=" + str(round(self.x_c(t),1)) + " mm")
            st.latex("\sf k = " + str(round(self.k(t),2)) + "{mm \over {\sqrt{year}}}")
            
            #calculation of xc_list:
            t_range = np.arange(1,t+1)
            xc_list = self.x_cList(t)
            res = {"time [years]":t_range, "X(t) [mm]":xc_list}
            
            # generation and output of chart:
            fig = pex.line(res, y="X(t) [mm]", x="time [years]", title=(self.name))
            st.plotly_chart(fig, use_container_width=True)
            
            # generation and output of table, with download button:
            st.dataframe(res, use_container_width=True)
            res1=pd.DataFrame(res)
            st.download_button(("Download table"), res1.to_csv(sep=",", index=False, decimal=".", header=self.name), file_name=("CarbonationDepth.csv"))

    def histogram(self, X, t, c_nom, sample_total):
        """
        
        Parameters
        ----------
        X : object
            object of a model-class
        t : float
            time [years]
        c_nom : float
            concrete cover [mm]
        sample_total : int
            total of samples [-]

        Methods
        -------
        shows histogram and probability of depassivation (or warning if model is not calculateable)

        """
        # distribution of c_nom (Beta):
        m=c_nom; s=8; a=0; b=5*c_nom; var=s**2                      #m=mean value, s=standard deviation, a=minimum, b=maximum, var=variance
        alpha_input = ((a-m)*(a*b-a*m-b*m+m**2+var))/(var*(b-a))
        beta_input = -((b-m)*(a*b-a*m-b*m+m**2+var))/(var*(b-a))
        
        # checks if model is compatible;  counter for probability of depassivation:
        counter = 0    
        x_cList = []
        c_nom_p = []
        for i in range(0,sample_total):
            if X[i].karbo == "NaN":
                st.warning("Model not compatible with input values!")
                return
            else:
                c_nom_p.append(beta.rvs(alpha_input, beta_input, scale=b-a, loc=a))
                x_cList.append(X[i].x_c(t))
                if X[i].x_c(t)>c_nom_p[i]:
                    counter=counter+1

        # calculation and output of probability:
        st.warning("Probability of despassivation after " + str(t) + " years: " + str(round(counter/sample_total*100,2)) + "%")
        
        # generation of histograms:
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=x_cList, name="Carbonation Depth"))
        fig.add_trace(go.Histogram(x=c_nom_p, name="Concrete Cover"))
        
        # change Layout of histograms:
        fig.update_layout(barmode="overlay", xaxis_title_text="Depth [mm]", yaxis_title_text="Count")
        
        # calculate binsize: 
        bin_size_x = (max(x_cList)-min(x_cList))/20 
        bin_size_c = (max(c_nom_p)-min(c_nom_p))/20
        bin_size = round(min(bin_size_x, bin_size_c), 2)
        bin_size = max(bin_size, 0.5)                       # bin_size min. 0.5
        st.warning(bin_size)
        
        # reduce opacity to see both histograms and set binsize:
        fig.update_traces(opacity=0.75, xbins_size=bin_size)
        
        # add c_nom-line to histograms:
        fig.add_vline(c_nom, line_dash="dash", line_color="red")
        
        # show histogram:
        st.plotly_chart(fig)


        
        
        
        
        
        
        
        
        