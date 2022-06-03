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
import pandas as pd
from Victim import Victim
from Thief import Thief
from Thief import Policeman
from CrimeModel import CrimeModel
from NearRepeat import NearRepeat
from Count import count
import matplotlib.pyplot as plt
import statistics

#Dia y noche
#Model(Thiefs,Victims,Policemen,Width,Height)
T = 9
V = 225
P = 9
W = 10
H = 20

Dias = 100
crimenes_dia = []
arrestos_dia = []

for j in range(Dias):
    x_pos = []
    y_pos = []
    x_arrest = []
    y_arrest = []
    #Dia
    model = CrimeModel(T,V,P,W,H)
    for i in range(12):
        model.step()
    x1 = len(x_pos)
    y1 = len(x_arrest)


    #Noche
    model = CrimeModel(T,V-200,P,W,H)
    for i in range(12):

        model.step()
    x2 = len(x_pos)
    y2 = len(x_arrest)
    
    crimenes_dia.append(x1+x2)
    arrestos_dia.append(y1+y2)
plt.plot(crimenes_dia)
plt.plot(arrestos_dia)

## Statistics ## 
print(statistics.mean(crimenes_dia))#5.20
print(round(np.std(crimenes_dia),2))

print(statistics.mean(arrestos_dia))#1.02
print(round(np.std(arrestos_dia),2)) 