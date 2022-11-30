#CODIGO REALIZADO POR: BARRIGUETE RODRÑIGUEZ HÉCTOR ALEJANDRO 

import threading
import time
import random

barrera = threading.Semaphore(5)
mutex = threading.Semaphore(1)

#104 CARTAS EN TOTAL
#id 0
cartas_corazon = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#id 1
cartas_diamante = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#id 2
cartas_trebol = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#id 3
cartas_pica = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

puntaje = [0, 0, 0, 0, 0] #Puntajes de cada jugador, el último no se utiliza, solo es para evitar error
puntaje_crupier = 0

dinero = [0, 0, 0, 0]
apuesta = [000, 0, 0, 0, 0] #Apuestas de cada jugador, el último no se utiliza, solo es para evitar error
lista_plantados = ['S', 'S', 'S', 'S', 'S'] # S -> sigue, P -> plantado , el ultimo corresponde al Crupier

tipo = 0 #Tipo de carta, 0 -> Corazón, 1 -> Diamante, 2 -> Trebol, 3 -> Pica
numero = 0 #Numero/valor de cada carta

pedir_carta = True #Variable para saber si el jugador pide otra carta o se planta
pedir_carta_crupier = True #Variable para saber si el Crupier pide otra carta o se planta

carta_repetida = False #Variable para saber si la carta ya fue repartida (jugada 2 veces)

diferencia = 0 #Diferencia entre 21 y el puntaje del jugador
decision = 0 #Decision aleatoria para saber si el jugador pide otra carta o se planta, 

contador_plantados = 0 #Contador para saber cuantos jugadores se plantaron, incluye el Crupier

personas_mesa = 4 
lista_turnos = [] #Lista de turnos
id_crupier = 4 

def jugador(id):
    global dinero, apuesta
    dinero[id] = 0
    apuesta[id] = 0

    mutex.acquire()
    lista_turnos.append(id)

    if len(lista_turnos) == 4: #Cuando todos los jugadores ya estén en la lista se agrega al crupier
        lista_turnos.append(id_crupier)

    dinero[id] = random.randrange(4, 12) * 100 
    print("Dinero del Jugador #" + str(id) + " $" + str(dinero[id]))

    apuesta[id] = random.randrange(1, 4) * 100 
    print("Apuesta del Jugador #" + str(id) + " $" + str(apuesta[id]) + "\n")

    mutex.release()
    mesa(id, dinero[id], apuesta[id])

def crupier():
    mesa(id_crupier, 0, 0)

def mesa(id, dinero_jugador, apuesta_jugador):
    global puntaje, puntaje_crupier, dinero, apuesta, lista_plantados, contador_plantados
    puntaje[id] = 0
    apuesta[id] = 0
    pedir_carta = True
    pedir_carta_crupier = True
    carta_repetida = False

    time.sleep(5)
    while True:
        for plantado in lista_plantados: #Verifica si todos los jugadores se plantaron
            if plantado == 'P':
                contador_plantados += 1
            
        if contador_plantados != 5: #Si no se plantaron todos los jugadores
            for turno in lista_turnos: #Verifica el turno del jugador
                if turno == id and lista_plantados[id] == 'S': #Si es el turno del jugador y no se plantó
                    mutex.acquire()

                    #Se reparte una carta
                    tipo = random.randrange(0, 4) # 0 -> Corazón, 1 -> Diamante, 2 -> Trebol, 3 -> Pica
                    numero = random.randrange(1, 11)

                    if (id != id_crupier and int(puntaje[id]) < 22 and pedir_carta) or (id == id_crupier and int(puntaje_crupier) < 22 and pedir_carta_crupier):
                        # Si el ID es el de un jugador, su puntaje es menor a 22 y pide carta, o si el ID es el del Crupier, su puntaje es menor a 22 y pide carta

                        if(tipo == 0): 
                            carta_repetida = repartiendo(numero, cartas_corazon, "CORAZONES")
                        elif(tipo == 1): 
                            carta_repetida = repartiendo(numero, cartas_diamante, "DIAMANTES")
                        elif(tipo == 2): 
                            carta_repetida = repartiendo(numero, cartas_trebol, "TREBOLES")
                        elif(tipo == 3): 
                            carta_repetida = repartiendo(numero, cartas_pica, "PICAS")

                    time.sleep(1)

                    if id != id_crupier: #Si el ID es el de un jugador
                        if int(puntaje[id]) < 22 and pedir_carta: #Si el puntaje es menor a 22 y pide carta
                            #print("Repartiendo cartas al jugador", id, "\n")

                            if carta_repetida == False: #Si la carta no ha sido repetida (jugada 2 veces) se le suma al puntaje del jugador
                                puntaje[id] += numero
                            
                            if (int(puntaje[id]) == 21): #Si el puntaje es 21, se planta
                                pedir_carta = False    
                            else:
                                print("JUGADOR #" + str(id) + " Puntaje actual:", puntaje[id], "\n")
                                
                                if int(puntaje[id]) >= 11: #Puntaje mayor/igual a 11
                                    pedir_carta = probabilidad(int(puntaje[id])) #¿Se pide otra carta?

                            if pedir_carta == False or int(puntaje[id]) > 21: #Si se planta o el puntaje es mayor a 21
                                lista_plantados[id] = 'P' #Se agrega a la lista de plantados

                        else:
                            print("-> JUGADOR #" + str(id) + " Puntaje final:", puntaje[id], "\n")

                    else: #Si el ID es el del Crupier
                        if int(puntaje_crupier) < 22 and pedir_carta_crupier: #Si el puntaje es menor a 22 y pide carta
                            if carta_repetida == False: #Si la carta no ha sido repetida (jugada 2 veces) se le suma al puntaje del Crupier
                                puntaje_crupier += numero

                            if puntaje_crupier >= 17: #Si el puntaje es mayor o igual a 17, se planta
                                pedir_carta_crupier = False
                            
                            print("Crupier Puntaje actual:", puntaje_crupier, "\n")        
                        else:
                            print("-> Crupier Puntaje final:", puntaje_crupier, "\n")
                        
                        if pedir_carta_crupier == False or int(puntaje_crupier) > 21: #Si se planta o el puntaje es mayor a 21
                            lista_plantados[id_crupier] = 'P' #Se agrega a la lista de plantados

                    mutex.release()

                    time.sleep(1)
                else:
                    time.sleep(4) #Espera 4 segundos para volver a verificar el turno del jugador
        else:
            if id != 4: #Si el ID es el de un jugador
                #Se hacen comprobaciones para saber si el jugador gana, pierde o empata con el Crupier
                if puntaje[id] < 22 and (puntaje[id] > puntaje_crupier or (puntaje_crupier > 21 and puntaje[id] < puntaje_crupier)):
                    dinero_jugador += apuesta_jugador * 2
                    print("-> Jugador #" + str(id) + " (" + str(puntaje[id]) + ") le ganó al Crupier (" +  str(puntaje_crupier) +")\nDinero actual del jugador: $" + str(dinero_jugador) + "\n")
                elif (puntaje[id] < puntaje_crupier or puntaje[id] > 21) and puntaje_crupier < 22:
                    dinero_jugador -= apuesta_jugador
                    print("-> El Crupier (" + str(puntaje_crupier) +") le ganó al Jugador #" + str(id) + " (" + str(puntaje[id]) + ")\nDinero actual del jugador: $" + str(dinero_jugador) + "\n")                    
                else:
                    print("-> Entre el Jugador #" + str(id) + " (" + str(puntaje[id]) +") y el Crupier (" + str(puntaje_crupier) +"), nadie gana\n")

            break #Se sale del ciclo infinito al llegar al ID del Crupier
        contador_plantados = 0 #Se reinicia el contador de plantados

def repartiendo(valor, lista_carta, str_carta):
    if (valor in lista_carta): #Si la carta está en la lista de cartas
        lista_carta.remove(valor) #Se elimina de la lista de cartas
        print(valor, "DE", str_carta)
        return False
    else:
        return True
        
def probabilidad(puntaje):
    diferencia = 21 - puntaje #Se calcula la diferencia entre 21 y el puntaje actual

    decision = random.randrange(1, 11) #Se genera un número aleatorio entre 1 y 10

    if decision <= diferencia: #Si el número aleatorio es menor o igual a la diferencia
        print("Pide otra carta\n")
        return True #Se pide otra carta
    else: #Si el número aleatorio es mayor a la diferencia
        print("Se planta\n")
        return False #Se planta

def main():
    for i in range(personas_mesa):
        threading.Thread(target=jugador, args=[i]).start()
    
    time.sleep(1)

    threading.Thread(target=crupier).start()

main()