# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 15:13:37 2021
nombre=input('Ingrese su Nombre:')
print('hola!', leer)
@author: Jhoss
"""
print("REGISTRO DE FACTURACIÓN","\n")
print(' Nombre:'+)
nombre=input()
print('Apellido:')
apellido=input()
print('RUC:')
ruc=input()
print('Ciudad:')
ciudad=input()
print('Fecha')
Fecha=input()
print("VERIFIQUE LOS DATOS","\n")
print("Nombre :" + nombre,"\n")
print("Apellido :" + apellido,"\n")
print("RUC :" + ruc,"\n")
print("Ciudad :" + ciudad,"\n")
print("Fecha :" + Fecha,"\n")
op=int(input("Escriba 1 para aceptar y guardar "))
if op==1:
    print("DATOS DE"+" "+nombre+" "+apellido+" GUARDADOS")
else:
    print("Error en datos")
    