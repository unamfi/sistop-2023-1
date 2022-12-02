import threading
import random
import time


#Recursos compartidos
contador_personas=0


#Administración de procesos

entrada_mutex= threading.Semaphore(1)
salida_mutex= threading.Semaphore(1)
esperar_m=threading.Event()
esperar_c=threading.Event()


## La función mesero crea al mesero

def mesero():
    global esperar_c

    print(" -- Mesero  espera clientes")
    flag=esperar_c.wait() #Esta bandera nos indica si un cliente a solicitado que se sea atendido
    if flag:
        print(" -- El mesero le entrega el menú al cliente")
        esperar_c.clear()
        esperar_m.set()

        flag=esperar_c.wait() #Esta bandera nos indica si cliente escogio su bebida
        if flag:
            print(" -- El mesero va a preparar la bebida del cliente")
            preparar=random.randint(1,2)
            time.sleep(preparar)
            print(" -- El mesero entrega la bebida")
            new_m=threading.Thread(target=mesero)
            new_m.start()
            esperar_m.set()
            new_m.join()



#Cliente crea el hilo cliente
def Cliente(num):
    global contador_personas
    runCliente(num)
    entrada_mutex.acquire() #Implementamos torniquete para evitar que entren más de una persona
    entrar(num)
    entrada_mutex.release()

#Inicia hilo cliente
def runCliente(numC):
    print(" - Cliente "+str(numC)+" solicitando entrar")



#Método que inidica el comportamiento de un cliente
def pedir(numC):
    global ticket
    esperar_c.clear()
    esperar_m.clear()

    print(" - El cliente "+str(numC)+" está esperando ser atendido")
    esperar_c.set()
    esperar_m.wait()
    esperar_m.clear()
    print(" - El cliente "+str(numC)+" está escogiendo su bebida")
    time.sleep(0.5)
    print(" - El cliente "+str(numC)+" pide su bebida")
    esperar_c.set()
    esperar_m.wait()
    esperar_c.clear()
    print(" - El cliente "+str(numC)+" empieza a tomar su bebida")
    tomar=random.randint(1,2)
    time.sleep(tomar)
    print(" - El cliente "+str(numC)+" terminó su bebida")
    salir(numC)


#Método que indica cuando un cliente está adentro de la tienda
def entrar(num):
    print(" - El cliente "+str(num)+" entró al café")
    pedir(num)

#Método que indica que un cliente a salido de la tienda
def salir(num):
    global contador_personas
    print(" - El cliente "+str(num)+ " paga y se va")
    salida_mutex.acquire()
    contador_personas-=1
    salida_mutex.release()




# Almacenamos los hilos de actores
hilos_clientes = []
hilo_mesero = []


def main():
    print("     -------------------------------------------------------------")
    print("                          EL PUMACAFÉ :D ")
    print("     -------------------------------------------------------------")

    numClientes = int(input(" - ¿Cuántos clientes tendrá durante el día?"))

    for j in range (1):
        hilo_mesero.append(threading.Thread(target=mesero))#Creamos los hilos de los meseros
        hilo_mesero[j].start()
        time.sleep(1)
    for i in range(numClientes):
        hilos_clientes.append(threading.Thread(target=Cliente, args=[i])) #Creamos los hilos de los clientes
        hilos_clientes[i].start()
        time.sleep(0.25)
    for j in range (1):
        hilo_mesero[j].join()
    for i in range(numClientes):
        hilos_clientes[i].join()

main()
