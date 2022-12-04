import random
import time
from threading import Barrier,Thread,Semaphore

#Barrera que detendra 5 hilos, 5 teléfonos 
maxLlamadas=Barrier(5)

#Semaforos y mutex que se le asigna a los hilos, dando la fluidez del programa
mut_atendiendo=Semaphore(1)
mut_pedido=Semaphore(1)
mutLlamada=Semaphore(1)

llamadaPedido=Semaphore(0)
nuevoIngt=Semaphore(0) 

#Lista de servicios que se brinda
servicios=["Una Hamburguesa"," Unos Hot-Dogs"," Una Torta"]


def llamada(num):
    global mutLlamada,telefonos,llamadaPedido
    while True:
        llamadaPedido.acquire()
        mutLlamada.acquire() 
        
        print("Llamada entrante")
        time.sleep(3)
        mutLlamada.release()
        mutLlamada.acquire()
        
        print("Tomando el pedido del cliente ",num)
        telefonos.append(1)
        time.sleep(2)
        mutLlamada.release()
        mutLlamada.acquire()
        
        print("Los telefonos ocupados\n")
        time.sleep(2)
        mutLlamada.release()
        mutLlamada.acquire()

        time.sleep(2)
        mutLlamada.release()
        llamadaPedido.release()
        maxLlamadas.wait()
       

#Envío del pedido
def pedido(num):
    global mut_pedido,ayuda,mutLlamada,telefonos
    while True:
        
        mutLlamada.acquire()
        
        mut_pedido.acquire()
        print("Preparando: ",str(random.choice(servicios)))
        print("Va en camino el repartidor\n")
        telefonos=telefonos[:-1]
        time.sleep(3)
        mut_pedido.release()
             
        llamadaPedido.release()
        mutLlamada.release()
        mut_pedido.acquire()

        time.sleep(random.randint(1,5))
        mut_pedido.release()
        llamadaPedido.acquire()
        
        
def main():
    global llamadaPedido, mut_atendiendo
    while True:
        if len(telefonos) >= 0:
            telDisponible=5-len(telefonos)
        else:
            telDisponible=0
        
        print("Líneas disponibles: ",telDisponible)
        print("Telefonos ", telefonos, "ocupados ", len(telefonos))
       
        mut_atendiendo.release()
        nuevoIngt.release()
        llamadaPedido.release()
        print("Esperando llamada\n")
        
        time.sleep(3)
        
        for num_llamadas in range(1,5):
            Thread(target=llamada,args=[num_llamadas]).start()
            
        for num_pedido in range(1,5):
            Thread(target=pedido,args=[num_pedido]).start()

#Lista donde nos inidcara la disponibilidad y el uso de los telefonos
telefonos=[] 
Thread(target=main,args=[]).start()