from os import system, name, chdir
from time import sleep  
from struct import unpack
#Este comando es mas para mí, ya que era "tedioso" escribir la carpeta a la cual se almacena los archivos cada vez que arrancaba el programa
directorio = '/home/carlosodette0803/sistop-2023-1/proyectos/2/DeLaCruzLopezCarlosOdette'
chdir(directorio)

####################################################################################################
################### Variables que son los valores establecidos por el proyecto  ####################
####################################################################################################

tamSector = 256#bytes
cantSectores = 4
cluster = tamSector * cantSectores#sectores
diskette = open('fiunamfs.img','r+b')
cantCluster = 4
medidaEntradaDirectorio = 64#Bytes
#La verdad no entiendo porque, pero se filtra bien si usamos esta estructura jajaja, se visualizo desde un print y por eso lo coloque así 
entradaNoUtilizados = b'---------------'
entradaNoUtilizadosSinEnconde = '---------------'
tamEntradas = len(entradaNoUtilizados) 
formato = '<I'

####################################################################################################
###########################  Funciones para la estetica de la interfaz   ###########################
####################################################################################################

#La siguiente función no tiene mucha ciencia, solo nos sirve para lo visual en el menú principal
def Menu():
    print("".center(73,"#"))
    print("  Menú principal  ".center(73,"#"))
    print("".center(73,"#"))
    print("#".ljust(35," "),end="")
    print("#".rjust(38," "))
    print("#\tsB".ljust(23," "),end=" ")
    print("-> Desplegar superBloque".ljust(30," "),end="\t\t#")
    #print("#\n#\tls".rjust(25," "),end=" ")
    #print('#'.rjust(38," "))
    print("\n#\tls".ljust(24," "),end=" ")
    print("-> Listar contenido del directorio".ljust(25," "),end="\t")
    print("#\n#\tcp".ljust(25," "),end=" ")
    print("-> Copiar archivo".ljust(33," "),end="\t\t")
    print("#\n#\trm".ljust(25," "),end=" ")
    print("-> Eliminar archivo de FiUnamFS".ljust(25," "),end="\t\t")
    print("#\n#\tdefrag".ljust(25," "),end=" ")
    print("-> Desfragmentar FiUnamFS".ljust(33," "),end="\t\t")
    print("#\n#\texit".ljust(25," "),end=" ")
    print("-> Salir de FiUnamFS".ljust(33," "),end="\t\t")
    print("#\n#".ljust(35," "),end="")
    print("#".rjust(40," "))
    print("".center(73,"#"))

#Esta funcion es "importante" ya que funciona como un switch-case, el cual nos redespliega las funciones correspondiente
def SeleccionarMenu(opcion):
    menuInteractivo = {'sB':superBloque,'ls':Instruccion_ls,'cp':Instruccion_cp,'rm':Instruccion_rm,'defrag':Instruccion_defrag,'exit': exit}
    menuInteractivo.get(opcion)() if opcion in menuInteractivo else print('No existe dicha opcion')

#Se creo una funcion que nos ayude a limpiar la pantalla, hace el analisis automaticamente para insertar el comando necesario si es windos o linux
def Limpiar():
    if name == "posix":
        system ("clear")
    elif name == "ce" or name == "nt" or name == "dos":
        system ("cls")

#Esta funcion nos ayuda a generar un mini delay para poder leer la información, y posteriormente nos limpia la pantalla para pasar a la siguiente instruccion
def Transicion():
    sleep(2)
    Limpiar()

#Se creo esta funcion para que nos creara el mismo formato al transicionar las instrucciones, solo le pasamos el texto que queremos que tenga 
#como principal
def InicioInterfaz(texto):
    print("".center(73,"#"))
    print(texto.center(73,"#"))
    print("".center(73,"#"))
    print("\n\n")

#Lo mismo que la funcion anterior, pero solo sirve para "cerrar" nuestra interfaz
def FinInterfaz():
    print("\n\n")
    print("".center(73,"#"))
    print("".center(73,"#"))
    print("".center(73,"#"))

def salto():
    print(''.center(73,'-'))
#PENDIENTE
#https://es.stackoverflow.com/questions/139223/se-puede-pasar-una-funci%C3%B3n-como-par%C3%A1metro-en-python
#Crear una función que reciba la función a ejecutar y el texto del inicio de cada instruccion, con el fin de dejar "limpia"
#Las intrucciones, en mi caso lo haré principalmente para usar la Instruccion_ls() sin que se cree su interfaz y poder 
#visualizarlo tambien en Instruccion_rm()
def InterfazInstruccion(función,textoPrincipal):
    pass

#Una simple función que solo imprime la "despedida" y limpia la pantalla antes de finalizar por completo
def Exit():
    print("Fin del programa!")
    Transicion()

####################################################################################################
#################  Funciones que realizan instrucciones requeridas en el proyecto  #################
####################################################################################################

def superBloque():
    global diskette, formato
    InicioInterfaz('  información de super bloque  ')
    diskette.seek(0)
    print(f"Nombre del sistema: {diskette.read(8).decode()}")
    diskette.seek(10)
    print(f"Version: {diskette.read(4).decode()}")
    diskette.seek(20)
    print(f"Etiqueta del volumen: {diskette.read(15).decode()}")
    diskette.seek(40)
    print(f"Tamaño de cluster: {unpack(formato,diskette.read(4))[0]}")
    diskette.seek(45)
    print(f"Numero de clusters por directorio: {unpack(formato,diskette.read(4))[0]}")
    diskette.seek(50)
    print(f"Numero de cluster que mide la unidad completa: {unpack(formato,diskette.read(4))[0]}")
    diskette.seek(0)
    FinInterfaz()
    Transicion()

#Se crea una funcion en la cual nos permitira visualizar el nombre de los archivos existentes en nuestro "diskette"
def Instruccion_ls():
    global diskette,cluster,medidaEntradaDirectorio,entradaNoUtilizados,tamEntradas
    #posicionamos el "cursor" al incio
    diskette.seek(0)
    #Imprimimos la interfaz
    InicioInterfaz('  Archivos del Diskette  ')
    #Realizamos un for que nos ayudara a visualizar las entradas
    for entrada in range(0,medidaEntradaDirectorio):
        #Calcularemos cada posicion de las entradas
        posicion = cluster + (entrada*medidaEntradaDirectorio)
        #Nos posicionaremos en la "posición" calculada previamente
        diskette.seek(posicion)
        #Almacenamos la lectura de dicha entrada para realizar una "limpieza" para descartar la cadena '-     '
        lectura = diskette.read(tamEntradas)
        #En caso de que la lectura recibida se diferente de '---------------' lo imprimirá
        if lectura != entradaNoUtilizados:
            #Como nuestro archivo tiene el formato '-    ' lo eliminamos usando un split y rescatamos unicamente el nombre del archivo
            diskette.seek(posicion+0)
            print(f"Tipo de archivo: {diskette.read(1).decode().strip()}")
            #posteriormente se captura los datos con el formato entregado
            diskette.seek(posicion+1)
            print(f"Archivo: {diskette.read(15).decode().strip()}")
            diskette.seek(posicion + 16)
            #print(f'Tamaño del archivo: {diskette.read(5).decode()}')
            diskette.seek(posicion + 20)
            print(f'Cluster inicial: {diskette.read(4).decode()}')
            diskette.seek(posicion + 24)
            fechaHora = diskette.read(14).decode()
            print(f"Hora y fecha de creación del archivo: {fechaHora[0:4]}-{fechaHora[4:6]}-{fechaHora[6:8]}  {fechaHora[8:10]}:{fechaHora[10:12]}:{fechaHora[12:14]}")
            diskette.seek(posicion + 38)
            fechaHora = diskette.read(14).decode()
            print(f"Hora y fecha de ultima modificacion del archivo: {fechaHora[0:4]}-{fechaHora[4:6]}-{fechaHora[6:8]}  {fechaHora[8:10]}:{fechaHora[10:12]}:{fechaHora[12:14]}")
            diskette.seek(posicion + 52)
            print(f'Espacio no utilizado: {diskette.read(13).decode()}')
            salto()
    #Imprimos el final de esta interfaz
    FinInterfaz()
    #Limpiamos y pasamos a la siguiente instruccion
    Transicion()
    #Regresamos la lecturas desde un principio 
    diskette.seek(0)

#Se crea una funcion en la cual nos permitira copiar un archivo del "diskette" a un directorio de nuestra computadora
def Instruccion_cp():
    global diskette, medidaEntradaDirectorio, cluster, tamEntradas
    InicioInterfaz('  Copiar archivo de nuestro diskette  ')
    #Solicitamos el nombre del archivo que deseamos copiar
    archivoACopiar = input("Ingresa el nombre del archivo ubicado en el Diskette que deseas copiar\nCopiar: ")
    #Seguimos realizando la busqueda de cada entrada
    for entrada in range(0, medidaEntradaDirectorio):
        #Calculamos la posicion de la respectiva entrada
        posicion = cluster + (entrada * medidaEntradaDirectorio)
        #Nos posicionamos para poder realizar la lectura
        diskette.seek(posicion)
        #Obtenemos la lectura de la posición correspondiente
        lectura = diskette.read(tamEntradas)
        #Obtenemos la lectura inicial
        diskette.read(1)#Reinciamos la lectura
        #Realizamos una condición para ver si existe el archivo en el diskette, en caso de que no lanza una alerta, en caso 
        # afirmativo procederá a pedir el directorio que sea necesario almacenarlo
        existeArchivo = True if (len(lectura.decode().split()) == 2 and lectura.decode().split()[1] == archivoACopiar) else 0#Usamossplit, ya que extrae mi entrada de direccion '-      nombredel.archivo', entonces solo capturamos el nombre
        #Si existe pedimos el directorio
        if existeArchivo:
            #ejemplo para la documentacion: /home/carlosodette0803/Descargas/ejemploParaElProyecto
            direccion = input("Ingresa la direccion donde se almacenará la copia\nDireccion: ")
            #Obtenemos la longitud que se debera leer
            longitud = unpack(formato,diskette.read(4))[0]
            #Obtenemos el inicio que se debera leer
            inicio = unpack(formato, diskette.read(4))[0]
            #Posicionamos el cursor para obtener el inicio del archivo
            diskette.seek(cluster*inicio)
            #capturamos el contenido del archivo
            contenido = diskette.read(longitud)
            #Creamos un nuevo archivo, que se almacenará en el directorio que selecciono el usuario y le daremos el mismo nombre ya que es una copia
            crearArchivo = open(direccion+'/'+lectura.decode().split()[1],'wb')
            #Le damos el contenido de nuestro respectivo archivo previamente creado para que tenga los mismos datos
            crearArchivo.write(contenido)
            #Cerramos el archivo para que se guarde correctamente
            crearArchivo.close()
            #Ya que lo encuentra no es necesario que siga realizando una busqueda así que paramos abruptamente el loop, cuando se crea nuestra copia
            break
    #Realizamos una impresion donde notificamos si se logró o no por la existencia del archivo
    print(f"Copiado exitosamente al directorio {direccion}") if existeArchivo else print('Ese archivo no existe en nuestro diskette')
    FinInterfaz()
    Transicion()

#Se crea una función que nos permitira eliminar cualquier archivo existente en el "diskette"
def Instruccion_rm():
    global tamEntradas, diskette, cluster, entradaNoUtilizados
    #Creamos el titulo de nuestra pantalla
    InicioInterfaz('  Eliminar archivo almacenado en la unidad  ')
    #Recibimos el nombre del archivo que queremos eliminar
    archivo_a_eliminar = input("Ingresa el archivo que deseas eliminar del diskette:\t")
    #Realizamos un recorrido para obtener las entradas
    for entrada in range (0,medidaEntradaDirectorio):
        #Obtenemos la posicion de cada entrada
        posicion = cluster + (entrada * medidaEntradaDirectorio)
        #Colocamos el apuntador al inicio de cada entrada
        diskette.seek(posicion)
        #Almacenamos la lectura del tamaño de la entrada
        lectura = diskette.read(tamEntradas)
        #Analizamos si existe el archivo que queremos eliminar en nuestro "diskette"
        existeArchivo = True if len(lectura.decode().split()) == 2 and lectura.decode().split()[1] == archivo_a_eliminar else False
        #En caso de que exista, procedemos a eliminar el archivo 
        if existeArchivo:
            #Nos posicionamos en donde se encuentra nuestro archvio
            diskette.seek(posicion)
            #y lo "eliminamos" rescribiendo el nombre del archivo, con la marca de las entradas no utilizadas
            diskette.write(entradaNoUtilizadosSinEnconde.encode())
            #Así como en cp, una vez eliminado el archivo, terminamos el loop ya que no es necesario encontrar otro con el mismo nombre
            break
    #Realizamos la advertencia donde notificamos si se logra eliminar o no se encuentra el archivo que se desea eliminar
    print(f"El archivo: {archivo_a_eliminar}, fue eliminado exitosamente") if existeArchivo else print(f"El archivo: {archivo_a_eliminar}, no existe en la unidad")
    FinInterfaz()

def Instruccion_defrag():
    pass

####################################################################################################
####################################### Inicio del programa  #######################################
####################################################################################################

def Main():
    #Limpiamos la pantalla para que este libre para la ejecucion del programa
    Limpiar()
    #Inicializamos el valor de opcion
    opcion = None
    while(opcion!='exit'):
        #Imprimimos la interfaz del menú
        Menu()
        #Capturamos la opcion que requerimos
        opcion = input("Opcion: ")
        #Limpiamos la pantalla
        Limpiar()
        #Nos lanza la funcion que requeriamos
        SeleccionarMenu(opcion)
        #Realizamos un delay
        sleep(1)

#Comenzamos el programa
Main()

