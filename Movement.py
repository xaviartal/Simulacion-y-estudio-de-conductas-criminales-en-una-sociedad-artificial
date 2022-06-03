# -*- coding: utf-8 -*-
"""
Created on Tue May 24 17:34:32 2022

@author: xarta
"""
import mesa
import random
import numpy as np
from mesa import Agent,Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from mesa.batchrunner import batch_run
import pandas as pd
from mesa.visualization.modules import CanvasGrid , ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
import seaborn as sns
from pylab import savefig

def movement(self_x,self_y,x_start,y_start,ida,x,y,viajes):


        #Llegada al objetivo
    if (y-self_y ==0) and (x-self_x == 0):
        ida = 1

        #Vuelta
        
    if ida == 1:
        if x_start-self_x !=0:
            x_new = self_x + (x_start-self_x)/abs(x_start-self_x)
            self_x = int(x_new)
        if y_start - self_y !=0:
            y_new = self_y + (y_start-self_y)/abs(y_start-self_y)
            self_y = int(y_new)
        
        #Llegada a casa
    if x_start-self_x ==0 and y_start - self_y ==0 and ida == 1:
        ida = 0
        
    if viajes != 0:
            
                
        #Ida
        if ida == 0:
            if x-self_x !=0:
                x_new = self_x + (x-self_x)/abs(x-self_x)
                self_x = int(x_new)
            if y-self_y !=0:
                y_new = self_y + (y-self_y)/abs(y-self_y)
                self_y = int(y_new)
    return(self_x,self_y,ida,viajes)