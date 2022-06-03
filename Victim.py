# -*- coding: utf-8 -*-
"""
Created on Tue May 24 17:28:00 2022

@author: xarta
"""
import mesa
import random
from mesa import Agent,Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from Movement import movement

class Victim(Agent):
    
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.numcrimes = 0
        self.rob_times = 0
        self.thiefs_arrested = 0
        self.today = 0
        self.type = "Victim"
        self.count = 0
        p1 = [0,0.1,0.3,0.5]
        self.clase = random.choices(p1,weights=[0.04,0.2,0.7,0.03],k=1)[0]
        #Movement parameters
        self.start = 0
        
    def move(self):
        
        self.model.grid.move_agent(self, movement(self.pos[0],self.pos[1],x_start=self.x_start,y_start=self.y_start,ida=self.ida,viajes=self.viajes,x=self.self_x,y=self.self_y)[0:2])
        self.ida = movement(self.pos[0],self.pos[1],x_start=self.x_start,y_start=self.y_start,ida=self.ida,viajes=self.viajes,x=self.self_x,y=self.self_y)[2]
        
        self.count = self.count + 1
        if self.count == 10:
            self.self_x = random.choice(range(0,10))
            self.self_y = random.choice(range(1,20))
            self.viajes = self.viajes -1        
        

    def step(self):
        self.move()