# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:15:54 2021

@author: Jhoss
"""

acl = int (input("Ingrese el # de ACL "))
if acl >=1 and acl<=99:
    print("es una ACL estándar")
elif acl >=100 and acl<=199:
    print("es una ACL extendida")
else:
     print("No es un # de ACL válido")

try:
    print('es para un error')
except:
    print("manda mensajes de error")