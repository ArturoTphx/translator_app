#!/usr/bin/env python3
import csv
import sys

def make(number):
    ls = ['nombre','casa','gato','perro','chocolate', 'hola']
    index = 0
    count = 1
    bash = open('requests.sh', 'w')
    bash.write('#!/bin/bash\n')
    with open('persons.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if count != number:
                bash.write("curl -X POST -H \"Content-Type: application/json\" \\\n"
                    + "-d '{\"name\": \"" + row.get('name') +"\"}' \\\n"
                    + "http://127.0.0.1:5000/traductor?palabra="+ls[index]+"\\\n"
                    + "&\\\n")
            else:
                bash.write("curl -X POST -H \"Content-Type: application/json\" \\\n"
                    + "-d '{\"name\": \"" + row.get('name') +"\"}' \\\n"
                    + "http://127.0.0.1:5000/traductor?palabra="+ls[index]+"\n")
            if index == (len(ls) - 1):
                index = 0
            else:
                index = index + 1
            if count == number:
                break
            else:
                count = count + 1
    bash.close()

if __name__ == '__main__':
    number = 100
    if len(sys.argv) == 2:
        number = int(sys.argv[1])
    else:
        number = 100
    if number <= 0:
        number = 100
    elif number > 1000:
        number = 1000
    make(number)
