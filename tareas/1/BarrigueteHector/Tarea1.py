'''
Barriguete Rodrríguez Héctor Alejandro
Tarea #1

Punto #3: las solicitudes se están resolviendo por primer ajuste (se asigna el proceso a un bloque con el tamaño necesario para alojarlo).
'''

def asignar(lista, lista_procesos, espacios):
    lista_actual = ''.join(lista)
    contador = 0
    inicio = 0
    aviso = 0
    
    nuevo = input("\nIngresa el nuevo elemento: ")    
    cantidad = int(input("Ingresa la longitud del nuevo elemento: "))
    
    if espacios - cantidad < 0:
        print("\nEl nuevo proceso es muy grande y no hay suficiente memoria para almacenarlo\nMemoria disponible:", espacios)
        return lista, lista_procesos, espacios
    
    espacios = espacios - cantidad

    if nuevo not in lista_procesos:
        lista_procesos.append(nuevo)

    for elemento in lista:
        if elemento == '-' and contador == cantidad:
            for i in range(inicio, inicio + contador):
                lista[i] = nuevo
            aviso = 1
            break
        elif elemento == '-':
            contador += 1
        elif elemento != '-':
            inicio += 1
            inicio += contador
            contador = 0     

    if aviso == 0:
        print("\nNo hay suficiente memoria para almacenar el proceso, es necesario realizar una compactacion de memoria")
        lista = compactar(lista)
        lista_actual = ''.join(lista)
        contador = 0; inicio = 0
        for elemento in lista:
            if elemento == '-' and contador == cantidad:
                for i in range(inicio, inicio + contador):
                    lista[i] = nuevo
                break
            elif elemento == '-':
                contador += 1
            elif elemento != '-':
                inicio += 1
                inicio += contador
                contador = 0     
        
        

    lista_formato = ''.join(lista)
    print("\nAsignación actual:\n" + lista_actual + "\nAsignar (0) o liberar (1): 0\nNuevo proceso ("+ nuevo +"):", cantidad, "\nNueva asignacion:\n" + lista_formato)
    
    return lista, lista_procesos, espacios

def liberar(lista, lista_procesos, espacios):
    contador = 0;
    lista_actual = ''.join(lista)
    procesos_formato = ''.join(lista_procesos)
    quitar = input("\nIngresa el proceso a quitar: ")

    if quitar not in lista_procesos:
        print("\nNo existe el proceso")
        return lista, lista_procesos, espacios
    
    for elemento in lista:
        if quitar == elemento:
            lista[contador] = '-'
        contador += 1

    espacios += contador
    
    lista_formato = ''.join(lista)
    print("\nAsignación actual:\n", lista_actual, "\nAsignar (0) o liberar (1): 1\nProceso a liberar (" + procesos_formato + ")\nAsignacion actual:\n" + lista_formato)
    lista_procesos.remove(quitar)

    return lista, lista_procesos, espacios

def compactar(lista):
    for elemento in lista:
        if elemento == '-':
            lista.remove(elemento)
            lista.append('-')
    
    lista_actual = ''.join(lista)
    print("\nResultado de la compactacion:\n" + lista_actual)

    return lista

def main():
    lista = ['-'] * 30
    lista_procesos = []
    opcion = 0 
    espacios = 30;

    while opcion != 3:
        opcion = int(input("\n------------ Menu ------------\n1. Asignar memoria\n2. Liberar memoria\n3. Salir\nOpcion: "))
        if opcion == 1:
            lista, lista_procesos, espacios = asignar(lista, lista_procesos, espacios)
        elif opcion == 2:
            lista, lista_procesos, espacios = liberar(lista, lista_procesos, espacios)
        elif opcion == 3:
            print("\nGracias por usar el programa")
        else:
            print("\nOpcion invalida")

main()