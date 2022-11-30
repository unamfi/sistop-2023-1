import threading
import time
import random
from datetime import datetime

#Total de consultorios 
n_consultorios = 4
num_pacientes = 12 #porfa en mutiplos de 6

multiplex_consultorios = threading.Semaphore(n_consultorios) #consultorios ocupados
multiplex_emergencia = threading.Semaphore(n_consultorios) # Verifica que alguien con emergencia pase antes que cualquiera
multiplex_regulares= threading.Semaphore(1) #Verifica que alguien con cita pase antes que alguien sin cita
now = datetime.now()

class Reloj:
    def __init__(self):
        self.hora = 7
        self.minutos = 0

    def avanzaReloj(self):
        #Despues de 45 le sumamos 1 ahora y minutos vuelve a ser 0            
        if(self.minutos == 45):
            if(self.hora == 21):
                self.hora = 7
            else:   
                self.hora += 1 
            self.minutos = 00
        else:
            self.minutos += 15
        
def relojito():
    reloj1=Reloj()
    print(str(reloj1.hora)+":"+str(reloj1.minutos))
    while True:
        reloj1.avanzaReloj()
        time.sleep(1)
        if (reloj1.minutos==0):
            print(str(reloj1.hora)+":00")
        else:
            print(str(reloj1.hora)+":"+str(reloj1.minutos))


        

class Cita: 
    def __init__(self,hora ,minuto):
        self.hora = hora
        self.minuto = minuto

def regular():
    #Se crea la cita. Cada numero de cita representa una hora en específico
    #1 son las 7:00, 2 son las 7:15, 60 son las 22:00, ...
    cita1 = Cita(random.randint(7,21), random.randint(0,3)*15)
    #Un paciente regular puede llegar (mas o menos) una hora antes de su cita y ser atendido.
    #si llega antes o después no se le atendera
    if cita1.hora-reloj1.hora <= 1 and  cita1.hora-reloj1.hora >= 0:
        multiplex_emergencia.acquire()
        multiplex_emergencia.release()
        multiplex_regulares.acquire()
        multiplex_consultorios.acquire()
        print("Soy un paciente regular y acabo de entrar a mi cita. La cita era a las "+str(cita1.hora)+":"+str(cita1.minuto))
        time.sleep(1)
        multiplex_consultorios.release()
        multiplex_regulares.release()
    else:
        print("Soy un paciente regular y como no llegué a la hora de mi cita me mandaron pa mi casa :( \nMi cita era a las"+str(cita1.hora)+":"+str(cita1.minuto))
    

def emergencia():
    multiplex_emergencia.acquire()
    multiplex_consultorios.acquire()
    print("Soy un paciente con emergencia. He pasado directo al consultorio")
    time.sleep(1)
    multiplex_consultorios.release()
    multiplex_emergencia.release()
    
def chequeo():
    multiplex_emergencia.acquire()
    multiplex_emergencia.release()

    multiplex_regulares.acquire()
    multiplex_regulares.release()
    multiplex_consultorios.acquire()
    print("Soy un paciente de chequeo. He pasado al consultorio")
    time.sleep(1)
    multiplex_consultorios.release()


reloj1 = Reloj()
print(now.hour)
print(now.minute)
#Modelamos para que cada una de las citas dure un segundo 
print(now.second)

def iniciaPrograma():

    threading.Thread(target=relojito).start()
    #threading.Thread(target=emergencia).start()

    global num_pacientes
    num_emergencias = num_pacientes/6
    num_regulares = num_pacientes/2
    num_chequeo = num_pacientes/3

    for x in range((int)(num_pacientes)):
        threading.Thread(target=emergencia).start()
        for x in range(3):
            threading.Thread(target=regular).start()
        for x in range(2):
            threading.Thread(target=chequeo).start()


iniciaPrograma()

"""
x = datetime.datetime()
print(x.strftime("%S")) 

Chat 
Tenemos en cuenta que la clínica cuenta con 12 consultorios por turno y cada consulta está pensada para durar 15 minutos
Existen 3 tipos de pacientes: regulares, espontáneos y chequeos.
Dentro de los pacientes regulares se encuentran las personas diabéticas, embarazadas, hipertensas y que requieren oxígeno quienes requieren una cita cada mes. A ellos se les dan citas a partir de las 9 hs a las 13:40 hs. 
En los pacientes espontáneos se encuentran aquellos que tienen cosas que no se pudieron prevenir con anticipación (una caída, gripa, etc) a ellos se les asignan las 4 primeras consultas en cada consultorio de 8 hs a 9 hs. Si existen más pacientes espontáneos que no alcanzaron a tomar un lugar dentro de esa 4 consultas se pueden formar en la “Unifila”, donde otro otro médico que se encuentre disponible los atenderá, o bien si en algún consultorio no llegó algún paciente. 
Y los pacientes de chequeos los cuales pueden hacer una cita telefónica (llamada cita digital) en alguno de estos horarios 9:00, 9:15 y 11:00 hs
   
    48 consultas en total para cada consultorio 
   7 a 10 
   Emergencia 1 
   Regular 2
   Chequeo Sin cita 3



   for id in range(10):
        for y in range(int(random.uniform(1,4))):
            num_ratones += 1
            threading.Thread(target=raton, args=[num_ratones]).start()
            time.sleep(0.1)
        for x in range(int(random.uniform(1,4))):
            num_gatos += 1
            threading.Thread(target=gato, args=[num_gatos]).start()
            time.sleep(0.1)

    for x in range((int)(num_emergencias)):
        threading.Thread(target=emergencia).start()
    for x in range((int)(num_chequeo)):
        threading.Thread(target=chequeo).start()
    for x in range((int)(num_regulares)):
        threading.Thread(target=regular).start()
"""