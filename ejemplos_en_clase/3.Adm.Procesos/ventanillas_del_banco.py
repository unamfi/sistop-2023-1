#!/usr/bin/python3
from threading import Semaphore, Thread
import time

ventanilla = Semaphore(0)
en_turno = True

def maneja_fin_del_dia():
    print("**** ABRE EL BANCO ****")
    time.sleep(10)
    en_turno = False
    print("**** CERRANDO BANCO ****")

def cajero(id):
    ventanilla.release()
    while en_turno:
        print('%d: Cajero listo' % id)
        procesa_cliente(id)
        print('%d: Terminé de procesar a un cliente' % id)
    ventanilla.acquire()
    print('%d: Ventanilla cerrada. ¡Adios!' % id)

def cliente(id):
    print('Cliente %d entra' % id)
    ventanilla.acquire()
    print('Manejando lana %d' % id)
    maneja_lana(id)
    ventanilla.release()
    print('Cliente %d se fue.' % id)

def maneja_lana(id):
    print('¡Quiero más! (%d)' % id)
    time.sleep(2)

def procesa_cliente(id):
    time.sleep(4)
    print('Lo siento, no hay sistema.')

Thread(target=maneja_fin_del_dia).start()

for i in range(5):
    Thread(target=cajero, args=[i]).start()

id_cliente = 0
while en_turno:
    id_cliente += 1
    Thread(target=cliente, args=[id_cliente]).start()
    time.sleep(2)
