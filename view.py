#!/usr/bin/env python3
from flask import Flask, request, render_template
import os
app = Flask(__name__)
db = {'nombre': 'name', 'casa': 'home', 'gato': 'cat', 'perro': 'dog', 'chocolate': 'chocolate', 'hola': 'hello'}

def clientManagment(word, client):
    with open('server.log','a') as f:
        f.write('El cliente {} ha hecho una peticion de la palabra: {}\n'.format(client.get('name'),word))
    return db.get(word, 'default')


@app.route('/traductor', methods=['POST'])
def translator():
    return clientManagment(request.args.get('palabra', 'casa'), request.json)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
