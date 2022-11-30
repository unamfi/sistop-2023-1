#Autores
### Mendez Sanchez y Rodriguez Colorado.
### 3 de octubre de 2022

from threading import Thread, Semaphore, Barrier
import random
import time

#Variable que determina el número de personas que abordan
num_hackers = 4
num_serfs = 7

#barreras que delimitan el número de personas por bando
barreraHack = Barrier(2)
barreraSerfs = Barrier(2)

#barrera 
barreraBalsa = Barrier(4)
barreraLlegada = Barrier(4)

#mutex que representa el numero de asientos en la balsa
asiento_balsa = Semaphore(4)


def hacker(id):
      
    print("Hacker %d esperando\n"%id)
    barreraHack.wait()

    asiento_balsa.acquire()
    print("Subo a la balsa soy hack %d\n"%id)
    barreraBalsa.wait()
    

    print("Adios, zarpamos\n")
    barreraLlegada.wait()
    asiento_balsa.release()
    print("Este no iba pa'l centro\n")
    
    
def serf(id):
   print("Serf %d esperando\n"%id)
   barreraSerfs.wait()

   asiento_balsa.acquire()
   print("Subo a la balsa soy serf %d\n"%id)
   barreraBalsa.wait()

   print("Adios, zarpamos\n")
   barreraLlegada.wait()
   asiento_balsa.release()
   print("Este no iba pa'l centro\n")
   

for i in range(num_hackers):
  Thread(target=hacker, args=[i]).start()

for i in range(num_serfs):
  time.sleep(random.randint(0,2))
  Thread(target=serf, args=[i]).start()
