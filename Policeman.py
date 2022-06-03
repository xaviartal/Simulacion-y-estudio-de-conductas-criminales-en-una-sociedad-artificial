# -*- coding: utf-8 -*-
"""
Created on Tue May 24 17:28:05 2022

@author: xarta
"""
import mesa
import random
import numpy as np
from mesa import Agent,Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from NearRepeat import NearRepeat
from Thief import Thief

x_pos = []
y_pos = []
x_arrest = []
y_arrest = []

class Policeman(Agent):
    def __init__(self,unique_id,model):
        super().__init__(unique_id, model)
        self.thiefs_arrested = 0
        self.numcrimes = 0
        self.rob_times = 0
        self.today = 0
        self.type = "Police"
        
        
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
        
    def arrest(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=True
        )
        for cell in possible_steps:
            cell = self.model.grid.get_cell_list_contents(cell)
            nr_l = [obj for obj in cell if isinstance(obj, NearRepeat)]
            nr = random.choice(nr_l)
            if nr.today == 1:
                search = nr.model.grid.get_neighborhood(
                    nr.pos, moore=True, include_center=True
                )
                for s in search:
                    s1 =self.model.grid.get_cell_list_contents(s)
                    Thiefs = [obj1 for obj1 in s1 if isinstance(obj1, Thief)]
                
                    if len(Thiefs) > 0 and round(np.random.uniform(0,1),3)> 0.95:
                        thief_to_arrest = random.choice(Thiefs)
                        self.model.grid._remove_agent(thief_to_arrest.pos, thief_to_arrest)
                        self.model.schedule.remove(thief_to_arrest)
                        x_arrest.append(self.pos[0])
                        y_arrest.append(self.pos[1])
                        nr.ar = 1
                        break
            
    def step(self):
        self.arrest()
        self.move()