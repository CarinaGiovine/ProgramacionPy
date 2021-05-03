# -*- coding: utf-8 -*-
"""
Created on Sun May  2 23:40:22 2021

@author: CarinaGiovine
"""

'''Ejercicio que carga productos, muestra el listado una vez finalizada la carga y lista los productos con stock cero'''

class Producto:
    
    def __init__(self):
    
        self.productos={}  #diccionario que almacena los productos, la clave es el codigo y en una tupla se carga el precio, stock y descripcion
        self.codigo=0
        self.descripcion=' '
        self.precio=0
        self.stock=0
         
    
    def cargar(self):
        continua="s"
        while continua=="s":
            self.codigo=int(input("Ingrese el codigo del producto:"))
            self.descripcion=input("Ingrese la descripcion:")
            self.precio=float(input("Ingrese el precio:"))
            self.stock=int(input("Ingrese el stock actual:"))
            self.productos[self.codigo]=(self.descripcion,self.precio,self.stock)
            continua=input("Desea cargar otro producto[s/n]?")


    def listado_de_productos(self):
        print("Listado completo de productos:")
        for self.codigo in self.productos:
            print(self.codigo,self.productos[self.codigo][0],self.productos[self.codigo][1],self.productos[self.codigo][2])
        print (self.productos)  # muestro el diccionario con los datos que ingrese
        
    
    def listado_stock_cero(self):
        print("Listado de articulos con stock en cero:")
        for self.codigo in self.productos:
            if self.productos[self.codigo][2]==0:
                print(self.codigo,self.productos[self.codigo][0],self.productos[self.codigo][1],self.productos[self.codigo][2])
                
                
p=Producto()
p.cargar()
p.listado_de_productos()
p.listado_stock_cero()