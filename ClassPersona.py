# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 19:08:08 2021

@author: CarinaGiovine
"""


class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

   
    def avanza(self):
        print(self.nombre,':Ando caminando')


class Ciclista(Persona): #clase Ciclista hereda de Persona

    def __init__(self, nombre):
        super().__init__(nombre)


    def avanza(self):
        print(self.nombre,':Ando moviendome en mi bicicleta')



persona = Persona('David')
persona.avanza()
ciclista = Ciclista('Daniel')
ciclista.avanza()


    