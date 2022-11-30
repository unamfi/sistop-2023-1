import threading
import time
import random
import tkinter  
from PIL import Image, ImageTk
from tkinter import Canvas

#Total de consultorios

n_consultorios = 4
multiplex_consultorios = threading.Semaphore(n_consultorios) #consultorios ocupados
multiplex_emergencia = threading.Semaphore(n_consultorios) # Verifica que alguien con emergencia pase antes que cualquiera
multiplex_regulares= threading.Semaphore(1) #Verifica que alguien con cita pase antes que alguien sin cita
mutex_copia =  threading.Semaphore(1)
GUI_mutex_fila = threading.Semaphore(5)
mutex_protege_incrementos = threading.Semaphore(1)
#consultorio_disponible = [0,0,0,0]
root = tkinter.Tk()
canvas = Canvas(root,width = 1050, height = 600)
tamanio = (150,150)
GUI_cont_fila = 0
GUI_cont_cons = 0
GUI_fila = []
GUI_consultorios = []
'''
def buscaConsultorio():
    global consultorio_disponible
    cont = 0
    while(consultorio_disponible[cont]):
        cont+=1
    consultorio_disponible[cont] = 1
    print (cont)
    return cont+1
def liberaConsultorio(num_consultorio):
    global consultorio_disponible
    consultorio_disponible[num_consultorio] = 0
'''
def up(canvaImagen):
    canvas.move(canvaImagen,0,-5)
    root.update()
    #time.sleep(.01)

def down(canvaImagen):
    canvas.move(canvaImagen,0,5)
    root.update()
    #time.sleep(.01)

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
    time.sleep(1)
    while True:
        threading.Thread(target=emergencia,args=[id]).start()
        time.sleep(3)
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
        time.sleep(random.randint(1,2))
        id+=1
def avanzaFila(GUI_fila):
    for i in range (0, len(GUI_fila)):
        for j in range (1,30):
                left(GUI_fila[i])
    
def avanzaConsultorio(GUI_fila, noConsultorio):
    if(noConsultorio==1):
        for i in range (0, 60):
            left(GUI_fila[0])
        return GUI_fila.pop()
    elif(noConsultorio==2):
        for i in range (0, 60):
            if(i < 40):
                up(GUI_fila[0])
            left(GUI_fila[0])
            
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

def regular(id):
    global reloj1
    global GUI_cont_fila
    global GUI_fila
    global tamanio
    #Se crea la cita. Cada numero de cita representa una hora en específico
    #1 son las 7:00, 2 son las 7:15, 60 son las 22:00, ...

    cita1 = Cita(random.randint(reloj1.hora-2,reloj1.hora+2), random.randint(0,3)*15)

    #Un paciente regular puede llegar (mas o menos) una hora antes de su cita y ser atendido.
    #si llega antes o después no se le atendera
    if cita1.hora-reloj1.hora <= 1 and  cita1.hora-reloj1.hora >= 0:
        multiplex_emergencia.acquire()
        multiplex_emergencia.release()
        GUI_mutex_fila.acquire()
        GUI_icono = generaImagen("Regular", tamanio)
        mutex_protege_incrementos.acquire()
        GUI_fila.append(canvas.create_image(1200,500, image = GUI_icono))    
        posision=150-30*(len(GUI_fila)-1)
        print("La posicion de regular es", str(posision))
        for i in range (1,posision):
            left(GUI_fila[len(GUI_fila)-1])
        mutex_protege_incrementos.release()

        

        multiplex_regulares.acquire()
        multiplex_consultorios.acquire()
        print("Soy un paciente regular",id,"y acabo de entrar a mi cita. La cita era a las "+str(cita1.hora)+":"+str(cita1.minuto))
        
        time.sleep(5)
        print("Soy el paciente regular",id,"y ya salí de consulta")
        
        #Elimina un elemento grafico
        mutex_copia.acquire()
        #consultrio_asignado =  buscaConsultorio()
        #avanzaConsultorio(GUI_fila,random.randint(1,4))
        GUI_fila.pop(0)
        avanzaFila(GUI_fila)
        mutex_copia.release()
        #liberaConsultorio(consultrio_asignado-1)
        GUI_mutex_fila.release()
        multiplex_regulares.release()
        multiplex_consultorios.release() #fin de consulta
        
    
    else:
        print("Soy un paciente regular y como no llegué a la hora de mi cita me mandaron pa mi casa :( \nMi cita era a las "+str(cita1.hora)+":"+str(cita1.minuto))
    

def emergencia(id):
    global GUI_fila
    global tamanio
    GUI_mutex_fila.acquire()
    
    GUI_icono = generaImagen("Emergencia", tamanio)
   
     
    mutex_protege_incrementos.acquire()
    GUI_fila.append(canvas.create_image(1200,500, image = GUI_icono))   
    posision=150-30*(len(GUI_fila)-1)
    print("La posicion de emergencia es", str(posision))
    for i in range (1,posision):
        left(GUI_fila[len(GUI_fila)-1])
    mutex_protege_incrementos.release()

    
    
    multiplex_emergencia.acquire()
    multiplex_consultorios.acquire()
    print("Soy el paciente con emergencia "+str(id)+".He pasado directo al consultorio")
    
    time.sleep(10)
    print("Soy el paciente con emergencia "+str(id)+" y ya me voy")
    
    #Elimina un elemento grafico
    mutex_copia.acquire()
        #consultrio_asignado =  buscaConsultorio()
        #avanzaConsultorio(GUI_fila,random.randint(1,4))
    GUI_fila.pop(0)
    avanzaFila(GUI_fila)
    mutex_copia.release()
    #liberaConsultorio(consultrio_asignado-1)
    GUI_mutex_fila.release()
    multiplex_emergencia.release()
    multiplex_consultorios.release() #fin de consulta
    
    
    
def chequeo(id):
    global GUI_consultorios
    global GUI_fila
    global tamanio
    #Verifica que cumple las condiciones para hacer fila
    multiplex_emergencia.acquire()
    multiplex_emergencia.release()

    multiplex_regulares.acquire()
    multiplex_regulares.release()
    GUI_mutex_fila.acquire()

    #Crea su representacion grafica
    GUI_icono = generaImagen("Chequeo", tamanio)
      
    mutex_protege_incrementos.acquire()
    GUI_fila.append(canvas.create_image(1200,500, image = GUI_icono))  
    posision=150-30*(len(GUI_fila)-1)
    print("La posicion de cheaquo es", str(posision))
    for i in range (1,posision):
        left(GUI_fila[len(GUI_fila)-1])
    mutex_protege_incrementos.release()

    
    
    #verifica que haya consultorios disponibles y resive consulta    
    multiplex_consultorios.acquire()
    print("Soy el paciente de chequeo "+str(id)+". He pasado al consultorio")
    
    time.sleep(5)    
    
    print("El paciente de chequeo "+str(id)+" se a ido") 
    #Elimina un elemento grafico
    mutex_copia.acquire()
        #consultrio_asignado =  buscaConsultorio()
        #avanzaConsultorio(GUI_fila,random.randint(1,4))
    GUI_fila.pop(0)
    avanzaFila(GUI_fila)
    mutex_copia.release()
    #liberaConsultorio(consultrio_asignado-1)
    GUI_mutex_fila.release()
    multiplex_consultorios.release() #fin de consulta
    

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