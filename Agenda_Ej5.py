# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:08:16 2021

@author: Carina
"""

class Agenda:
    
    def __init__(self):
        self.contactos={}  # creo un diccionario para almacenar los datos de la agenda
        
    def menu (self):
        opcion=0
        
        while opcion !=5:
            print("1- Cargar un contacto a la agenda")
            print("2- Mostrar datos de la agenda")
            print("3- Consultar ingresando nombre de la persona")
            print("4- Modificar datos: teléfono o mail")
            print("5- Finalizar el programa")
            opcion=int(input("Ingerese su opción: "))
            
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.mostrar()
            elif opcion==3:
                self.consultar()
            elif opcion==4:
                self.modificar()
            elif opcion==5:
                print("Gracias")
            else:
                print("Ingresaste una opción no válida. Vuelve a interntarlo")
                opcion=int(input("Ingrese su opción: "))
        
    def cargar(self):
        nombre=input("Ingrese el nombre de la persona: ")
        telefono=input("Ingrese el teléfono: ")
        mail=input("Ingrese el e-mail: ")
        self.contactos[nombre]=(telefono, mail)  #la clave del diccionario es el nombre y el valor es una tupla con los datos de telefono y mail
        
    def mostrar(self):
        print("Listado de la agenda")
        for nombre in self.contactos:
            print(nombre, self.contactos[nombre][0], self.contactos[nombre][1])   #recorro el diccionario y voy mostrando
            
    def consultar(self):
        nombre=input("Ingrese el nombre a consultar: ")
        if nombre in self.contactos:
            print(nombre, "su teléfono es ",self.contactos[nombre][0], "y su e-mail es ",self.contactos[nombre][1])
            
        else:
            print("No existe un contacto con dicho nombre.")
            
    def modificar(self):
        nombre=input("Ingrese el nombre de la persona a modificar teléfono y e-mail: ")
        if nombre in self.contactos:
            telefono=input("Ingrese el nuevo número de teléfono: ")
            mail=input("Ingrese el nuevo e-mail: ")
            self.contactos[nombre]=(telefono,mail)
        else:
            
            print("No existe un contacto con dicho nombre.")
            
    
agenda1=Agenda()
agenda1.menu()