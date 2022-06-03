# -*- coding: utf-8 -*-
"""
Created on Tue May 24 17:38:14 2022

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

def agent_portrayal(agent):
    if agent is None:
        return

    portrayal = {}

    if type(agent) is Victim:
        portrayal["Shape"] = "C:/Users/xarta/OneDrive/Escritorio/TFG/Agentes_png/Victim1.png"
        portrayal["scale"] = 1
        portrayal["Layer"] = 1
        portrayal["Color"] = "green"

    elif type(agent) is Policeman:
        portrayal["Shape"] = "C:/Users/xarta/OneDrive/Escritorio/TFG/Agentes_png/Policemen1.png"
        portrayal["scale"] = 0.5
        portrayal["Layer"] = 2
        portrayal["Color"] = "blue"

        

    elif type(agent) is Thief:
        portrayal["Shape"] = "C:/Users/xarta/OneDrive/Escritorio/TFG/Agentes_png/Thief1.png"        
        portrayal["scale"] = 0.4
        portrayal["Layer"] = 3
        portrayal["Color"] = "red"
        
    elif type(agent) is NearRepeat:
        portrayal["Shape"] = "circle"    
        portrayal["r"] = 1
        portrayal["Layer"] = 4        
        
        if agent.today == 1:
            portrayal["Color"] = "red"
        
#         elif agent.ar == 1:
#             portrayal["Color"] = "blue"
        
        elif agent.today == 0:
            portrayal["Color"] = "white"
       

    return portrayal

w=10
h=10
grid= CanvasGrid(agent_portrayal, w, h, w*50, h*50)

crimes_graph = ChartModule([{"Label":"Numero de robos", "Color":"Red"}],
                          data_collector_name = "datacollector")

########## Set parameters ####
number_thiefs = UserSettableParameter('slider' , 'Number of thiefs', 9 , 0 , 100 , 1)
number_victims = UserSettableParameter('slider' , 'Number of victims', 225 , 0 , 10 , 1)
number_policemen = UserSettableParameter('slider' , 'Number of policemen', 9 , 0 , 100 , 1)

server = ModularServer(CrimeModel,[grid,crimes_graph],"CrimeModel",{"T":number_thiefs, "V": number_victims, 
                                                                    "P":number_policemen, "width":w,"height":h})

server.port = 8548 #8521 default server

server.launch()
