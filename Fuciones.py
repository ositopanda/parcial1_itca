
def guardar_registro():
    nombre = input("Titulo de la pelicula: ")
    Genero= input("Genero:")
    estreno   = input("fecha de estreno: ")





    pelicula = {
        "nombre de la pelicula": nombre,
        "Genero":Genero,
        "estreno":estreno,



    }
    return pelicula

def actualizar_registro():
    print("***Que desea modificar")
    print("1. Modificar pelicula")
    print("2. Modificar un elemento de la pelicula")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        nombre = input("Titulo de la pelicula: ")
        actor = input("Nombre de la pelicula: ")



        pelicula = {
            "nombre": nombre,
            "actor": actor,


        }
        return pelicula
    elif opcion == "2":
        indice = input("Ingrese el indice: ")
        valor = input("Ingrese el valor a modificar: ")
        pelicula = {indice: valor}
        return pelicula