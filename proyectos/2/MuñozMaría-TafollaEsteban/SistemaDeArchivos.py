#Bibliotecas
import struct
NOMBRE_IMAGEN = "fiunamfs.img"

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

def sacaDatosArchivo(posicion):
    inicial = 1024 + (posicion * 64)
    if(sacaDatosAscii(inicial+1,14) != "--------------"):
        tipo = sacaDatosAscii(inicial,1)
        nombre = sacaDatosAscii(inicial+1, 14)
        tamanio = datoUnpack(inicial+16, 4)
        clusterInicial = datoUnpack(inicial+20,4)
        fechaCreacion = sacaDatosAscii(inicial+24, 14)
        fechaModificacion = sacaDatosAscii(inicial+38, 14)
        print(tipo, nombre, tamanio, clusterInicial, fechaCreacion, fechaModificacion)

class archivo:
    def __init__(self, nombre, tamanio, clusterInicial, fechaCreacion, fechaModificacion):
        self.nombre = nombre
        self.tamanio = tamanio
        self.clusterInicial = clusterInicial
        self.fechaCreacion = fechaCreacion
        self.fechaModificacion = fechaModificacion

def inicio():
    numArchivos = int((tamanioCluster * clustersDirectorio)/tamanioDirectorio)
    for x in range(numArchivos):
        sacaDatosArchivo(x)
        

print("Saca datos:")
sacaDatosArchivo(0)

nombreSistema = sacaDatosAscii(0,8)
version = sacaDatosAscii(10,4)
etiqueta = sacaDatosAscii(20,5)
print(nombreSistema, version, etiqueta)

tamanioCluster= datoUnpack(40,4) #Da 1024
print(tamanioCluster)
clustersDirectorio = datoUnpack(45,4) #Da 4
print(clustersDirectorio)
clustersUnidad = datoUnpack(50,4) #Da 720
print(clustersUnidad)
tamanioDirectorio = 64

nombreArchivo = sacaDatosAscii(1025,14)
print(nombreArchivo)

inicio()

imagen.close()


