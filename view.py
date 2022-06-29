#!/usr/bin/env python3
from flask import Flask, request, render_template
import os
"""Se inicia la aplicacion de Flask. Se recuerda que Flask funciona con Threads por defecto"""
app = Flask(__name__)
"""Diccionario encargado de simular una base de datos de palabras"""
db = {'nombre': 'name', 'casa': 'home', 'gato': 'cat', 'perro': 'dog', 'chocolate': 'chocolate', 'hola': 'hello'}


"""Funcin encargada de escibir en el archivo 'server.log' y retornar la palabra"""
def clientManagment(word, client):
    with open('server.log','a') as f:
        f.write('El cliente {} ha hecho una peticion de la palabra: {}\n'.format(client.get('name'),word))
    return db.get(word, 'default')


"""Funcion que define la ruta de servidor y los métodos a utilizar con la misma"""
@app.route('/traductor', methods=['POST'])
def translator():
    """En 'request.args' se pueden recolectar los query parameters de la peticion"""
    """En 'request.json' se recolecta el json con informacion del cliente"""
    return clientManagment(request.args.get('palabra', 'casa'), request.json)


"""Funcion que define la ruta encargada de devolver el contenido del archivo 'server.log'"""
@app.route('/file')
def file():
    text = ''
    with open('server.log','r') as f:
        for line in f.readlines():
            text = text + line
    return text


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
