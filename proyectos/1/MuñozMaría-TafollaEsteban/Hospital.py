import threading
import time
import random
from datetime import datetime
import tkinter  # py3
from PIL import Image, ImageTk
from tkinter import Canvas

#Total de consultorios

n_consultorios = 4
num_pacientes = 12 #porfa en mutiplos de 6

multiplex_consultorios = threading.Semaphore(n_consultorios) #consultorios ocupados
multiplex_emergencia = threading.Semaphore(n_consultorios) # Verifica que alguien con emergencia pase antes que cualquiera
multiplex_regulares= threading.Semaphore(1) #Verifica que alguien con cita pase antes que alguien sin cita

GUI_mutex_fila = threading.Semaphore(1)

root = tkinter.Tk()
canvas = Canvas(root,width = 1050, height = 600)
tamanio = (150,150)
GUI_cont_fila = 0
GUI_cont_cons = 0
GUI_fila = []
GUI_consultorios = []

def up(canvaImagen):
    canvas.move(canvaImagen,0,-5)
    root.update()
    time.sleep(.01)

def down(canvaImagen):
    canvas.move(canvaImagen,0,5)
    root.update()
    time.sleep(.01)

def left(canvaImagen):
    canvas.move(canvaImagen,-5,0)
    root.update()
    #time.sleep(.01)

class Cita: 
    def __init__(self,hora ,minuto):
        self.hora = hora
        self.minuto = minuto
        
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
        
def relojito():
    global root
    global reloj1
    print("7:00")
    #GUI_reloj = StringVar()
    #GUI_reloj.set("7:00")
    #tkinter.Label.config(textvariable=GUI_reloj)
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
        
def HiloEmergencia():
    id=1
    time.sleep(6)
    while True:
        threading.Thread(target=emergencia,args=[id]).start()
        time.sleep(6)
        id+=1

def HiloRegular():
    id=1
    time.sleep(random.randint(1,2))
    while True:
        #icono = generaImagen("Regular", tamanio)
        threading.Thread(target=regular,args=[id]).start()
        time.sleep(random.randint(1,2))
        id+=1

def HiloChequeo():
    id=1
    time.sleep(random.randint(2,4))
    while True:
        threading.Thread(target=chequeo,args=[id]).start()
        time.sleep(random.randint(3,4))
        id+=1
        
def regular(id):
    global reloj1
    global GUI_cont_fila
    global GUI_fila
    global tamanio
    #Se crea la cita. Cada numero de cita representa una hora en específico
    #1 son las 7:00, 2 son las 7:15, 60 son las 22:00, ...

    cita1 = Cita(random.randint(reloj1.hora-2,reloj1.hora+2), random.randint(0,3)*15)
    #cita1 = Cita(random.randint(7,21), random.randint(0,3)*15)

    #Un paciente regular puede llegar (mas o menos) una hora antes de su cita y ser atendido.
    #si llega antes o después no se le atendera
    if cita1.hora-reloj1.hora <= 1 and  cita1.hora-reloj1.hora >= 0:
        if GUI_cont_fila <= 4:
            GUI_icono = generaImagen("Chequeo", tamanio)
            canvaImagen = canvas.create_image(1200,500, image = GUI_icono)
            #GUI_fila.append(canvaImagen)
            posision=150-(30*GUI_cont_fila)
            for i in range (1,posision):
                left(canvaImagen)
            GUI_mutex_fila.acquire()
            GUI_cont_fila+=1
            GUI_mutex_fila.acquire()

        multiplex_emergencia.acquire()
        multiplex_emergencia.release()
        multiplex_regulares.acquire()
        multiplex_consultorios.acquire()

        GUI_mutex_fila.acquire()
        GUI_cont_fila-=1
        GUI_mutex_fila.acquire()

        print("Soy un paciente regular",id,"y acabo de entrar a mi cita. La cita era a las "+str(cita1.hora)+":"+str(cita1.minuto))
        time.sleep(5)
        print("Soy el paciente regular",id,"y ya salí de consulta")
        multiplex_consultorios.release()
        multiplex_regulares.release()
    else:
        print("Soy un paciente regular y como no llegué a la hora de mi cita me mandaron pa mi casa :( \nMi cita era a las "+str(cita1.hora)+":"+str(cita1.minuto))
    

def emergencia(id):
    global GUI_cont_fila
    global GUI_fila
    global tamanio
    if GUI_cont_fila <= 4:
        GUI_icono = generaImagen("Emergencia", tamanio)
        canvaImagen = canvas.create_image(1200,500, image = GUI_icono)
        #GUI_fila.append(canvaImagen)
        posision=150-(30*GUI_cont_fila)
        for i in range (1,posision):
            left(canvaImagen)
        GUI_mutex_fila.acquire()
        GUI_cont_fila+=1
        GUI_mutex_fila.acquire()
    multiplex_emergencia.acquire()
    multiplex_consultorios.acquire()

    for i in range (1,300):
        left(canvaImagen)

    GUI_mutex_fila.acquire()
    GUI_cont_fila-=1
    GUI_mutex_fila.acquire()

    print("Soy el paciente con emergencia "+str(id)+".He pasado directo al consultorio")
    time.sleep(10)
    print("Soy el paciente con emergencia "+str(id)+" y ya me voy")
    multiplex_consultorios.release()
    multiplex_emergencia.release()
    
def chequeo(id):
    global GUI_cont_fila
    global GUI_fila
    global tamanio
    if GUI_cont_fila <= 4:
        GUI_icono = generaImagen("Chequeo", tamanio)
        canvaImagen = canvas.create_image(1200,500, image = GUI_icono)
        #GUI_fila.append(canvaImagen)
        posision=150-(30*GUI_cont_fila)
        for i in range (1,posision):
            left(canvaImagen)
        GUI_mutex_fila.acquire()
        GUI_cont_fila+=1
        GUI_mutex_fila.acquire()
    multiplex_emergencia.acquire()
    multiplex_emergencia.release()

    multiplex_regulares.acquire()
    multiplex_regulares.release()

    multiplex_consultorios.acquire()

    for i in range (1,300):
        left(canvaImagen)

    GUI_mutex_fila.acquire()
    GUI_cont_fila-=1
    GUI_mutex_fila.acquire()
    print("Soy el paciente de chequeo "+str(id)+". He pasado al consultorio")
    time.sleep(5)
    print("El paciente de chequeo "+str(id)+"Ya se fue")
    multiplex_consultorios.release()

"""
QUITAR DE AQUI BUSCAR IMAGEN Y GENERAIMAGEN PARA EVITAR COCHINERO
"""
def buscaImagen(tipo):
    aleatorio = random.randint(0, 5)   
    if(tipo=="Emergencia"):
        return "imagenes/imageR"+str(aleatorio)+".jpg"
    elif(tipo=="Chequeo"):
        return "imagenes/imageA"+str(aleatorio)+".jpg"
    elif(tipo=="Regular"):
        return "imagenes/imageV"+str(aleatorio)+".jpg"

def generaImagen(tipo, tamanio):
    imname = buscaImagen(tipo)
    return  ImageTk.PhotoImage(Image.open(imname).resize(tamanio))


def iniciaPrograma():

    global tamanio
    global canvas
    canvas.pack()

    fondo = ImageTk.PhotoImage(file = "imagenes/Background.jpeg")
    #res_fondo = tkinter.Label(root, image = fondo, bd = 0)
    #res_fondo.place(relx=0, rely=0)

    canvas.create_image(0,0,image = fondo, anchor="nw")

    """im2 = generaImagen("Chequeo", tamanio)
    canvaImagen = canvas.create_image(75,75, image = im2)

    label = tkinter.Label(root, image= generaImagen("Regular", (100,100)))
    label.place(x=0,y=0)

    im2 = generaImagen("Chequeo", tamanio)
    canvaImagen = canvas.create_image(75,75, image = im2)
    
    for i in range (1,100):
        canvas.move(canvaImagen,2,2)
        root.update()
        time.sleep(.01)

    """
    threading.Thread(target=relojito).start()
    threading.Thread(target=HiloRegular).start()
    threading.Thread(target=HiloChequeo).start()
    threading.Thread(target=HiloEmergencia).start()
    root.mainloop()
    

reloj1 = Reloj()
iniciaPrograma()

#---------------------------------------------

def buscaImagen(tipo):
    aleatorio = random.randint(0, 5)   
    if(tipo=="Emergencia"):
        return "imagenes/imageR"+str(aleatorio)+".jpg"
    elif(tipo=="Chequeo"):
        return "imagenes/imageA"+str(aleatorio)+".jpg"
    elif(tipo=="Regular"):
        return "imagenes/imageV"+str(aleatorio)+".jpg"

def generaImagen(tipo, tamanio):
    imname = buscaImagen(tipo)
    return  ImageTk.PhotoImage(Image.open(imname).resize(tamanio))


"""
Chat 

"""
