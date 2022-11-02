import random
import threading
import time
lectores = 0
mutex = threading.Semaphore(1)
cuarto_vacio = threading.Semaphore(1)
torniquete = threading.Semaphore(1)

def lee():
    with mutex:
        print("... Leyendo ... Hay %d lectores en el cuarto." % lectores)
    time.sleep(3)
    print("Ya leí.")

def escribe():
    print("... Escribiendo ...")
    time.sleep(5)
    print("Ya escribí.")

def escritor():
    print('Llega un escritor, ', end='')
    torniquete.acquire()
    print('toma el primer mutex, ', end='')
    cuarto_vacio.acquire()
    print('prende la luz, y escribe.')
    escribe()
    cuarto_vacio.release()
    torniquete.release()

def lector():
    print('Llega un lector, ', end='')
    torniquete.acquire()
    torniquete.release()

    print('pasa el torniquete, ')
    global lectores
    mutex.acquire()
    lectores = lectores + 1
    if lectores == 1:
        cuarto_vacio.acquire()
    mutex.release()
    print('y se pone a leer.')
    lee()

    mutex.acquire()
    lectores = lectores - 1
    if lectores == 0:
        cuarto_vacio.release()
    mutex.release()

while True:
    time.sleep(1)
    if random.random() < 0.15:
        threading.Thread(target=escritor).start()
    else:
        threading.Thread(target=lector).start()
