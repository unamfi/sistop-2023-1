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
    prof_dice('Inicia el horario de atención...')
    while True:
        despierte_profe.acquire()
        respuesta()

def alumno(id):
    sillas.acquire()
    alumno_dice(id, 'sentado.')
    despierte_profe.release()
    for i in range(1, random.randint(1,3)):
        pregunta(id, i)
    sillas.release()
    alumno_dice(id, '⇒🚪')

def pregunta(id_alum, id_preg):
    mutex_pregunta.acquire()
    alumno_dice(id_alum, 'Profe, mi duda %d ... ¿Por qué?' % id_preg)
    pregunta_formulada.release()
    respuesta_recibida.acquire()
    alumno_dice(id_alum, 'Gracias por su sabiduría.')

def respuesta():
    pregunta_formulada.acquire()
    prof_dice('Tu respuesta es... Que así es.')
    respuesta_recibida.release()
    mutex_pregunta.release()

def alumno_dice(id,str):
    print(' %s🧒%d %s' % (' '*id, id, str))

def prof_dice(str):
    print('🧓 %s' % (str))

Thread(target=profesor).start()
for i in range(max_alumnos):
    Thread(target=alumno, args=[i]).start()
