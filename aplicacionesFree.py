__author__ = 'cristina'

import time
from datetime import date
today = date.today()


class AplicacionesFree():
    def __init__(self, nombreApp,proveedorApp):
        self.nombreApp = nombreApp
        self.proveedorApp = proveedorApp

    def getNombreApp(self):
        return self.nombreApp

    def getProveedorApp(self):
        return self.proveedorApp

    def crearRegistro(self):
        registroApp = (self.nombreApp+"-"+self.proveedorApp+"-"+str(today)+"-"+"0,00"+"-"+"0"+"-"+"0"+"-"+"0"+"-"+"0"+"\n")

        with open('aplicacionesFree.txt', mode='a', encoding='utf-8')as archivo:
            archivo.write(registroApp)
            print(registroApp)
