#!/usr/bin/python3
from threading import Semaphore, Thread
import time
import random

num_sillas = 3
max_alumnos = 30
max_preguntas = 3
despierte_profe = Semaphore(0)
sillas = Semaphore(num_sillas)
mutex_pregunta = Semaphore(1)
pregunta_formulada = Semaphore(0)
respuesta_recibida = Semaphore(0)

def profesor():
    print('P: Inicia el horario de atención...')
    while True:
        despierte_profe.acquire()
        respuesta()

def alumno(id):
    sillas.acquire()
    print('A%d sentado.' % id)
    despierte_profe.release()
    for i in range(1, random.randint(1,3)):
        pregunta(id, i)
    sillas.release()
    print('A%d se fue.' % id)

def pregunta(id_alum, id_preg):
    mutex_pregunta.acquire()
    print('A%d: Profe, mi duda %d ... ¿Por qué?' % (id_alum, id_preg))
    pregunta_formulada.release()
    respuesta_recibida.acquire()
    print('A%d: Gracias por su sabiduría.' % id_alum)
    
def respuesta():
    pregunta_formulada.acquire()
    print('P: Tu respuesta es... Que así es.')
    respuesta_recibida.release()
    mutex_pregunta.release()

Thread(target=profesor).start()
for i in range(max_alumnos):
    Thread(target=alumno, args=[i]).start()
    
