#Fajardo Suárez Jesús Miguel - SO - El cruce del Rio
from threading import Semaphore, Thread
import time
import random

max_personas = 4
hackers = 0
serfs = 0
barrera = Semaphore(1) #Mutex para que los hilos suban de uno en uno
lugares =  Semaphore(4) #Multiplex para asegurar solo suban 4 personas
cuenta = 0

def Hacker ():
    global hackers
    print('Arriba el linux')
    SubirHackers()
    
def Serfs ():
    global serfs
    print('Arriba el Windows')
    SubirSerfs()
    
def SubirHackers():
    global hackers
    if (hackers >= 2 and serfs == 0) or (serfs <= 2 and hackers <= 1):
       lugares.acquire()
       hackers = hackers + 1
       print('Hacker a bordo')
       Viaje()
    else:
        print('Evitemos peleas, no puedes subir hacker\n')
        
   
        
def SubirSerfs():
    global serfs
    if (serfs >= 2 and hackers == 0) or (hackers <= 2 and serfs <= 1):
       lugares.acquire()   
       serfs= serfs+1
       #cuenta = cuenta +1
       print('Serf a bordo')
       Viaje()
       
    else:
        print('Evitemos peleas, no puedes subir serf')
        
    

def Viaje():
    global hackers
    global serfs
    if serfs + hackers == 4:
        print('viajando si que si')
        for i in range(4):
            lugares.release()
        print('Barco vacío, Subale hay lugares')
        hackers = 0
        serfs = 0
        
    else:
       print('Subale hay lugares') 

def Persona (id): #Para hacer realmente aleatorio el proceso de los hilos primero pasan por aqui asi sera realmente al azar si quien sube es un hacker o un serf
    num = random.randint(1,2)
    barrera.acquire() #Semaforo para ir de uno en uno
    if num % 2:
        Hacker()
    else:
        Serfs()
    barrera.release()  #Liberacion del semaforo para ir de uno en uno  

for i in range(12):
    Thread(target=Persona, args=[i]).start()