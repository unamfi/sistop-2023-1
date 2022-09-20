
salir = False
process_list = [
                'A','A','-','-','B'
               ,'B','C','C','-','-'
               ,'D','-','D','D','D'
               ,'D','E','-','-','-'
               ,'-','-','-','H','H'
               ,'H','-','-','-','-'
               ] #30 procesos iniciales 



def mostrar_salida():
    print('\nPor ultimo, deseas salir del administrador de procesos?')
    saliir = int(input('1 = Si        2= No \n\t'))
    if saliir == 1:
        print('Un gusto verte por aqui, hasta luego :)\n\n')
        saliir = True
    else :
        saliir = False
    return saliir

#def compactando_memoria():
def compactando_memoria(process_list):
    compact_list = []
    print(f'\t\tLista original : \n\t\t{process_list}\n')
    for item in process_list:
        if item != "-":
            compact_list.append(item)
    print(f'\t\tLista sin espacios: \n\t\t{compact_list}')

    while len(compact_list) < 30:
        compact_list.append("-") #rellenando espacios vacios
    print(f'\t\tLista compactada : \n\t\t{compact_list}')
    process_list = compact_list
    return compact_list

def insertando(insertion_index, p_name, u, insercion_compactada, process_list) :
    if insercion_compactada == False:
        while u > 0 :
            process_list[insertion_index] = p_name
            insertion_index += 1 #Avanzamos a la siguiente insercion
            u -= 1 #Reducimos el contador de unidades de memoria a insertar del proceso 
    else:
        index_compact_space = 0 
        for item in process_list:
            if item != '-':
                index_compact_space +=1
            else: 
                break
        while u > 0 :
            process_list[index_compact_space] = p_name
            index_compact_space += 1 #Avanzamos a la siguiente insercion
            u -= 1 
    print(f'\tMemoria insertada correctamente, lista de procesos actualizada: \n\t{process_list}')
    return process_list    
        


def asigna_o_compacta(p_name, u, process_list) :
#def asigna_o_compacta(p_name, u ) :
    index = 1
    continuous_space_count = 0
    spaces_available = 0
    insercion_compactada = False
    first_unit_available = False  #Para activar logica despues de que se haya encontrado un espacio de memoria disponible

    for item in process_list :
        if item != '-' and first_unit_available ==  False:
            pass 
        else:
            first_unit_available = True #Ya se encontro al menos un elemento disponible de memoria para iniciar la cuenta
            if item == '-' :
                continuous_space_count += 1
                spaces_available += continuous_space_count
                if continuous_space_count >= u :
                    print('\tSi hay suficiente memoria contigua')
                    break
                    #aqui sabemos el indice de insercion_contigua 
            else:
                spaces_available += continuous_space_count
                continuous_space_count = 0
                insercion_compactada = True
                if spaces_available >= u :
                    print('\tProcedere a compactar la memoria para realizar la insercion')
                    break
        index += 1
    
    #Despues de este ciclo ya sabemos en que parte de la lista hay la memoria suficiente, ya sea continua o compactada
    insertion_index = index - u
    if insercion_compactada == True :   
        print('\tcompactando... ')
        process_list = compactando_memoria(process_list)
        #process_list = process_list2
        process_list = insertando(insertion_index, p_name, u, insercion_compactada, process_list)     
    else:
        print('\tProcedere a insertar la memoria del proceso')
        print(f'insertion = {insertion_index} \t p_name = {p_name} \t u = {u}')
        process_list = insertando(insertion_index, p_name, u, insercion_compactada, process_list) 

    return process_list




def corrobora_memoria(process_name , unidades):
    p_name = process_name
    u = unidades
    space = 0
    for p in process_list:
        if p == '-': 
            space +=1

    if space > unidades:
        print(f'\t\ttenemos {space} unidades disponibles, si podemos hacer la asignacion :D')
        process_list = asigna_o_compacta(p_name, u, process_list)
        #asigna_o_compacta(p_name, u )
    else:
        print(f'\t\ttenemos {space} unidades disponibles, NO hay memoria suficiente :c')
    return process_list


def asignar():
    print('\n\tCreando nueva Asignaicion de proceso')
    print('\t\t-Recuerda que solo puedes asignar procesos que tengan entre 2 y 15 unidades de memoria')
    print('\t\t-No puede haber procesos con el mismo nombe (letra ya utilizada sin importar mayusculas o minusculas)')
    
    process_name = (input('\tInserte letra que nombra al proceso: \t')).upper()
    if process_name in process_list:
        print('\t\t\tNombre de proceso Invalido')
    else:
        unidades = int(input('\tDe cuantas unidades de memoria sera el nuevo proceso ?  '))
        if ( unidades > 1 and unidades < 16 ):
            print(f'\tListo, el nuevo proceso a asignar sera:\t {process_name}  con {unidades} unidades de memoria')
            print('\tCorroborando si hay memoria disponible para hacer la asignaicion...')
            corrobora_memoria(process_name , unidades)
        else:
            print('\t\t\tCantidad de unidades de memoria invalido')





def liberar():
    n_pr = input('\t Cual es el nombre del proceso que desea eliminar?\t')
    index_liberacion = 0
    for item in process_list:
        if item == n_pr:
            process_list[index_liberacion] = "-"
        index_liberacion +=1
    print(f'\tMemoria liberada, lista de procesos: \n\t{process_list}')    




while salir == False:
    print('\n\t\tBienvenido al administrador de procesos de Israel Mejia :D\n')
    print(f'A continuacion puedes ver los procesos actuales, cada letra representa una unidad de memoria del respectivo proceso: \n {process_list}')
    print('Ahora bien, que accion desea realizar?')
    accion = int(input('\tAsignar (0)     o   liberar (1) \n\t'))
    if accion == 0:
        asignar()
    elif accion == 1:
        liberar()
    else:
        print('\t\tOpcion no valida')

    salir = mostrar_salida()
    
 