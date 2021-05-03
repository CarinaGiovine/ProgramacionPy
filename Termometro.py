# -*- coding: utf-8 -*-
"""
Created on Mon May  3 18:53:29 2021

@author: Admins
"""

class Termometro():
    
    def __init__(self, nombre, temperatura):
        self.nombre=nombre
        self.temperatura=temperatura
        self.limite=38
        
    def comprobar_temperatura(self, nueva_temperatura):
        self.temperatura=nueva_temperatura
        if self.temperatura > self.limite:
            print(".·ALARMA·. La tempertura ingresada ",nueva_temperatura,", supera el límite, Dirigirse a guardia febril")
            
        else:
            print("La temperatura ingresada está dentro de los parámetros normales.")
            
t=Termometro("Puerta", 36)
t.comprobar_temperatura(38.1)
