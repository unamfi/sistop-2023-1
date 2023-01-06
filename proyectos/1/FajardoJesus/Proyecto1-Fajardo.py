from threading import Thread, Lock, Barrier
from time import sleep
from tkinter import *
import random
#Candado que simulara el afinador
Afinador = Lock()
#Candados que definen si los instrumentos se desafinaron
GuitarraDesafinada = Lock()
BajoDesafinado = Lock()
#candados auxiliares para romper un ciclo
CandadoBajo = Lock()
CandadoGuitarra = Lock()
#Candado para silenciar al baterista
SilenciaBateria = Lock()
#Barrera para sincronizar al guitarrista y al bajista
Barrera = Barrier(2)


def Guitarrista():
    #ciclo infinito para tocar la guitarra
    while True:
        #variable que definirá si se desafino el instrumento
        num = 0
        #liberamos el candado auxiliar para la ruptura del ciclo
        CandadoGuitarra.release()
        while num < 16: #si num es mayor a 16 entonces el instrumento se desafino 
            #en caso de que el bajo de desafine el guitarrista improvisara para no aburrirse
            #y cómo realmente sigue tocando aún corre el riesgo de desafinarse
            if BajoDesafinado.locked(): 
                while num < 16:
                    AccionGuitarra.set("Tiempo de improvisar")
                    sleep(3)
                    num = random.randint(1,20)
                    #si el candado auxiliar bloquea significa que el bajo se afino 
                    #por lo tanto se volverá a tocar en grupo y se rompe el ciclo
                    if CandadoBajo.locked(): 
                        Barrera.wait() #Barrera para sincronizar al grupo
                        break
                break
            #Si todos están parejos tocaran juntos su instrumento 
            AccionGuitarra.set("Tocando guitarra")
            sleep(3)
            num = random.randint(1,20) #la desafinación se dará de forma aleatoria en esta variable
        #Si se sale del ciclo significa que nuestro instrumento se desafino    
        GuitarraDesafinada.acquire()
        AccionGuitarra.set("Guitarra desafinada")
        sleep(1)
        if Afinador.locked(): #Si el afinador no esta disponible se callara al baterista para poder afinar
            AccionGuitarra.set("SHHHHHHH")
            sleep(1)
            SilenciaBateria.acquire()
            AccionGuitarra.set("Afinando de oido cuerda 7")
            sleep(2)
            AccionGuitarra.set("Afinando de oido cuerda 6")
            sleep(2)
            AccionGuitarra.set("Afinando de oido cuerda 5")
            sleep(2)
            AccionGuitarra.set("Afinando de oido cuerda 4")
            sleep(2)
            AccionGuitarra.set("Afinando de oido cuerda 3")
            sleep(2)
            AccionGuitarra.set("Afinando de oido cuerda 2")
            sleep(2)
            AccionGuitarra.set("Afinando de oido cuerda 1")
            sleep(2)
            AccionGuitarra.set("Termine de afinar, hora de tocar")
            #Se permite a la bateria seguir tocando al terminar de afinar
            SilenciaBateria.release() 
        else: #En caso de estar disponible el afinador se toma y se permite seguir tocando al baterista, ademas que el otro miembro puede tocar tambien
            Afinador.acquire()
            AccionGuitarra.set("Toma el afinador")
            sleep(1)
            AccionGuitarra.set("Guitarrista: Afinando cuerda 7")
            sleep(2)
            AccionGuitarra.set("Guitarrista: Afinando cuerda 6")
            sleep(2)
            AccionGuitarra.set("Guitarrista: Afinando cuerda 5")
            sleep(2)
            AccionGuitarra.set("Guitarrista: Afinando cuerda 4")
            sleep(2)
            AccionGuitarra.set("Guitarrista: Afinando cuerda 3")
            sleep(2)
            AccionGuitarra.set("Guitarrista: Afinando cuerda 2")
            sleep(2)
            AccionGuitarra.set("Guitarrista: Afinando cuerda 1")
            sleep(2)
            AccionGuitarra.set("Termine de afinar, hora de tocar")
            Afinador.release() #Se suelta el afinador 
        GuitarraDesafinada.release()    #Se libera el candado de la afinación porque ya esta afinado el instrumento
        CandadoGuitarra.acquire()   #Se bloquea el candado para que el bajo rompa el ciclo de slapeo random
        Barrera.wait() #Se espera a que los hilos esten en la barrera para poder sincronizarse
       
         
        
#Para el Bajista se omitiran los comentarios ya que es exactamente el mismo procedimiento que el guitarrista        
#solo que con sus respectivos dialogos
def Bajista():
    while True:
        num = 0
        CandadoBajo.release()
        while num < 16:        
            if GuitarraDesafinada.locked():
                while num < 16:
                    AccionBajo.set("Slap random activado")
                    sleep(3)
                    num = random.randint(1,20)
                    if CandadoGuitarra.locked():
                        Barrera.wait()
                        break
                break
            AccionBajo.set("Tocando bajo")
            sleep(3)
            num = random.randint(1,20)
            
        BajoDesafinado.acquire()
        AccionBajo.set("Bajo desafinado")
        sleep(1)
        if Afinador.locked():
            AccionBajo.set("SHHHHHHH")
            sleep(1)
            SilenciaBateria.acquire()
            AccionBajo.set("Afinando de oido cuerda 5")
            sleep(2)
            AccionBajo.set("Afinando de oido cuerda 4")
            sleep(2)
            AccionBajo.set("Afinando de oido cuerda 3")
            sleep(2)
            AccionBajo.set("Afinando de oido cuerda 2")
            sleep(2)
            AccionBajo.set("Afinando de oido cuerda 1")
            sleep(2)
            AccionBajo.set("Termine de afinar, hora de tocar")
            SilenciaBateria.release()
        else:
            Afinador.acquire()
            AccionBajo.set("Toma el afinador")
            sleep(1)
            AccionBajo.set("Bajista: Afinando cuerda 5")
            sleep(2)
            AccionBajo.set("Bajista: Afinando cuerda 4")
            sleep(2)
            AccionBajo.set("Bajista: Afinando cuerda 3")
            sleep(2)
            AccionBajo.set("Bajista: Afinando cuerda 2")
            sleep(2)
            AccionBajo.set("Bajista: Afinando cuerda 1")
            sleep(2)
            AccionBajo.set("Termine de afinar, hora de tocar")
            Afinador.release()
        BajoDesafinado.release()
        CandadoBajo.acquire()
        Barrera.wait()
        
    
def Baterista():
    #En caso de que algun hilo este afinando de oido se callara al baterista son SilenciaBateria
    #En cuanto termine de afinar el guitarrista podra tocar libremente
    while True:
        if SilenciaBateria.locked() :
            AccionBateria.set("Ya no puedo tocar")
            SilenciaBateria.acquire()
            AccionBateria.set("Ya me dejan tocar")
            sleep(1)
            SilenciaBateria.release()
        else:
            AccionBateria.set("TupaTupaTupa")
            sleep(2)
            
        
#Funcion que dara inicio al programa
def Inicio():
    CandadoBajo.acquire()
    CandadoGuitarra.acquire()
    Thread(target=Guitarrista, args=[]).start()
    Thread(target=Bajista, args=[]).start()
    Thread(target=Baterista, args=[]).start()
#Funcion para cerrar el programa
def Terminar():
    sys.exit()
        
#------INTERFAZ------#

#Creación de la ventana grafica
ventana = Tk()
#Tamaño de la ventana
ventana.geometry('850x600')

#Propiedades de despliegue de la imagen de la guitarra
guitarra = PhotoImage(file='guitarra.png')
guitarra_sub=guitarra.subsample(7)

#Propiedades de despliegue de la imagen del bajo
bajo = PhotoImage(file='bajo.png')
bajo_sub=bajo.subsample(2)

#Propiedades de despliegue de la imagen de la bateria
bateria = PhotoImage(file='bateria.png')
bateria_sub=bateria.subsample(9)

#Despliegue de las imagenes
Label(ventana, image=guitarra_sub).place(x=10, y=0)
Label(ventana, image=bajo_sub).place(x=20, y=110)
Label(ventana, image=bateria_sub).place(x=20, y=310)

#Mensajes de accion de la guitarra
AccionGuitarra = StringVar()
AccionGuitarra.set("Acción de la guitarra")
TextoGuitarra = Label(ventana, textvariable = AccionGuitarra, font=('Verdana', 18))
TextoGuitarra.place(x=400, y=50)

#Mensajes de accion del bajo
AccionBajo = StringVar()
AccionBajo.set("Acción del bajo")
TextoBajo = Label(ventana, textvariable = AccionBajo, font=('Verdana', 18))
TextoBajo.place(x=400, y=220)

#Mensajes de accion de la bateria
AccionBateria = StringVar()
AccionBateria.set("Acción de la bateria")
TextoBateria = Label(ventana, textvariable = AccionBateria, font=('Verdana', 18))
TextoBateria.place(x=400, y=400)

#Definición del boton iniciar
boton_iniciar=Button(ventana, text="INICIAR", command=Inicio)
boton_iniciar.config(width=10, height=3)
boton_iniciar.place(x=20, y=530)

#Definición del boton terminar
boton_iniciar=Button(ventana, text="TERMINAR", command=Terminar)
boton_iniciar.config(width=10, height=3)
boton_iniciar.place(x=150, y=530)

ventana.mainloop()








