##Autores:
##Rodriguez Colorado
##Méndez Sánchez

from threading import Thread, Semaphore, Barrier
import random
import time

#Patrones:Mecanismos de sincronización
recepcionistas = Semaphore(2)
pizzeris = Semaphore(2) 

caja_Reparto = Barrier(3)

queso = Semaphore(1)
horno = Semaphore(3)

#Acciones
def tomaPedido(idCliente):
  print("Buenas tardes, %d"%idCliente)
  print("Pedido no %d recibido"%idCliente)
  numero = random.randint(1,3)
  print("Ok cliente %d pizzas"%numero)
  return numero

def cocinar(idCliente):
  queso.acquire() ##Corresponde a que solo se pueden agarrar los ingredientes una pizza
                  ##a la vez
  print("Preparando la pizza %d"%idCliente)
  queso.release()
    
  horno.acquire()
  print("En el horno %d"%idCliente)
  horno.release()
    
  print("Preparada")

def reparto(idReparto):
  print("Repartidor esperando")
  caja_Reparto.wait()
  print("Repartidor saliendo con la orden %d"%idReparto)

def pedido(idCliente):

  proceso = Semaphore(1)

  #recepción de pedidos
  recepcionistas.acquire()
  noPizzas = tomaPedido(idCliente)
  recepcionistas.release()

  #en produccion
  pizzeris.acquire()
  print("Pizzera ocupada")
  pizzera=[]
  ##Se validan a continuación las 3 pizzas que pueden entrar al horno
  for i in range (noPizzas): 
    pizza = Thread(target=cocinar, args=[i])
    pizzera.append(pizza)
    pizza.start()

  for noPizza, thread in enumerate(pizzera):
    thread.join()
    print("pizza %d finalizada"%noPizza)
  print("Pizzera desocupada")
  pizzeris.release()

  #Reparto
  Thread(target=reparto, args=[idCliente]).start()


num_Clientes = int(input("Ingresa el numero de clientes a atender "))

for i in range(num_Clientes):
  Thread(target=pedido, args=[i]).start()