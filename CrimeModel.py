# -*- coding: utf-8 -*-
"""
Created on Tue May 24 17:28:07 2022

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
from Victim import Victim
from Thief import Thief
from Policeman import Policeman
from NearRepeat import NearRepeat
from Count import count

class CrimeModel(Model):


    def __init__(self, T, V, P, width, height):
        self.num_thiefs = T
        self.num_victims = V
        self.num_policemen = P
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.current_id = 0
        self.running = True
    

        
        
        # Create agents
        
        ########## Victim ##############
        for i in range(self.num_victims):
            x = int(self.grid.width/2 + random.choice(range(-4,4)))
            y = int(self.grid.height/2 + random.choice(range(-4,4)))
            victim = Victim(self.next_id(), self)
            
            # Add the agent to a random grid cell
            self.grid.place_agent(victim, (x, y))
            victim.x_start = x
            victim.y_start = y
            victim.ida = 0
            victim.self_x = random.choice(range(5,15))
            victim.self_y = random.choice(range(5,15))
            victim.viajes=random.choice(range(1,5))
            self.schedule.add(victim)
            
        ######## Policeman ############
        for i in range(self.num_policemen):            
            x = self.grid.width - 2
            y = round(self.grid.height/2)
            policeman = Policeman(self.next_id(), self)
            
            # Add the agent to a random grid cell
            self.grid.place_agent(policeman, (x, y))
            self.schedule.add(policeman)
            
            
        ######## Thiefs ############## 
        for i in range(self.num_thiefs):
            r_ch = random.choice([0,0,0,0,0,0,-4,-3,-2,-1,1,2,3,4,5])
            x = round(self.grid.width/2) - random.choice(range(-4,0))
            y = round(self.grid.height/2) - random.choice(range(-2,2))
            thief = Thief(self.next_id(), self)
            
            # Add the agent to a random grid cell
            self.grid.place_agent(thief, (x, y))
            self.schedule.add(thief)
            
        ######### Near Repeat cells ############     
        for i in range(self.grid.width):
            
            for j in range(self.grid.height):
                
                near_repeat = NearRepeat(self.next_id(),self)
                self.grid.place_agent(near_repeat, (i, j))
                self.schedule.add(near_repeat)    
                
            
        
        ################ Data Collector ######################
        self.datacollector = DataCollector(
        model_reporters = {"Num crimes":count},
        agent_reporters = {})
    

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
    