# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 16:05:10 2021

@author: gf5901
"""

#import math 

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
        x_c = self.k(t) * t**0.5
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
        x_c = []
        for i in t:
            x_c.append(round(self.k(i)* i**0.5, 2))
        return x_c