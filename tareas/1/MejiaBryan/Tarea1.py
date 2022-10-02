# Simulacion de memoria contigua
#Programa de Mejia Ramos Bryan
memoria = ["-","A","A","A","B","B","-","-","-","-", #memoria de 30 unidades de memoria
           "-","-","-","-","-","-","-","-","-","-",
           "-","-","-","-","-","-","-","-","-","-"]
continuar = "S" #Bandera para bucle
procesos = ""   #Variable auxiliar
anterior = ""   #Variable auxiliar
           
def imprimirmemoria(): #Funcion que imprime la memoria y genera la cadena de todos los procesos
    global procesos
    global anterior
    
    procesos = ""
    anterior = ""
    for i in range(0,30):
        if anterior != memoria[i] and memoria[i] != "-":
            procesos = procesos + memoria[i] + " "
            anterior = memoria[i]
        print(memoria[i], end = "")
    
def primerEspacio(unidades, proceso): #Funcion que busca el primer lugar para agregar un proceso nuevo
    espacio = 0                       #Cuenta el numero total de espacios en la memoria
    flag = False                      #Cuenta el numero maximo de espacios consecutivos
    espacioTotal = 0                  #Verifica si cabe el proceso que se quiere agregar
    maximoEspacio = 0                 #Realiza la compactacion de espacios
    
    for i in range(0,30):
        if memoria[i] == "-":
            espacio+=1
            espacioTotal+=1
            
        if espacio >= int(unidades):
            for j in range(i-espacio+1,i-espacio+int(unidades)+1):
                memoria[j] = proceso
            flag = True
            break
        
        if memoria[i] != "-" or i == 29:
            if maximoEspacio < espacio:
                maximoEspacio = espacio
            espacio = 0
            
    if espacioTotal < int(unidades):
        print("No hay espacio suficiente para agregar el proceso :c")
        
    elif flag == False:
        print("Se necesita "+unidades+" unidades, pero solo tengo "+str(maximoEspacio)+" unidades consecutivas :(")
        print("Compactacion requerida c:")
        for t in range(0,espacioTotal):
            memoria.remove("-")
        for t in range(0,espacioTotal):
            memoria.append("-")
        print("\nMemoria nueva:")
        imprimirmemoria()
        print("Agregando el proceso "+proceso+" :D")
        for t in range(30-espacioTotal,30-espacioTotal+int(unidades)):
            memoria[t] = proceso
        
while continuar != "N": #Bucle principal
    print("Memoria actual:")
    imprimirmemoria()
    print("\nAsignar 0, liberar 1: ")
    accion = input()

    if accion == "1":   #Opcion de liberar un proceso
        print("\n¿Que proceso quiere liberar? :D ("+procesos+")")
        proceso = input()
        for i in range(0,30):
            if memoria[i] == proceso:
                memoria[i] = "-"

    elif accion == "0": #Opcion de agregar un nuevo proceso
        print("\n¿Que nuevo proceso quieres asignar? :)")
        newProceso = input()
        print("¿Cuantas unidades necesita el nuevo proceso?")
        unidades = input()
        primerEspacio(unidades, newProceso)
        
    print("Quieres continuar: S/N")
    continuar = input()