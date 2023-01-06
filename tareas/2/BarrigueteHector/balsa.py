import threading
import time
import random

fila = 12
asientos = 4
hackers = 0
serfs = 0
persona = 0
hackers_esperando = 0
serfs_esperando = 0

mutex = threading.Semaphore(1)

def pasajero(id):
    global hackers
    global hackers_esperando
    global serfs
    global serfs_esperando

    mutex.acquire()
    time.sleep(2)

    persona = random.randrange(0, 2) # 0 = hacker, 1 = serf
           
    if persona == 0:
        hackers_esperando += 1
        print("-----------------------------------\nHacker", id, "esperando\n")
    else:
        serfs_esperando += 1
        print("-----------------------------------\nSerf", id, "esperando\n")
    
    print("--> Fila de espera\n    Hackers: ", hackers_esperando, "\n    Serfs: ", serfs_esperando, "\n")
    
    if (hackers_esperando + serfs_esperando == 5) or (hackers_esperando == 2 and serfs_esperando == 2) or hackers_esperando == 4 or serfs_esperando == 4:
        print("La balsa va a salir\n")
    else:
        print("La balsa todavia no puede salir\n")
        
    if hackers_esperando >= 2 and serfs_esperando >= 2:
        hackers_esperando -= 2
        serfs_esperando -= 2
        hackers += 2
        serfs += 2
        impresion()
    elif hackers_esperando >= 4:
        hackers_esperando -= 4
        hackers += 4
        impresion()
    elif serfs_esperando >= 4:
        serfs_esperando -= 4
        serfs += 4
        impresion()
    
    mutex.release()

def impresion():
    global hackers
    global serfs

    print("La balsa salio con:\n-> Hackers: ", hackers, "\n-> Serfs: ", serfs, "\n")

    hackers = 0
    serfs = 0

for i in range(fila):
	threading.Thread(target=pasajero, args=[i]).start()