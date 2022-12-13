from pymongo import MongoClient

client = MongoClient("localhost")

db = client["TALLER10"]

database = db['Slangs']


def agregar(var1, var2):
    database.insert_one(({'Palabra': var1,
                           'Significado': var2}))


def editar(var3, var4):
    database.update_one({'Palabra': var3},
                        {"$set": {"Significado": var4}})


def eliminar(var5):
    database.delete_many({'Palabra': var5})


def verPalabras():
    palabras = []
    for documentos in database.find({}):
        dict = {}
        dict['Palabra'] = documentos['Palabra']
        dict['Slang'] = documentos['Significado']
        palabras.append(dict)
    return palabras


def Significado(var6):
    palabra = []
    for elementos in database.find({'Palabra': var6}):
        dict = {}
        dict['Palabra'] = elementos['Palabra']
        dict['Significado'] = elementos['Significado']
        palabra.append(dict)
    return palabra