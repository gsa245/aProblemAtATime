# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 09:22:36 2019

@author: IAMTHEBEST
"""

from pulp import LpProblem,LpMinimize,LpVariable,LpStatus

diet_model = LpProblem("Minimize Diet Cost",LpMinimize)

E = LpVariable('E',lowBound=5,upBound=12,cat='Integer')
C = LpVariable('C',lowBound=0,cat='Integer')
P = LpVariable('P',lowBound=0,cat='Integer')

diet_model+=5*E+30*C+45*P

diet_model +=6*E + 27*C + 23*P >=200
diet_model +=C+P<=5

diet_model.solve()
print(LpStatus[diet_model.status])

for v in diet_model.variables():
	print(v.name,"=",v.varValue)

