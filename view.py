#!/usr/bin/env python3
from flask import Flask, request
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
import atexit
import os
"""Se inicia la aplicacion de Flask. Se recuerda que Flask funciona con Threads por defecto"""
app = Flask(__name__)
"""Se define la variable lock como metodo de proteccion de una condicion de carrera"""
lock = Lock()
"""Se define la variable del archivo 'server.log'"""
f = open('server.log','a')
"""Diccionario encargado de simular una base de datos de palabras"""
db = {'nombre': 'name', 'casa': 'home', 'gato': 'cat', 'perro': 'dog', 'chocolate': 'chocolate', 'hola': 'hello'}


"""Funcion encargada de escibir en el archivo 'server.log' y retornar la palabra"""
def clientManagment(word, client, lock):
    global f
    with lock:
        f.write('El cliente {} ha hecho una peticion de la palabra: {}\n'.format(client.get('name'),word))
        f.flush()
        os.fsync(f.fileno())
    return db.get(word, 'default')


"""Funcion que define la ruta de servidor y los métodos a utilizar con la misma"""
@app.route('/traductor', methods=['POST'])
def translator():
    """'ThreadPoolExecutor' se encarga de abrir un hilo con la funcion y devolver su resultado una vez termine"""
    """En 'request.args' se pueden recolectar los query parameters de la peticion"""
    """En 'request.json' se recolecta el json con informacion del cliente"""
    with ThreadPoolExecutor() as executor:
        prom = executor.submit(clientManagment, request.args.get('palabra', 'casa'), request.json, lock)
        return prom.result()


"""Funcion encargada de devolver un string con todo lo del archivo 'server.log'"""
def readOnFile(lock):
    global f
    text = ''
    with lock:
        f = open('server.log', 'r')
        for line in f.readlines():
            text = text + line
        f.close()
        f = open('server.log','a')
    return text


"""Funcion que define la ruta encargada de devolver el contenido del archivo 'server.log'"""
@app.route('/file')
def file():
    """'ThreadPoolExecutor' se encarga de abrir un hilo con la funcion y devolver su resultado una vez termine"""
    with ThreadPoolExecutor() as executor:
        prom = executor.submit(readOnFile, lock)
        return prom.result()


"""Funcion que cierra el archivo al finalizar el proceso del servidor"""
def closeFile():
    f.close()


if __name__ == '__main__':
    atexit.register(closeFile)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
