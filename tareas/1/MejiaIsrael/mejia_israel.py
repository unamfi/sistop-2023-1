
from concurrent.futures import process


salir = False
process_list = [
                'A','A','B','B','B'
               ,'B','C','C','C','C'
               ,'D','D','D','D','D'
               ,'D','E','E','E','E'
               ,'-','-','-','H','H'
               ,'H','I','I','-','-'
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



def asignar():
    print('Funcion de ASIGNAR activada xd')



def liberar():
    print('Funcion de LIBERAR activada xd')



while salir == False:
    print('\n\t\tBienvenido al administrador de procesos de Israel Mejia :D\n')
    print(f'A continuacion puedes ver los procesos actuales, cada letra representa una unidad de procesamiento del respectivo proceso: \n {process_list}')
    print('Ahora bien, que accion desea realizar?')
    accion = int(input('\tAsignar (0)     o   liberar (1) \n\t'))
    if accion == 0:
        asignar()
    elif accion == 1:
        liberar()
    else:
        print('\t\tOpcion no valida')

    salir = mostrar_salida()
    
