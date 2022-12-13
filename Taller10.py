### Programacion de Computadoras IV
## Taller 10
# Braulio Rodriguez 8-899-1093

from flask import Flask, jsonify, request
from database import verPalabras, Significado, agregar, editar, eliminar
app = Flask(__name__)


#Rutas
@app.route('/Diccionario')
def get():
    Palabras = verPalabras()
    return jsonify(Palabras)


@app.route('/Diccionario/<string:Palabra>')
def get(Palabra):
      Palabra = Significado(Palabra)
      print(Palabra)
      if Palabra !=None and Palabra != []:
          return jsonify(Palabra)
      else:
          return jsonify({"message":'Palabra No encontrada'})


@app.route('/Diccionario',methods=['POST'])
def add():
    var1 = request.json['Espanol']
    var2 = request.json["Slang"]
    agregar(var1, var2)
    Palabra = verPalabras()
    return jsonify({'message ':'Palabra añadida correctamente', "Palabras": Palabra})


@app.route('/Diccionario/<string:Espanol>',methods =['PUT'])
def edit(Espanol):
    Palabra = verPalabras()
    if Palabra !=None and Palabra != []:
        var3 = request.json['Espanol']
        var4= request.json['Slang']
        editar(var3,var4)
        return jsonify({"message":'Palabra Modificada Correctamente'})
    else:
        return jsonify({"message":'Palabra No encontrada'})


@app.route('/Diccionario/<string:Espanol>',methods=['DELETE'])
def delete(Palabra):
    Palabra = verPalabras()
    if Palabra !=None and Palabra != []:
        var5 = request.json['Palabra']
        eliminar(var5)
        Palabra = verPalabras()
        return jsonify({"message":'Palabra Eliminada',"Palabras":Palabra})
    else:
        return jsonify({"message":'Palabra No encontrada'})


if __name__ == '__main__':
    app.run(debug=True,port=5000)
