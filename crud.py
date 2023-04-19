from conexionDB import collection
import json

def buscar_pelicula(id=None):
    if id is not None:
        query = {"_id": id}
        document = collection.find_one(query)
        print(document)
    else:
        documents = collection.find()
        for document in documents:
            print(document)


def registro(guardar_pelicula):
    result = collection.insert_one(guardar_pelicula)
    print(result.inserted_id)


def modificar_registro(id, registro):
    query = {"_id": id }
    new_values = {"$set": registro }
    result = collection.update_one(query,new_values)
    print(result.modified_count)


def eliminar_pelicula(eliminar):
    db_base = collection
    resultado = collection.delete_one({'_id': eliminar })
    print(resultado.deleted_count)