# -*- coding: utf-8 -*-
"""
Created on Tue May 24 17:28:04 2022

@author: xarta
"""
import mesa
import random
import numpy as np
from Movement import movement
from mesa import Agent,Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from NearRepeat import NearRepeat
from Victim import Victim



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


class Thief(Agent):

    def __init__(self,unique_id,model):
        super().__init__(unique_id, model)
        self.thiefs_arrested = 0
        self.numcrimes = 0
        self.rob_times = 0
        self.today = 0
        self.dp = 0
        self.type = "Thief"
        
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
 
        
    def rob(self):
        x, y = self.pos
        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        
        NR_l = [obj for obj in this_cell if isinstance(obj, NearRepeat)]
        NR = random.choice(NR_l)
        
        #Police distance#
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False, radius=4
        )
        for cell in possible_steps:
            cell = self.model.grid.get_cell_list_contents(cell)
            police = [obj for obj in cell if isinstance(obj, Policeman)]
            
            if len(police) == 0:
                self.dp = 1
            else:
                self.dp = 0
                break
                
            
        Victims = [obj for obj in this_cell if isinstance(obj, Victim)]   
        
        if len(Victims) > 0:
            victim_to_steal = self.random.choice(Victims)
            S = victim_to_steal.clase
            Nr = round(NR.recently / NR.countdown,3)
            Esp = round(np.random.uniform(0,0.5),3)
            Dp = self.dp
            
            prob = (S+Nr+Esp+Dp)/17
            decision = random.choices([1,0],weights=[prob,1-prob])[0]
            
            
            if decision == 1:
                victim_to_steal.rob_times+=1
                self.numcrimes+=1
                NR.recently = 1
                NR.today = 1
                NR.countdown = 1
################Data collection automatic######################################################################################
                x_pos.append(self.pos[0])
                y_pos.append(self.pos[1])
                
            


    def step(self):
        self.rob()
        self.move()
