__author__ = 'cristina'

class AplicacionesFree():
    def __init__(self, nombreApp,proveedorApp):
        self.nombreApp = nombreApp
        self.proveedorApp = proveedorApp

    def getNombreApp(self):
        return self.nombreApp

    def getProveedorApp(self):
        return self.proveedorApp

    def crearRegistro(self):
        registroApp = (self.nombreApp+"-"+self.proveedorApp+"-"+date+"-"+"0,00"+"0"+"0"+"0"+"0"+"\n")

        with open('aplicacionesFree.txt', mode='a', encoding='utf-8')as archivo:
            archivo.write(registro)
            print(registro)
