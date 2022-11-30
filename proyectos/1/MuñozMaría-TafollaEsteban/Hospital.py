#Version con consultorios aleatorios
import threading
import time
import random
import tkinter  
from PIL import Image, ImageTk
from tkinter import Canvas

#Total de consultorios

n_consultorios = 4
multiplex_consultorios = threading.Semaphore(n_consultorios) #Consultorios disponibles en el hospital
#multiplex_emergencia = threading.Semaphore(n_consultorios) # Verifica que alguien con emergencia pase antes que cualquiera
mutex_copia =  threading.Semaphore(1) #Protege acceso a informacion para la interfaz
GUI_mutex_fila = threading.Semaphore(8) #Representa las imagenes que puede haber dentro de la interfaz
mutex_protege_incrementos = threading.Semaphore(1) #Protege a la hora de obtener el tamaño de nuestra fila
root = tkinter.Tk() #Crea nuestra ventana para la interfaz
canvas = Canvas(root,width = 1050, height = 600) #Crea un espacio de travajo dentro de la ventana
tamanio = (150,150) #Vector que define las dimenciones de las imagenes de nuestros pacientes
GUI_fila = [] #Representa a las persona formadas dentro de la fila  

#Funciones para realizar el movimiento de las personas
def up(canvaImagen):
    canvas.move(canvaImagen,0,-5)
    root.update()
    

def down(canvaImagen):
    canvas.move(canvaImagen,0,5)
    root.update()
    

def left(canvaImagen):
    canvas.move(canvaImagen,-5,0)
    root.update()
    

#Clase para generar citas para el paciente regular
class Cita: 
    def __init__(self,hora ,minuto):
        self.hora = hora
        self.minuto = minuto

#Clase para medir tiempo 
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
            self.minutos = 0
        else:
            self.minutos += 15
#Realiza la impresion del reloj dentro de la interfaz
def relojito():
    global root
    global reloj1
    print("7:00")
    GUI_reloj = tkinter.Label(root,text="7:00")
    GUI_reloj.config(font=("Verdana",24)) 
    GUI_reloj.pack(anchor="nw")
    root.update()
    while True:
        reloj1.avanzaReloj()
        time.sleep(5)
        if (reloj1.minutos==0):
            print(str(reloj1.hora)+":00")
            GUI_reloj.config(text=str(reloj1.hora)+":00")
        else:
            print(str(reloj1.hora)+":"+str(reloj1.minutos))
            GUI_reloj.config(text=str(reloj1.hora)+":"+str(reloj1.minutos))
        root.update()

#Hilos que generan mas hilos de forma ciclica
def HiloEmergencia():
    id=1
    time.sleep(1)
    while True:
        threading.Thread(target=emergencia,args=[id]).start()
        time.sleep(3)
        id+=1

def HiloRegular():
    id=1
    time.sleep(random.randint(1,2))
    while True:
        threading.Thread(target=regular,args=[id]).start()
        time.sleep(random.randint(1,2))
        id+=1

def HiloChequeo():
    id=1
    time.sleep(random.randint(2,4))
    while True:
        threading.Thread(target=chequeo,args=[id]).start()
        time.sleep(random.randint(1,2))
        id+=1

#Recorre los elementos ubicados dentro de la fila
def avanzaFila(GUI_fila):
    for i in range (0, len(GUI_fila)):
        for j in range (1,30):
                left(GUI_fila[i])

#Permite que avance hacia algun consultorio uno de los pacientes ubicados en la fila    
def avanzaConsultorio(GUI_fila, noConsultorio):
    if(noConsultorio==1):
        for i in range (0, 60):
            left(GUI_fila[0])
        return GUI_fila.pop(0)
    elif(noConsultorio==2):
        for i in range (0, 60):
            left(GUI_fila[0])
            if(i < 40):
                up(GUI_fila[0])
        return GUI_fila.pop(0)
    elif(noConsultorio==3):
        for i in range (0, 60):
            left(GUI_fila[0])
            up(GUI_fila[0])
        for i in range (0, 20):
            up(GUI_fila[0])
        return GUI_fila.pop(0)
    elif(noConsultorio==4):
        for i in range(0,80):
            if(i<3):
                left(GUI_fila[0])
            up(GUI_fila[0])
        return GUI_fila.pop(0)

#Hilo de paciente regular
def regular(id):
    global reloj1 
    global GUI_fila
    global tamanio
    #Se crea la cita. Cada numero de cita representa una hora en específico
    #1 son las 7:00, 2 son las 7:15, 60 son las 22:00, ...
    cita1 = Cita(random.randint(reloj1.hora-2,reloj1.hora+2), random.randint(0,3)*15)

    #Un paciente regular puede llegar (mas o menos) una hora antes de su cita y ser atendido.
    #si llega antes o después no se le atendera
    if cita1.hora-reloj1.hora <= 1 and  cita1.hora-reloj1.hora >= 0:
        #Entra a la fila
        GUI_mutex_fila.acquire()
        #Crea la imagen dentro de la interfaz grafica
        GUI_icono = generaImagen("Regular", tamanio)
        #Usamos un mutex para evitar alteraciones dentro de los datos que obtendremos
        mutex_protege_incrementos.acquire()
        GUI_fila.append(canvas.create_image(1200,500, image = GUI_icono))    
        posicion=150-30*(len(GUI_fila)-1)
        #Coloca la imagen dentro de la interfaz
        for i in range (1,posicion):
            left(GUI_fila[len(GUI_fila)-1])
        mutex_protege_incrementos.release()
        #Ingresa al consultorio
        multiplex_consultorios.acquire()
        print("Soy un paciente regular",id,"y acabo de entrar a mi cita. La cita era a las "+str(cita1.hora)+":"+str(cita1.minuto))
        #Protege la funcion avanzaConsultorio
        mutex_copia.acquire()
        avanzaConsultorio(GUI_fila, random.randint(1,4))
        avanzaFila(GUI_fila)
        mutex_copia.release()
        time.sleep(5)
        print("Soy el paciente regular",id,"y ya salí de consulta")
        GUI_mutex_fila.release()
        multiplex_consultorios.release() #fin de consulta
    
    else:
        #En caso de no llegar a cita
        print("Soy un paciente regular y como no llegué a la hora de mi cita me mandaron pa mi casa :( \nMi cita era a las "+str(cita1.hora)+":"+str(cita1.minuto))
    
#Hilo de paciente emergencia
def emergencia(id):
    global GUI_fila
    global tamanio

    #Hace fila
    GUI_mutex_fila.acquire()
    
    #Genera imagen de interfaz
    GUI_icono = generaImagen("Emergencia", tamanio) 
    #Protege acceso a la informacion
    mutex_protege_incrementos.acquire()
    GUI_fila.append(canvas.create_image(1200,500, image = GUI_icono))   
    posision=150-30*(len(GUI_fila)-1)
    for i in range (1,posision):
        left(GUI_fila[len(GUI_fila)-1])
    mutex_protege_incrementos.release()

    
    multiplex_consultorios.acquire()
    print("Soy el paciente con emergencia "+str(id)+".He pasado directo al consultorio")
    #protegeFuncion avanzaConsultorio
    mutex_copia.acquire()
    avanzaConsultorio(GUI_fila, random.randint(1,4))
    avanzaFila(GUI_fila)
    mutex_copia.release()
    time.sleep(10)
    print("Soy el paciente con emergencia "+str(id)+" y ya me voy")
    
    GUI_mutex_fila.release()
    multiplex_consultorios.release() #fin de consulta
    
    
def chequeo(id):
    global GUI_fila
    global tamanio
    #Verifica que cumple las condiciones para hacer fila
    GUI_mutex_fila.acquire()

    #Crea su representacion grafica
    GUI_icono = generaImagen("Chequeo", tamanio)
    #Protege datos de GUI_fila  
    mutex_protege_incrementos.acquire()
    GUI_fila.append(canvas.create_image(1200,500, image = GUI_icono))  
    posision=150-30*(len(GUI_fila)-1)
    for i in range (1,posision):
        left(GUI_fila[len(GUI_fila)-1])
    mutex_protege_incrementos.release()

    #Verifica que haya consultorios disponibles y resive consulta    
    multiplex_consultorios.acquire()
    print("Soy el paciente de chequeo "+str(id)+". He pasado al consultorio")
    mutex_copia.acquire()
    avanzaConsultorio(GUI_fila, random.randint(1,4))
    avanzaFila(GUI_fila)
    mutex_copia.release()
    time.sleep(5)
    print("El paciente de chequeo "+str(id)+" se a ido")
    GUI_mutex_fila.release()
    multiplex_consultorios.release() #fin de consulta

#Obtiene imagen de directorio cada uno de los doctores representa un tipo de paciente 
# Verde = Regular
# Rojo = Emergencia
# Azul = Chequeo

def buscaImagen(tipo):
    aleatorio = random.randint(0, 5)   
    if(tipo=="Emergencia"):
        return "imagenes/imageR"+str(aleatorio)+".jpg"
    elif(tipo=="Chequeo"):
        return "imagenes/imageA"+str(aleatorio)+".jpg"
    elif(tipo=="Regular"):
        return "imagenes/imageV"+str(aleatorio)+".jpg"

#Crea imagen con el tamaño de la variable tamanio
def generaImagen(tipo, tamanio):
    imname = buscaImagen(tipo)
    return  ImageTk.PhotoImage(Image.open(imname).resize(tamanio))


def iniciaPrograma():

    global tamanio
    global canvas
    canvas.pack()

    #Fondo de la interfaz
    fondo = ImageTk.PhotoImage(file = "imagenes/Background.jpeg")
    canvas.create_image(0,0,image = fondo, anchor="nw")

    #Inicia hilos
    threading.Thread(target=relojito).start()
    threading.Thread(target=HiloRegular).start()
    threading.Thread(target=HiloChequeo).start()
    threading.Thread(target=HiloEmergencia).start()
    
    #Inicia interfaz
    root.mainloop()
    
#Inicia reloj
reloj1 = Reloj()

iniciaPrograma()

