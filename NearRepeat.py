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


class NearRepeat(Agent):


    def __init__(self, unique_id, model):

        super().__init__(unique_id, model)
        self.countdown = 1
        self.recently = 0
        self.today = 0
        ###########
        self.thiefs_arrested = 0
        self.numcrimes = 0
        self.rob_times = 0
        self.type = "NearRepeat"
        ###########

    def step(self):
        if self.recently == 1:
            if self.countdown == 2:
                self.today = 0
            self.countdown += 1
            if self.countdown == 7:
                self.countdown = 1
                self.recently = 0