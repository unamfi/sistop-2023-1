#!/usr/bin/python
from time import time

print(time())

tamano = 1024

def llena_arreglo(modo):
    arr = []
    for x in range(tamano):
        arr.append([])
        for y in range(tamano):
            arr[x].append([])

    for x in range(tamano):
        for y in range(tamano):
            if modo:
                arr[x][y] = 1
            else:
                arr[y][x] = 1

resultados = []
for i in range(10):
    inicio = time()
    llena_arreglo(0)
    fin = time()
    resultados.append(fin - inicio)

print( 'Resultados en vertical:')
for i in resultados:
    print(i)

resultados = []
for i in range(10):
    inicio = time()
    llena_arreglo(1)
    fin = time()
    resultados.append(fin - inicio)

print( 'Resultados en horizontal:')
for i in resultados:
    print(i)
