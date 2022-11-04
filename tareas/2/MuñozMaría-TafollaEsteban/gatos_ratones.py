import threading
import time
import random

n_platos = 5 #Platos disponibles para alimentarse 
ratones = 0
gatos = 0
num_ratones = 0
num_gatos = 0

multiplex_platos = threading.Semaphore(n_platos) # Verifica cuantos platos hay disponibles
cuarto_con_ratones = threading.Semaphore(1) # Verificar que no haya en el cuarto ratones
mutex = threading.Semaphore(1) # Protege a la variable ratones
mutex2 = threading.Semaphore(1) # Protege a la variable gatos
mutex_muerte = threading.Semaphore(0) # Permite a los ratones valientes morir :c
fila_gatos= threading.Semaphore(1) # Evita la inhalicion para los gatos 

def gato(id):
    global gatos

    #para verificar que no haya ratones
    fila_gatos.acquire()
    cuarto_con_ratones.acquire()
    cuarto_con_ratones.release()

    #"ticket" de espera para gatos. Si un gato estaba esperando los ratones no entraran
    multiplex_platos.acquire()
    fila_gatos.release()

    mutex2.acquire()
    gatos = gatos + 1
    mutex2.release()

    print("Hola, soy el gato", id)
    comeGato(id)

    mutex2.acquire()
    gatos = gatos - 1
    mutex2.release()

    terminaDeComer(id, "Gato")
    multiplex_platos.release()

def muerte(id):
    global ratones
    print("Un gato mató al ratoncito", id,":(")
    mutex.acquire()
    ratones = ratones - 1
    if ratones == 0:
        cuarto_con_ratones.release()
    mutex.release()

def raton(id):
    global ratones
    global gatos

    fila_gatos.acquire()
    fila_gatos.release()

    mutex.acquire()
    ratones = ratones + 1
    if ratones == 1:
        cuarto_con_ratones.acquire()
    mutex.release()

    multiplex_platos.acquire()
    print("Hola, soy el ratoncito", id)

    mutex2.acquire()
    if gatos > 0 :
        mutex_muerte.acquire()
        muerte(id)
        mutex_muerte.release()
        mutex2.release()
        multiplex_platos.release()
        return
    mutex2.release()

    come(id, "Ratón")
    terminaDeComer(id, "Ratón")

    mutex.acquire()
    ratones = ratones - 1
    if ratones == 0:
        cuarto_con_ratones.release()
    mutex.release()

    multiplex_platos.release()

def terminaDeComer(id, animal):
    print(animal, id , "a terminado de comer")

def come(id, animal):
    print(animal, id, "esta comiendo")
    time.sleep(0.5)
    time.sleep(random.random())

def comeGato(id):
    mutex_muerte.release()
    print("Gato", id, "esta comiendo")
    time.sleep(0.1)
    time.sleep(random.random())
    mutex_muerte.acquire()


def iniciaPrograma():
    global num_gatos
    global num_ratones
    for id in range(10):
        for y in range(int(random.uniform(1,4))):
            num_ratones += 1
            threading.Thread(target=raton, args=[num_ratones]).start()
            time.sleep(0.1)
        for x in range(int(random.uniform(1,4))):
            num_gatos += 1
            threading.Thread(target=gato, args=[num_gatos]).start()
            time.sleep(0.1)

iniciaPrograma()


