# -*- coding: utf-8 -*-
"""
Created on Tue May 24 17:28:07 2022

@author: xarta
"""
def count(model):
    n_crimes = 0
    crimes_report = [agent.today for agent in model.schedule.agents]
    
    for x in crimes_report:
        if x == 1:
            n_crimes +=1
    return n_crimes

