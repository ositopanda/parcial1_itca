from crud import *
from Fuciones import *
while True:
    print("***Menu***")
    print("1.***Mostrar toda las peliculas***")
    print("2.***Agregar  pelicula***")
    print("3.***Actualizar pelicula***")
    print("4.***Eliminar registro***")
    print("5.***Salir del menu***")
    opcion = input("Ingrese un opcion: ")
    if opcion == "1":
        buscar_pelicula()
    elif opcion == "2":
        pelicula = guardar_registro()
        registro(pelicula)
    elif opcion == "3":
        id = int(input("Ingrese el ID del pelicula a modificar: "))
        pelicula= actualizar_registro()
        modificar_registro(id,pelicula)
    elif opcion == "4":
        id = int(input("Ingrese el ID a eliminar: "))
        eliminar= eliminar_pelicula(id)
