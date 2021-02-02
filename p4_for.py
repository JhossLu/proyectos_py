# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:33:14 2021

@author: Jhoss
"""

lista=["R1", "R2","R3", 
       "S1", "S2","s3",
       "R4"," R5"]
for i in lista:
    if 'S' in i:
        print(i,end=' ')
    elif "R" in i:
        print(i,end=' ')
    else:
        print("no es un equipo de la red")