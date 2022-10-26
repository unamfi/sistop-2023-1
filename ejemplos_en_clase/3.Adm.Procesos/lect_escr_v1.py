import random
import threading
import time
lectores = 0
mutex = threading.Semaphore(1)
cuarto_vacio = threading.Semaphore(1)

def lee():
    print("... Leyendo ...")
    time.sleep(3)
    print("Ya leí.")

def escribe():
    print("... Escribiendo ...")
    time.sleep(5)
    print("Ya escribí.")

def escritor():
    cuarto_vacio.acquire()
    escribe()
    cuarto_vacio.release()

def lector():
    global lectores
    mutex.acquire()
    lectores = lectores + 1
    if lectores == 1:
        cuarto_vacio.acquire()
    mutex.release()

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
