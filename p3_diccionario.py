# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:16:39 2021

@author: Jhoss
"""
print('no se puede repetir datos, caso contrario se reemplazará el dato')
dict2={'R1':'10.0.0.1',
       1:'AP',
       2:2.5,3:True,
       'R1':'172.17.0.1' }
print(dict2)
print('\n')
dict1={'R1':'10.0.0.1',
       1:'AP',
       2:2.5,
       3:True}
print(dict1)
print(len(dict1))
print(type(dict1))
print(dict1[1])
print(dict1[2])
print(dict1[3])
print(dict1['R1'])
dict1['R3']='10.0.0.3'
print('R3' in dict1)
