# -*- coding: utf-8 -*-
"""
Created on Sat May  1 20:09:18 2021

@author: CarinaGiovine
"""

class Empleado():
    
    def __init__(self,cod,sueldo,valor_hora_extra,cantidad_h_e,casado,nro_hijos):
        self.codigo=cod
        self.sueldo_base=sueldo
        self.pago_hora_extra=valor_hora_extra
        self.cant_h_e=cantidad_h_e
        self.casado=casado   # 1 casado y 0 no
        self.nro_hijos=nro_hijos
        self.calculo=0
        self.retxhijos=0
        self.retxcasa=0
        self.neto=0
        
    def Calculo_Sueldo (self):
        #calculo=0
        self.calculo=self.sueldo_base + (self.cant_h_e * self.pago_hora_extra)
       
        
    def Calculo_Retenciones(self):  
        self.retxhijos=0.05 * self.nro_hijos #retenciones por hijo falta sumar las de casado
        if self.casado==1:
            self.retxcasa=0.05
            
       
        
    def Sueldo_Neto(self):
        
        self.neto= self.calculo - (self.calculo *(self.retxhijos + self.retxcasa))
            
            
            
    def Mostrar_Det (self):
        print("Sueldo Base para el empleado ", self.codigo, "es de: $",self.sueldo_base)
        print ("El sueldo bruto es de: $ ",self.calculo)
        print ("Las retenciones por ser casado y tener hijos es de: $",round(self.calculo*(self.retxhijos + self.retxcasa )),2)
        print("El sueldo neto queda es $",self.neto)
        
e=Empleado(12,80000,1000,15,1,3)
e.Calculo_Sueldo()
e.Calculo_Retenciones()
e.Sueldo_Neto() 
e.Mostrar_Det() 