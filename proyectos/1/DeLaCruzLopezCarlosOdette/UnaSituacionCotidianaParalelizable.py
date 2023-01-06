#import threading
from threading import Semaphore
from threading import Thread
from time import sleep
from random import randrange
from random import getrandbits

#Primitivas
jugadoresMaxEnSalaDeEspera  = Semaphore(10)#MULTIPLEX
jugadoresEnSalaDeEspera     = Semaphore(4)#MULTIPLEX
esperandoInicializarPartida = Semaphore(3)#MULTIPLEX
LobbyDisponibles            = Semaphore(3)#MULTIPLEX
LobbysEnPartida             = Semaphore(0)
partidaFinalizada           = Semaphore(0)
SalirseDelLobbyDeJuego      = Semaphore(0)
pantallaDeCarga             = Semaphore(0)
recibirExperiencia          = Semaphore(0)
mensajesConsola             = Semaphore(1)#MUTEX--->Me servira para poder conseguir mensajes en la consola sin afectarme las paralelidad


#Configuracion de lobbys (Variables globales)
jugadoresPorPartida                     = 10
jugadoresEnMenu                         = 4
jugadoresRestantesDelLobbyParaJugar     = 3

#Funciones
def desarrolloDelLobby(jugadorIDWarzone):
    global jugadoresPorPartida
    global jugadoresEnMenu
    global jugadoresRestantesDelLobbyParaJugar

    #El usuario entra al juego
    jugadoresMaxEnSalaDeEspera.acquire()
    
    mensajesConsola.acquire()
    jugadoresPorPartida -= 1
    print(f"Usuario: {jugadorIDWarzone} Entrando a Warzone")
    print(f"Disponibilidad para mas jugadores: {jugadoresPorPartida}")
    mensajesConsola.release()
    sleep(randrange(3))

    #El usuario permanece en el menu, en espera a dar comienzo a una partida
    jugadoresEnSalaDeEspera.acquire()
    
    mensajesConsola.acquire()
    print(f"Usuario: {jugadorIDWarzone}, se encuentra en el menú")
    jugadoresEnMenu -= 1
    print(f"Disponibilidad para más jugadores{jugadoresEnMenu}")
    mensajesConsola.release()

    #El Usuario, entra a un Lobby, en espera que de comienzo la partida
    esperandoInicializarPartida.acquire()
    jugadoresEnSalaDeEspera.release()

    mensajesConsola.acquire()
    print(f"Usuario: {jugadorIDWarzone}, la partidad comenzara en {randrange(60)} segundos, practica mientras")
    jugadoresRestantesDelLobbyParaJugar -= 1
    jugadoresEnMenu += 1
    print(f"Disponibilidad para más jugadores: {jugadoresEnMenu}")
    print(f"Partida de \"1 vs {jugadoresRestantesDelLobbyParaJugar}\"")
    mensajesConsola.release()

    #Partida en "juego"
    LobbysEnPartida.release()
    sleep(randrange(3))

    mensajesConsola.acquire()
    print(f"El usuario: {jugadorIDWarzone} mató de un disparo a usuario: {randrange(300)}")
    mensajesConsola.release()

    #Finaliza la partida, (muerte/victoria)
    partidaFinalizada.acquire()

    mensajesConsola.acquire()
    if (1 == (getrandbits(1))):
        a = "ganado" 
    else:
        a="perdio"
    print(f"Usuario: {jugadorIDWarzone} usted a {a}!")
    mensajesConsola.release()

    #Haya ganado o perdido, necesitan todos salir del lobby y moverse al menu principal
    SalirseDelLobbyDeJuego.release()

    mensajesConsola.acquire()
    print(f"Usuario: {jugadorIDWarzone} en espera de salir al menú")
    mensajesConsola.release()

    #Salio, el jugador, cargando para moverse al menú
    pantallaDeCarga.release()

    mensajesConsola.acquire()
    print(f"Cargando, esperando moverse a l menú, Usuario: {jugadorIDWarzone}")
    mensajesConsola.release()

    #adquiere su recompensa en experiencia
    mensajesConsola.acquire()
    print(f"Usuario: {jugadorIDWarzone}, obtuviste {randrange(10000)} puntos")
    mensajesConsola.release()
    recibirExperiencia.acquire()

    #jugador en el menu
    mensajesConsola.acquire()
    print(f"Usuario: {jugadorIDWarzone}, se encuentra en el menú")
    jugadoresPorPartida += 1
    print(f"Disponibilidad para mas jugadores: {jugadoresPorPartida}")
    mensajesConsola.release()

    jugadoresMaxEnSalaDeEspera.release()

def interaccionUsuarioEnWarzone():
    global jugadoresRestantesDelLobbyParaJugar

    while(1):
        #Se espera a la llegada de cliente
        mensajesConsola.acquire()
        print("Esperando a iniciar la partida")
        mensajesConsola.release()

        LobbysEnPartida.acquire()

        #Esperando a encontrar una sala para jugar
        LobbyDisponibles.acquire()

        #Ya dentro de una sala para competir
        mensajesConsola.acquire()
        print(f"Ya en espera de comenzar la partida")
        mensajesConsola.release()

        LobbyDisponibles.release()
        partidaFinalizada.release()

        #Inicializa la partida
        mensajesConsola.acquire()
        print(f"usted se encuetra jugando, suerte")
        mensajesConsola.release()

        SalirseDelLobbyDeJuego.acquire()

        #Se libera una silla para que pase otro cliente
        mensajesConsola.acquire()
        print("usted a terminado su partida")
        jugadoresRestantesDelLobbyParaJugar += 1
        print(f"Disponibilidad para mas jugadores: {jugadoresRestantesDelLobbyParaJugar}")
        mensajesConsola.release()

        esperandoInicializarPartida.release()

def inicializarPartida():
    while(1):
        #Pantalla de carga
        mensajesConsola.acquire()
        print("Cargando, pantalla de carga")
        mensajesConsola.release()
        
        pantallaDeCarga.acquire()

        #Actualizar el estado de lobby actual
        mensajesConsola.acquire()
        print("Cerrando Lobby")
        mensajesConsola.release()

        LobbyDisponibles.acquire()

        #Entregando experiencia
        mensajesConsola.acquire()
        print("Entrgando experiencia al jugador")
        mensajesConsola.release()

        LobbyDisponibles.release()
        recibirExperiencia.release()

def main():
    #Control de "disponibilidad" de usuarios y lobbys
    usuariosDisponibles     = 24
    lobbyDisponibles        = 6

    #Inicializamos a los usuarios
    listaDeHilosUsuario = []
    for x in range(lobbyDisponibles):
        usuario = Thread(target=interaccionUsuarioEnWarzone)
        usuario.setDaemon(True)
        listaDeHilosUsuario.append(usuario)
        usuario.start()

    #Inicializamos el "finalizar partida"

    cob = Thread(target=inicializarPartida)
    cob.setDaemon(True)
    cob.start()

    #Inicializamos los lobbys
    listaDeHilosLobby = []
    for c in range (usuariosDisponibles):
        lobby = Thread(target=desarrolloDelLobby, args=[c+1])
        lobby.setDaemon(True)
        listaDeHilosLobby.append(lobby)
        lobby.start()
        sleep(randrange(2))

    #for t in listaDeHilosLobby:
        #t.join()

main()