"""
----Cruce del río----
    *   Para llegar a un encuentro de desarrolladores de sistemas
        operativos, hace falta cruzar un río en balsa.
    *   Los desarrolladores podrían pelearse entre sí, hay que cuidar
        que vayan con un balance adecuado
    *   En la balsa caben cuatro (y sólo cuatro) personas
        -   La balsa es demasiado ligera, y con menos de cuatro puede
            volcar.
    *   Al encuentro están invitados hackers (desarrolladores de Linux)
        y serfs (desarrolladores de Microsoft).
        -   Para evitar peleas, debe mantenerse un buen balance: No
            debes permitir que aborden tres hackers y un serf, o tres serfs y
            un hacker. Pueden subir cuatro del mismo bando, o dos y dos.
    *   Hay sólo una balsa.
    *   No se preocupen por devolver la balsa (está programada para
        volver sola)
"""

import threading
from time import sleep
from random import random

num_pasajeros = 10
pasajerosABajar = 4
p_tipo = 0.3
barrPasajeros = threading.Barrier(pasajerosABajar)
bajar = threading.Semaphore(0)
arribaB = threading.Semaphore(0)
asientosDeBalsa=[]
mutexB = threading.Semaphore(1)

def pasajeros(id:int):
    global asientosDeBalsa
    while True:
        sleep(1)
        if random() < p_tipo:
            print(f"Aborda desarrollador Linux: {id}")
            with mutexB:
                asientosDeBalsa.append("desarrollador Linux")
            barrPasajeros.wait()
            with mutexB:
                bajar.release()
            arribaB.acquire()
        else:
            print(f"Aborda desarrollador Microsoft: {id}")
            with mutexB:
                asientosDeBalsa.append("desarrollador Microsoft")
            barrPasajeros.wait()
            with mutexB:
                    bajar.release()
            arribaB.acquire()

def asientos():
    global asientosDeBalsa
    while True:
        print("Balsa: aborda")
        bajar.acquire()
        print("Balsa: checando la posibilidad de salir")
        mutexB.acquire()
        if((len(asientosDeBalsa) == 4) and (((asientosDeBalsa.count("desarrollador Microsoft")==4) or (asientosDeBalsa.count("desarrollador Microsoft")==2)) or ((asientosDeBalsa.count("desarrollador Microsoft")==2) and (asientosDeBalsa.count("desarrollador Linux")==2)))):
            print("Balsa: Desenbarcando")
            while len(asientosDeBalsa) > 0:
                pasajeros = asientosDeBalsa.pop(0)
                print(f"Balsa: Dejando al pasajero: {pasajeros}")
                arribaB.release()
            mutexB.release()
        elif (len(asientosDeBalsa)==0):
            print("Esperando")
            mutexB.release()
        else:
            print("Balsa: solicitud denegada, balsa no balanceada, todos abajo")
            while len(asientosDeBalsa) > 0:
                pasajeros = asientosDeBalsa.pop(0)
                print(f"Bajando al pasajero {pasajeros}")
                arribaB.release()
            mutexB.release()
            
def main():
    threading.Thread(target=asientos).start()
    for i in range(4,num_pasajeros):
        threading.Thread(target=pasajeros,args=[i]).start()

main()