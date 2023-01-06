import os
from datetime import datetime
from struct import *

Imagen = open("fiunamfs.img", "r+b")
#Se hace el inicio del sistema leyendo los elementos almacenados en nuestro superbloque 0-57    
Read = Imagen.read(57)
#Se reinicia el "apuntador" de nuestro disco
Imagen.seek(0)
#Se muestran los datos iniciales del sistema (Datos del superbloque)
print("          (Micro)Sistema de archivos:",Imagen.read(8).decode("latin_1"))
print("\nVersión: ", Imagen.read(10).decode("latin_1"), "\n")
print("Etiqueta volumen:", Imagen.read(20).decode("latin_1"), "\n")
#En el caso de los enteros al estar en little endian se obtienen los valores por medio del unpack 
#regresando los valores en una tupla, por lo cual solo se almacena el elemento 0 de cada tupla
Size = unpack("i", Read[40:44])[0]
print("Tamaño cluster:", Size, "bytes\n")
ClusDirect = unpack("i", Read[45:49])[0]
print("Numero de clusters (directorio):", ClusDirect, "\n")
ClusUnidad = unpack("i", Read[50:54])[0]
print("Número de clusters (unidad):", ClusUnidad, "\n")



def ImprimirMenu(): #Función que imprime el menu
	Salir = False
	while not Salir:
		#os.system("clear")
		print(" 1- Visualizar todos los archivos\n","2- Exportar un archivo\n", "3- Eliminar un archivo\n", "4- Importar un archivo\n", "5- Salir\n")
		Opc = int(input("Escriba una opción: "))
		if Opc == 1:
			ImprArchivos()
		elif Opc == 2:
			ExportarArchivo()
		elif Opc == 3:
			EliminarArchivos()
		elif Opc == 4:
			ImportarArchivo()
		elif Opc == 5:
			Salir = True
		else: 
			print("Escoja una opción valida\n")

def ImprArchivos(): 
	#Se llama la función CargaArchivos la cual nos regresara en una lista con los datos de todos los archivos almacenados en el disco
	#Y posteriormente por medio de un ciclo imprimir todos
    
    Archivos = CargarArchivos()
    print("Listado de archivos:\n", "/    Nombre    / Peso /      Fecha y Hora de modificación      /")
    for elemento in Archivos:
        print("\n",elemento[0]," ", elemento[1]," ", elemento[3])
    print("\n")
def ExportarArchivo(): 
	#Se le pedira al usuario el nombre del archivo a exportar y este se mandara a una función donde se checaran todos
	#los elementos guardados viendo si alguno coinvvide con el nombre dado, en caso de encontrar una coincidencia se
	#obtendran los datos del archivo
    NombreArchivo = input("Ingresa el nombre del archivo a exportar(Con formato): ")
    ArchivoExport = BuscarArchivo(NombreArchivo)
	#En caso de que lo devuelto no sea "none" se entrara a la condicional 
    if ArchivoExport:
		#Se crea un archivo con el mismo nombre del archivo a exportar y se posicióna el apuntador del disco en la dirección donde se
		#encuentra (clusterinicial * tamañodecadacluster)
        ArchivoNuevo = open(NombreArchivo,"wb")
        Imagen.seek(ArchivoExport[2]*Size)
		#Se guarda en el archivo nuevo los datos almacenados desde la posición del apuntador en el rango de la memoria que ocupa
        ArchivoNuevo.write(Imagen.read(ArchivoExport[1]))
        ArchivoNuevo.close()
        print("Copia realizada\n")
        
def EliminarArchivos():
	#Al igual que en la función anterior se pide el archivo al usuario y se verifica que ese archivo se encuentre en el disco
    NombreArchivo = input("Ingresa el nombre del archivo a borrar(Con formato): ")
    ArchivoExport = BuscarArchivo(NombreArchivo)
    dire=Size #Posición inicial al terminar el superbloque donde inicia el registro de archivos
    nEspacio = 64 #nEspacio = 64 ya que es el espacio que ocupa el registro de cada archivo
    #Si ArchivoExport no es none se entra a la condicional
    if ArchivoExport:
		#Ciclo que recorrera el disco hasta encontrar un registro que coincida con el nombre obtenido
        for i in range(nEspacio):
			#Se coloca el apuntador en la ultima posición leida y se leen los datos a partir de ahí hasta 64 para
			#obtener todos los datos de un registro
            Imagen.seek(dire)
            Readt = Imagen.read(64)
			#En caso de que lo leido de nuestro disco coincida con el nombre se entrara al ciclo donde se cambiara el nombre del registro
			#a "--------------" lo cual quitara el acceso a los datos del archivo
            if Readt[1:15].decode("latin_1").lstrip(" ") == NombreArchivo:
                Imagen.seek(dire+1)
                Imagen.write("--------------".encode("latin_1"))
                print("Archivo eliminado\n")
                return
            dire = dire + 64


def ImportarArchivo():
	#Se pide el nombre de un archivo y se verifica su existencia
    NombreArchivo = input("Ingrese el nombre del archivo a copiar en FiUNAM(Con formato): ")
    ArchivoImport = BuscarArchivo(NombreArchivo)
    ClusterFinal = 0 #Se inicializa una variable para saber el cluster final de los archivos
    dire = Size
	#En caso de que el archivo no exista (ArchivoImport=None) se entra al ciclo
    if not ArchivoImport:
		#Se abre el archivo que se quiere importar y se calcula el tamaño que ocupa
        print("Se puede importar\n")
        ArchivoAImportar =  open(NombreArchivo, 'rb')  
        TamañoImportar = os.stat(NombreArchivo).st_size
		#Se obtienen los registros almacenados en el archivo y se ordenan de menor a mayor cluster
        Archivos = CargarArchivos()
        ArchivosOrdenados = sorted(Archivos, key=OrdenarArchivos)
		#Ciclo para buscar si hay espació disponible de almacenamiento entre archivos ya creados
        for x in range(len(ArchivosOrdenados)-1):
			#Se calcula cual seria el cluster final del archivo x 
            ClusterFinalA = (ArchivosOrdenados[x][1])/Size + ArchivosOrdenados[x][2] 
            #Se obtiene el cluster inicial del archivo siguiente al x
            ClusterInicialB = (ArchivosOrdenados[x + 1][2])
            #Si el tamaño de clusters que ocupa el archivo es menor a los clusters entre el cluster final del archivo x y el inicial de x+1
			#se entra a la condiconal donde se guardara el cluster donde ahora debera ser guardado el contenido del archivo a importar
            if (TamañoImportar/Size) < (ClusterInicialB-ClusterFinalA):
                ClusterFinal = int(ClusterFinalA)
                break
			#En caso contrario el cluster inicial de guardado sera el cluster final + 1 del ultimo archivo
            else:
                ClusterFinal = int((ArchivosOrdenados[x + 1][1])/Size + ArchivosOrdenados[x + 1][2]) 
        
        #Ciclo para actualizar el registro de los archivos y guardar su información
        for i in range(Size):
			#Se coloca el apuntador en el inicio de los registros de archivos y se busca donde hay un lugar libre ("---------------")
            Imagen.seek(dire)
            tRead = Imagen.read(64)
            if tRead[0:15].decode("latin_1") == "---------------":
				#Se avanza en uno el apuntador para no modificar el guion del tipo de archivo y despues se almacena la info del documento guardado
                Imagen.seek(dire+1)
                Imagen.write(NombreArchivo.rjust(14).encode("latin_1")+'\x00'.encode("latin_1")+pack("<i", TamañoImportar)+pack("<i", ClusterFinal + 1)+datetime.now().strftime('%Y%m%d%H%M%S').encode("latin_1")+datetime.now().strftime('%Y%m%d%H%M%S').encode("latin_1"))
                print("Archivo importado\n")
                return
            dire = dire + 64
        
        #Se posiciona el apuntador del disco en el cluster inicial encontrado en el ciclo anterior y se guarda el contenido del archivo en la memoria
        Imagen.seek((ClusterFinal + 1)*Size)
        ReadImportar = ArchivoAImportar.read()
        Imagen.write(ReadImportar)
        ArchivoAImportar.close()
        
    else:
        print("Un archivo con ese nombre ya existe en el disco")
        

#Función para guardar la información de los archivos almacenados en el sistema
def CargarArchivos(): 
    Archivos = []
    dire = Size
    nEspacio = 64
    Fecha = None
    #Ciclo para recorrer todos los registros guardados en el disco
    for i in range (nEspacio):
        Imagen.seek(dire)
        dire = dire + 64
        ReadImg = Imagen.read(64)
		#Si en el registro que se esta verificando hay un nombre en vez de "--------------" entonces se guardara 
		#el registro con toda su informació en una lista que se usara durante algunas operaciones 
        if ReadImg[1:15].decode("latin_1") != "--------------":
            list0 = []#lista temporal
            list0.append(ReadImg[1:15].decode("latin_1"))#Nombre
            list0.append(unpack("i", ReadImg[16:20])[0])#Peso
            list0.append(unpack("i", ReadImg[20:24])[0])#Cluster Inicial
            list0.append(datetime.strptime(ReadImg[38:52].decode("latin_1"),'%Y%m%d%H%M%S'))#Fecha y hora de modificación
            Archivos.append(list0)
    return Archivos
	
#Función para buscar si un elemento se encuentra en la memoria   
def BuscarArchivo(NombreArchivo):
	#Se cargan los archivos existentes
    Archivos = CargarArchivos()
	#Se recorren todos los archivos y se comparan con el Nombre que se manda a la función
    for nFile in Archivos:
		#En caso de encontrarse alguna coincidencia se regresa el registro con la información de ese archivo, en caso contrario se indicara que no se encontro
        if NombreArchivo == nFile[0].lstrip(" "): #lstrip es necesario para quitar los espacios en blanco a la izquierda
            return nFile
    print("Archivo no encontrado\n")
    return None
#Funcion que indicara el indice por el cual se deben ordenar los archivos	
def OrdenarArchivos(Archivo):
    return Archivo[2]
#Se llama la función que mostrara nuestro menu
ImprimirMenu()
Imagen.close()