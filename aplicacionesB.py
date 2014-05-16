__author__ = 'cristina'

import time
from datetime import date
today = date.today()

class AplicacionesB():
    def __init__(self, nombreAppB,proveedorAppB,precioAppB):
        self.nombreAppB = nombreAppB
        self.proveedorAppB = proveedorAppB
        self.precioAppB = precioAppB

    def getNombreAppB(self):
        return self.nombreAppB

    def getProveedorAppB(self):
        return self.proveedorAppB

    def getPrecioAppB(selfself):
        return self.precioAppB

    def crearRegistroB(self):
        registroAppB = (self.nombreAppB+"-"+self.proveedorAppB+"-"+str(today)+"-"+self.precioAppB+"0"+"-"+"0"+"-"+"0"+"-"+"0"+"\n")

        with open('aplicacionesB.txt', mode='a', encoding='utf-8')as archivo:
            archivo.write(registroAppB)
            print(registroAppB)
