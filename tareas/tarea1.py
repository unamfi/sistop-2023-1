'''
Alumnos: Camacho Lara Ana Laura
         Pérez Palomeque José Mauricio
Programa que simula el proceso que el sistema operativo lleva acabo a la hora de asignar y liberar porciones de la memoria conforme lo requiere el conjunto de
procesos, a través del algoritmo de mejor ajuste
'''

def espaciosDisponibles(memoria):
    banderaEspacio = 0
    posicionEspacioDisponible = []
    numeroEspaciosDisponibles = []
    auxBloquesDeEspacios = 0
    for i in range(len(memoria)):
        if memoria[i] == '-':
            if banderaEspacio == 0:
                banderaEspacio = 1
                posicionEspacioDisponible.append(i) #Encuentra un espacio y guarda su posición en la lista original
                numeroEspaciosDisponibles.append(1) #Inicializa con 1 el espacio disponible para luego sumar la cantidad de espacios consecutivos que constituirán un bloque
            else: #Si la bandera está prendida quiere decir que se están contando los espacios disponibles en un bloque
                numeroEspaciosDisponibles[len(numeroEspaciosDisponibles)-1] += 1
                if i != len(memoria)-1:
                    if memoria[i+1] != '-':
                        banderaEspacio = 0
        else: #Cambia la bandera a 0 cuando se dejó de encontrar "-" en la lista
            benaderaEspacio = 0

    return posicionEspacioDisponible,numeroEspaciosDisponibles

def mejorAjuste(memoria,nombreProceso,tamañoProceso):
    posicionInsercion = -1
    auxMejorTamaño = -1
    pEspacio, cEspacio = espaciosDisponibles(memoria)
    for i in range(len(cEspacio)):
        if tamañoProceso > cEspacio[i]:
            print("Calculando espacio óptimo")
        else:
            if auxMejorTamaño == -1:
                auxMejorTamaño = cEspacio[i]
                posicionInsercion = i
            else:
                if auxMejorTamaño >= tamañoProceso:
                    posicionInsercion = i

    if auxMejorTamaño == -1: #Si el tamaño no ha cambiado de su valor por default, quiere decir que no hubo espacio disponible en ningún bloque
        auxSumaBloques = 0
        for i in range(len(cEspacio)):
            auxSumaBloques += cEspacio[i]
        if auxSumaBloques >= tamañoProceso:
            print(f"Existe espacio suficiente para el proceso de tamaño {tamañoProceso} realizando una compactacion")
            memoria = compactacion(memoria)
            auxEspacioNuevo = memoria.index("-")
            for i in range(tamañoProceso):
                memoria[auxEspacioNuevo+i] = nombreProceso
        else:
            print("No hay espacio disponible para el tamaño del proceso")
    else: #Si el tamaño ha cambiado su valor por default, quiere decir que hay espacio disponible en algún bloque
        for i in range(tamañoProceso):
            memoria[pEspacio[posicionInsercion]+(i)] = nombreProceso

    print(f'Memoria actualizada:\n {memoria}')

def liberar(memoria,procesoLiberar):
    newMemoria = [p.replace(procesoLiberar, '-') for p in memoria]
    memoria=newMemoria
    print(f'Memoria actualizada:\n {memoria}')

def compactacion(memoria):
    newM=[]
    for i in range (len(memoria)):
        if memoria[i] != '-':
            newM.append(memoria[i])
    for i in range (len(memoria)):
        if memoria[i] == '-':
            newM.append(memoria[i])
    memoria = newM
    return memoria

def main():
    memoria = ['A','A','B','B','B','B','-','-','-','-','D','D','D','D','D','D','E','E','E','E','-','-','-','H','H','H','I','I','-','-']
    print(f'Memoria actual:\n{memoria}')
    op = input("1)Asignar proceso \n2)Liberar proceso \n")
    if op == '1':
        nombreProceso = input("Nombre del proceso a introducir: ")
        tamañoProceso = int(input("Tamaño del proceso: "))
        mejorAjuste(memoria,nombreProceso,tamañoProceso)
    else:
        procesoLiberar = input("Nombre del proceso a liberar: ")
        liberar(memoria,procesoLiberar)



main()
