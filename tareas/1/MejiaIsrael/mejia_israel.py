
from concurrent.futures import process


salir = False
process_list = [
                'A','A','-','-','B'
               ,'B','C','C','-','-'
               ,'D','-','D','D','D'
               ,'D','E','-','-','-'
               ,'-','-','-','H','H'
               ,'H','-','I','-','-'
               ] #30 procesos iniciales 



def mostrar_salida():
    print('\nPor ultimo, deseas salir del administrador de procesos?')
    saliir = int(input('1 = Si        2= No \n\t'))
    if saliir == 1:
        print('Un gusto verte por aqui, hasta luego :)')
        saliir = True
    else :
        saliir = False
    return saliir

def asigna_o_compacta(p_name, u) :
    index = 0
    continuous_space_count = 0
    spaces_available = 0
    insercion_compactada = False
    
    for index in len(process_list):
        if process_list[index] == '-' :
            continuous_space_count += 1
            spaces_available += continuous_space_count
            if continuous_space_count > u :
                print('\tSi hay suficiente memoria contigua')
                #aqui sabemos el indice de insercion_contigua 
        else:
            spaces_available += continuous_space_count
            continuous_space_count = 0
            insercion_compactada = True
    
    #Despues de este ciclo ya sabemos en que parte de la lista hay la memoria suficiente, ya sea continua o compactada
    if insercion_compactada == True :   
        print('\tNecesito realizar una compactacion de memoria, para poder ingresar el nuevo proceso, estoy en eso ;) ')
    else:
        print('Procedere a insertar la memoria del proceso')


def corrobora_memoria(process_name , unidades):
    p_name = process_name
    u = unidades
    space = 0
    for p in process_list:
        if p == '-':
            space +=1

    if space > unidades:
        print(f'\t\ttenemos {space} unidades disponibles, si podemos hacer la asignacion :D')
        asigna_o_compacta(p_name, u)
    else:
        print(f'\t\ttenemos {space} unidades disponibles, NO hay memoria suficiente :c')


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
    print('Funcion de LIBERAR activada xd')



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
    
