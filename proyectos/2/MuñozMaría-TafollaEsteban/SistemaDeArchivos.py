#Bibliotecas
#732,160
import struct
import os
import time
import datetime
import math

NOMBRE_IMAGEN = "fiunamfs.img"
archivos=[]
mapaAlmacenamiento = []
imagen = open(NOMBRE_IMAGEN,"br+")

def sacaDatos(inicio, tamanio):
    global imagen
    imagen.seek(inicio)
    return imagen.read(tamanio)

def sacaDatosAscii(inicio, tamanio):
    global imagen
    imagen.seek(inicio)
    return imagen.read(tamanio).decode("ascii")

def datoUnpack(inicio, tamanio):
    global imagen
    imagen.seek(inicio)
    dato = imagen.read(tamanio)
    return struct.unpack('<i', dato)[0]

tamanioCluster= datoUnpack(40,4) #Da 1024
clustersDirectorio = datoUnpack(45,4) #Da 4
clustersUnidad = datoUnpack(50,4) #Da 720
tamanioDirectorio = 64

def iniciaMapa():
    global mapaAlmacenamiento
    for x in range(5):
        mapaAlmacenamiento.append(1)
    while (len(mapaAlmacenamiento) != 720):
        mapaAlmacenamiento.append(0)

class archivo:
    global tamanioCluster
    def __init__(self, nombre, tamanio, clusterInicial, fechaCreacion, fechaModificacion):
        self.nombre = nombre.replace(" ","")
        self.tamanio = tamanio
        self.clusterInicial = clusterInicial
        self.fechaCreacion = fechaCreacion
        self.fechaModificacion = fechaModificacion
        self.numClusters = math.ceil(tamanio/tamanioCluster)

def sacaDatosArchivo(posicion):
    inicial = 1024 + (posicion * 64)
    if(sacaDatosAscii(inicial+1,14) != "--------------"):
        tipo = sacaDatosAscii(inicial,1)#borrar
        nombre = sacaDatosAscii(inicial+1, 14)
        tamanio = datoUnpack(inicial+16, 4)
        clusterInicial = datoUnpack(inicial+20,4)
        fechaCreacion = sacaDatosAscii(inicial+24, 14)
        fechaModificacion = sacaDatosAscii(inicial+38, 14)
        archivoAux = archivo(nombre, tamanio, clusterInicial, fechaCreacion, fechaModificacion)
        print(tipo, nombre, tamanio, clusterInicial, fechaCreacion, fechaModificacion, archivoAux.numClusters) #borrar
        return archivoAux
        
def inicializaArchivos():
    global archivos
    numArchivos = int((tamanioCluster * clustersDirectorio)/tamanioDirectorio)
    for x in range(numArchivos):
        resultado = sacaDatosArchivo(x)
        if(resultado != None):
            archivos.append(resultado)
            actualizaMapa()

#Método que enlista los contenidos del directorio
def muestraDirectorio():
    global archivos
    for x in archivos:
        print(x.nombre, x.clusterInicial)


def actualizaMapa():
    global mapaAlmacenamiento
    global archivos
    for x in range(720):
        mapaAlmacenamiento[x]=0
    for x in range(5):
        mapaAlmacenamiento[x]=1
    for archivoActual in archivos:
        aux = archivoActual.numClusters
        for j in range(aux):
            mapaAlmacenamiento[archivoActual.clusterInicial+j] = 1
    #print(mapaAlmacenamiento)#borrar

#Método que copia un archivo desde el sistema de archivos a la computadora 
#Devolvera -1 en caso de no encotrar el archivo    
def buscaArchivoNombre(nombre):
    global archivos
    for x in archivos:
        #print("comparamos", x.nombre, "con", nombre)
        if(x.nombre==nombre):
            return archivos.index(x)
    return -1

def buscaArchivoClusterInicial(clusterInicial):#borrar?
    global archivos
    for x in archivos:
        #print("comparamos", x.nombre, "con", nombre)
        if(x.clusterInicial==clusterInicial):
            return archivos.index(x)
    return -1

#Método que copia un archivo desde el sistema de archivos a la computadora 
def copiaArchivoAComputadora(nombreArchivo, ruta):
    global archivos
    global imagen
    
    #busca si el nombre del archvo se encuentra en nuestro sistema de archivos.
    posicion = buscaArchivoNombre(nombreArchivo)
    if(posicion != -1):
        auxiliar = sacaDatos(archivos[posicion].clusterInicial*1024,archivos[posicion].tamanio)
        #print(auxiliar)
        if(os.path.exists(ruta) and not os.path.exists(ruta+"/"+nombreArchivo)):
            print("Se puede copiar el archivo")
            ArchivoNuevo = open(ruta+"/"+nombreArchivo, "bw")
            ArchivoNuevo.write(auxiliar)
            ArchivoNuevo.close()
        else:
            print("No se puede copiar el archivo if 2")
    else:
        print("No se puede copiar el archivo if 1")

def borraEnDirectorio(posicion):
    global imagen
    inicial = 1024 + (posicion * 64)
    imagen.seek(inicial)
    imagen.write(b'---------------'+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'+b'0000000000000000000000000000'+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    
    
#Método que borra un archivo de nuestro sistema de archivos
def borraArchivo(nombreArchivo, archivos):
    for x in archivos:
        if(x.nombre==nombreArchivo):           
            archivos.pop(archivos.index(x))
            actualizaMapa()
            for y in range(64):
                inicial = 1024 + (y * 64)
                nombre = sacaDatosAscii(inicial+1, 14).replace(" ","")
                if(nombre == nombreArchivo):
                    borraEnDirectorio(y)
                    return
    print("El archivo para borrar no existe")
    return 

#Método que copia un archivo desde nuestra computadora a nuestro sistema de archivos.
def copiaArchivoAImagen(rutaOrigen):
    global archivos
    #verifica que el archivo exista, que el tamaño del nombre sea de 14 o menos y que el tamaño del archivo sea de menos de 732,160 bytes (715 clusters)
    if(os.path.exists(rutaOrigen) and len(os.path.split(rutaOrigen)[-1].replace(" ","")) < 15 and os.stat(rutaOrigen).st_size < 732160):
        #verificamos que no exista un archivo en el sistema con el mismo nombre
        if(buscaArchivoNombre(os.path.split(rutaOrigen)[-1]==-1)):
            nombre=os.path.split(rutaOrigen)[-1]
            tamanio = os.stat(rutaOrigen).st_size
            clusterInicial = asignaCluster(tamanio)
            fechaCreacion = datetime.datetime.strptime(time.ctime(os.stat(rutaOrigen).st_ctime), "%a %b %d %H:%M:%S %Y").strftime("%Y%m%d%H%M%S")
            fechaModificacion = datetime.datetime.strptime(time.ctime(os.stat(rutaOrigen).st_mtime), "%a %b %d %H:%M:%S %Y").strftime("%Y%m%d%H%M%S")
            archivoAux = archivo(nombre, tamanio, clusterInicial, fechaCreacion, fechaModificacion)
            
def asignaCluster(tam):
    global mapaAlmacenamiento
    try:
        clusterInicialPosible = mapaAlmacenamiento.index(0)
    except:
        print("Ya no hay espacio en el dipositivo para almacenar")
        return -1
    clustersDeArchivo = math.ceil(tam/tamanioCluster)
    if(clusterInicialPosible+clustersDeArchivo<720):
        return clusterInicialPosible
    else:
        return -1
    #print("cluster inicial posible", clusterInicialPosible)
def agregaEspacios(nombre):
    while(len(nombre) != 14):
        nombre = " " + nombre
    return nombre

def desfragmentar():
    global archivos
    global imagen
    global mapaAlmacenamiento 
    espacioLibre = 0
    posicionMapa = -1
    for x in mapaAlmacenamiento:
        posicionMapa += 1
        if (x == 0):
            espacioLibre += 1
        elif(x == 1 and espacioLibre != 0):
            #poner el archivo en su nuevo lugar de la imagen
            moverArchivoEnImagen(posicionMapa, espacioLibre)
            #actualizar su cluster inicial en archivos
            actualizarArchivos(posicionMapa, espacioLibre)
            #actualizar directorio
            actualizarDirectorio()
            espacioLibre = 0

def moverArchivoEnImagen(posicionMapa, espacioLibre):
    global imagen
    global archivos

    imagen.seek(posicionMapa*tamanioCluster)
    tamanio = archivos[buscaArchivoClusterInicial(posicionMapa)].tamanio
    contenido = imagen.read(tamanio)
    imagen.seek(posicionMapa*tamanioCluster-espacioLibre*tamanioCluster)
    imagen.write(contenido)

def actualizarArchivos(posicionMapa, espacioLibre):
    global archivos
    nuevoClusterInicial = posicionMapa-espacioLibre
    archivos[buscaArchivoClusterInicial(posicionMapa)].clusterInicial = nuevoClusterInicial
    actualizaMapa()

def actualizarDirectorio():
    global archivos
    for y in range(64):
        resultado = sacaDatosArchivo(y)
        
        if(resultado != None  ):
            posicionArchivo = buscaArchivoNombre(resultado.nombre)
            if(archivos[posicionArchivo] != -1):
                inicial = 1024 + (y * 64)
                imagen.seek(inicial+20)
                almacen = struct.pack('<i', (archivos[posicionArchivo].clusterInicial))
                almacen2 = 1354
                print("El resultado de la nueva asignacion de la desframentacion es", almacen)
                imagen.write(almacen)


def inicio():
    print("1.")
    iniciaMapa()
    print("2.")
    inicializaArchivos()
    print("Directorio:")
    muestraDirectorio()
    #copiaArchivoAComputadora("logo.png","C:/Users/steph/Desktop/Tareas 7mosemestre")
    #borraArchivo("mensajes.png", archivos)
    #copiaArchivoAImagen("C:/Users/steph/Desktop/Tareas 7mosemestre/Ta folla.pdf")
    #print(mapaAlmacenamiento)
    desfragmentar()
    muestraDirectorio()
    asignaCluster(100)
    #copiaArchivoAComputadora("README.org","C:/Users/steph/Desktop/Tareas 7mosemestre")
    #copiaArchivoAComputadora("logo.png","C:/Users/steph/Desktop/Tareas 7mosemestre")
    copiaArchivoAComputadora("mensajes.png","C:/Users/steph/Desktop/Tareas 7mosemestre")
    #print(mapaAlmacenamiento)

"""""""""    
print("Saca datos:")
sacaDatosArchivo(0)
nombreSistema = sacaDatosAscii(0,8)
version = sacaDatosAscii(10,4)
etiqueta = sacaDatosAscii(20,5)
print(nombreSistema, version, etiqueta)
"""

tamanioCluster= datoUnpack(40,4) #Da 1024
print(tamanioCluster)
clustersDirectorio = datoUnpack(45,4) #Da 4
print(clustersDirectorio)
clustersUnidad = datoUnpack(50,4) #Da 720
print(clustersUnidad)
tamanioDirectorio = 64

"""
nombreArchivo = sacaDatosAscii(1025,14)
print(nombreArchivo)
"""

inicio()

imagen.close()








