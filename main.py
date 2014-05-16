__author__ = 'cristina'

from aplicacionesFree import AplicacionesFree

def menu():
    print("PeacheStore")
    print("1.APLICACIONES GRATUITAS")
    print("2.APLICACIONES DE PAGO")

menu()
aplicaciones = int(input())

if aplicaciones == 1:
    print("1. Mostrar lista")
    print("2. añadir nueva aplicacion")
    print("3. modificar los datos de identificacion de un aplicacion")
    print("4. sumar una descarga")
    print("5. sumar un comentario")
    tipoApp = int(input())

    if tipoApp == 1:
        print("lista")

    if tipoApp == 2:
            print("Introduce Nombre Aplicacion")
            nombreApp = str(input())
            print("proveedor")
            proveedorApp = str(input())
            aplicacionesFree = AplicacionesFree(nombreApp,proveedorApp)
            aplicacionesFree.crearRegistro()

    if tipoApp == 3:
        print("modificar datos")

    if tipoApp == 4:
        print("para sumar descarga introduce nombre de la aplicacion")
        nameApp = str(input())
        sumarDescarga =
        print("Descarga finalizada (+1)")

    if tipoApp == 5:
        print("para sumar un comentario introduce nombre de la aplicacion")
        print("Comentario registrado (+1)")

elif aplicaciones == 2:
    print("1. Mostrar lista")
    print("2. añadir nueva aplicacion")
    print("3. modificar los datos de identificacion de un aplicacion")
    print("4. sumar una descarga")
    print("5. sumar un comentario")
    tipoAppB = int(input())

    if tipoAppB == 1:
        print("lista")

    if tipoAppB == 2:
            print("Introduce Nombre Aplicacion")
            nombreAppB = str(input())
            print("proveedor")
            proveedorAppB = str(input())
            print("Indica el precio de la aplicacion: ejemplo 0,95")
            precioAppB = str(input())
            aplicacionesB = AplicacionesB(nombreAppB,proveedorAppB,precioAppB)
            aplicacionesB.crearRegistroB()


    if tipoApp == 3:
        print("modificar datos")

    if tipoApp == 4:
        print("para sumar descarga introduce nombre de la aplicacion")
        print("Descarga finalizada (+1)")

    if tipoApp == 5:
        print("para sumar un comentario introduce nombre de la aplicacion")
        print("Comentario registrado (+1)")
