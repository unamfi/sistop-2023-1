import os
import time
from struct import pack, unpack
import struct

def Buscar(archivo_base, sistemaArchivos, cluster): #funcion que recorre el directorio hasta encontrar un archivo. 
	sistemaArchivos.seek(cluster)
	for i in range(1, cluster * 4, 64):
		sistemaArchivos.seek(cluster+i)
		archivo = sistemaArchivos.read(15).decode("ascii")[:-1]
		print(archivo.strip())
		if str(archivo.strip()) == str(archivo_base.strip()):
			tamano_archivo = int(struct.unpack('<' + 'I'*1, sistemaArchivos.read(4))[0])
			cluster_inicial = int(struct.unpack('<' + 'I'*1, sistemaArchivos.read(4))[0])

			return (tamano_archivo, cluster_inicial)
		
	return (0,0)

def Listado(sistemaArchivos, cluster): #al igual que en encontrar archivo se recorre el directorio pero se imprimen los archivos diferentes de ---------
	sistemaArchivos.seek(cluster)

	for i in range(1, cluster * 4, 64):
		sistemaArchivos.seek(cluster+i)
		archivo = sistemaArchivos.read(15).decode("ascii")
		if archivo[:14] != "--------------":
			#print(archivo)

			print("\nArchivo:", archivo.strip(), struct.unpack('<' + 'I'*1, sistemaArchivos.read(4))[0], 'Cluster inicial', struct.unpack('<' + 'I'*1, sistemaArchivos.read(4))[0])


def Copiar_a_sistema(sistemaArchivos, cluster): #funcion que copia un archivo de fiunamfs a la computadora. 
	archivo_copia = input("Ingrese nombre del archivo: ")
	datos = Buscar(archivo_copia, sistemaArchivos, cluster)
	tamano_archivo = datos[0]
	cluster_inicial = datos[1]
	if tamano_archivo == 0 and cluster_inicial == 0:
		print("\nEl archivo no se encontro")

	else:

		print("\nArchivo encontrado:", archivo_copia)
		print("Espacio que ocupa:", tamano_archivo," Cluster inicial:", cluster_inicial)

		nuevo_archivo = open(archivo_copia,"wb")

		sistemaArchivos.seek(cluster * cluster_inicial)
		nuevo_archivo.write(sistemaArchivos.read(tamano_archivo))

		nuevo_archivo.close()

		print("\nArchivo copiado")

def Siguiente_Cluster(cluster_inicial, tamano_archivo, cluster):
	sobrante = tamano_archivo%cluster
	valor_a_aumentar = 1024 - sobrante

	return (cluster_inicial) * 1024 + tamano_archivo + valor_a_aumentar


def Espacio_en_directorio(sistemaArchivos, cluster):
	sistemaArchivos.seek(cluster)

	for i in range(0, cluster * 4, 64):
		sistemaArchivos.seek(cluster+i)
		archivo = sistemaArchivos.read(15).decode("ascii")
		if archivo[:14] == "--------------":
			return cluster + i

	return -1


def Cluster_disponible(tamano_de_archivo_copia, sistemaArchivos, cluster, tamano_sistemaArchivos):
	sistemaArchivos.seek(cluster)
	datoss = []
	for i in range(1, cluster * 4, 64):
		sistemaArchivos.seek(cluster+i)

		archivo = sistemaArchivos.read(15).decode("ascii").strip()[:-1]
		if archivo[:14] != "--------------":
			tamano_archivo = int(struct.unpack('<' + 'I'*1, sistemaArchivos.read(4))[0])
			cluster_inicial = int(struct.unpack('<' + 'I'*1, sistemaArchivos.read(4))[0])

			#se agrega a una lista donde se contienen los datos esenciales de los archivos
			datoss.append((cluster_inicial,tamano_archivo))

	
	#se ordenan los datos  de los archivos con respecto a su cluster inicial
	datoss = sorted(datoss, key=lambda x: x[0])

	for i in range(0,len(datoss)):

		dir_cluster_Siguiente = Siguiente_Cluster(datoss[i][0], datoss[i][1], cluster)

		#comparacion si son los ultimos datos de los archivos
		if i == len(datoss)-1:
			espacio_libre = tamano_sistemaArchivos - dir_cluster_Siguiente
		#en caso contrario la comparacion es con el archivo siguiente
		else:
			dir_cluster_archivo_siguiente = datoss[i+1][0] * 1024
			espacio_libre = dir_cluster_archivo_siguiente - dir_cluster_Siguiente

		if espacio_libre >= tamano_de_archivo_copia:
			return dir_cluster_Siguiente
	return -1
			
def Copiar_a_fiunamfs(sistemaArchivos, tamano_sistemaArchivos, cluster):
	archivo_copia = input("\nIngrese nombre del archivo: ")

	if len(archivo_copia) > 14:
		print("\nEl nombre del archivo es demasiado largo.")
		return

	if os.path.isfile(archivo_copia) == False:
		print("\nEl archivo no existe")
		return
	#se obtienen los datos esenciales del archivo y se ponen en una tupla
	datos = Buscar(archivo_copia, sistemaArchivos, cluster)
	#print(datos)
	#se obtienen los datos de la tupla
	tamano_archivo = datos[0]
	cluster_inicial = datos[1]
	print(datos)

	if tamano_archivo == 0 and cluster_inicial == 0:
		
		tamano_archivo_copia = os.stat(archivo_copia).st_size

		print("\nEspacio del archivo", tamano_archivo_copia)

		direccion = Espacio_en_directorio(sistemaArchivos, cluster)

		if direccion == -1:
			print("\nNo hay espacio en el directorio")
			return

		dir_cluster_disponible = Cluster_disponible(tamano_archivo_copia, sistemaArchivos, cluster, tamano_sistemaArchivos)

		if dir_cluster_disponible == -1:
			print("\nNo hay espacio en el sistema de archivos")
			return

		sistemaArchivos.seek(direccion)
		sistemaArchivos.write("                ".encode("ascii"))
		sistemaArchivos.seek(direccion)
		sistemaArchivos.write("-".encode("ascii"))
		
		sistemaArchivos.seek(direccion+1)
		sistemaArchivos.write("                ".encode("ascii"))
		sistemaArchivos.seek(direccion+1)
		sistemaArchivos.write(archivo_copia.encode("ascii"))

		#A partir de la direccion base vamos a ir aumentando segun los parametros establecidos en github.
		sistemaArchivos.seek(direccion+16)
		sistemaArchivos.write("000000000".encode("ascii"))
		str_tamano_archivo_copia = str(tamano_archivo_copia)
		numero_ceros = 9 - len(str_tamano_archivo_copia)
		sistemaArchivos.seek(direccion + 16 + numero_ceros)
		sistemaArchivos.write(struct.pack('<' + 'I'*1, int(str_tamano_archivo_copia)))

		sistemaArchivos.seek(direccion+20)
		sistemaArchivos.write("000000".encode("ascii"))
		cluster_disponible = int(dir_cluster_disponible / 1024)
		str_cluster_disponible= str(cluster_disponible)
		numero_ceros = 6 - len(str_cluster_disponible)
		sistemaArchivos.seek(direccion + 25 + numero_ceros)
		sistemaArchivos.write(struct.pack('<' + 'I'*1, int(str_tamano_archivo_copia)))

		sistemaArchivos.seek(direccion+24)
		str_fecha = str(time.localtime().tm_year) + str(time.localtime().tm_mon).zfill(2) + str(time.localtime().tm_mday).zfill(2) + str(time.localtime().tm_hour).zfill(2) + str(time.localtime().tm_min).zfill(2) + str(time.localtime().tm_sec).zfill(2)
		str_fecha = str_fecha + "."
		sistemaArchivos.write(str_fecha.encode("ascii"))

		sistemaArchivos.seek(direccion+38)
		sistemaArchivos.write(str_fecha.encode("ascii"))

		contenido_archivo = open(archivo_copia, "r+b")
		sistemaArchivos.seek(dir_cluster_disponible)
		for elemento in contenido_archivo:
			sistemaArchivos.write(elemento)

		print("\nArchivo Copiado")

	else:

		print("\nEl archivo ya existe")

def Eliminar(sistemaArchivos, cluster): #para eliminar de nuevo se recorre el directorio y cuando encuentra el archivo en cuestion se vacia el espacio
	archivo_a_eliminar = input("Ingrese nombre del archivo a eliminar: ")

	sistemaArchivos.seek(cluster)
	for i in range(1, cluster * 4, 64):
		sistemaArchivos.seek(cluster+i)
		archivo = sistemaArchivos.read(15).decode("ascii")[:-1]
		print(archivo)
		if archivo.strip() == archivo_a_eliminar.strip():
			sistemaArchivos.seek(cluster+i)
			sistemaArchivos.write("--------------".encode("ascii"))

			print("\nArchivo eliminado")
			return

	print("\nNo existe el archivo:")


sector = 256
cluster = sector * 4
seleccion = ""

sistemaArchivos = open("fiunamfs.img", "r+b")

print("\nSistema de archivos\n")

sistemaArchivos.seek(0)
print("Nombre:", sistemaArchivos.read(9).decode("ascii"))
sistemaArchivos.seek(10)
print("Versión de la implementación:", sistemaArchivos.read(4).decode("ascii"))
sistemaArchivos.seek(20)
print("Etiqueta del volumen:", sistemaArchivos.read(16).decode("ascii"))
sistemaArchivos.seek(40)
print("Tamaño del cluster en bytes:", struct.unpack('<' + 'I'*1, sistemaArchivos.read(4))[0])
#print("Tamaño del cluster en bytes:", sistemaArchivos.read(4))
sistemaArchivos.seek(45)
print("Número de clusters que mide el directorio:", struct.unpack('<' + 'I'*1, sistemaArchivos.read(4))[0])
sistemaArchivos.seek(51)
print("Número de clusters que mide la unidad completa:", struct.unpack('<' + 'I'*1, sistemaArchivos.read(4))[0])


while(seleccion != "5"):

	sistemaArchivos = open("fiunamfs.img", "r+b") #se actualizan los datos volviendo a abrir el archivo.

	tamano_sistemaArchivos = os.stat("fiunamfs.img").st_size
	#print(tamano_sistemaArchivos, "tamano sistema")

	print("\n Opciones \n")
	print("1. Listar contenido")
	print("2. Copiar archivo de FiUnamFS hacia tu sistema")
	print("3. Copiar archivo de tu sistema hacia FiUnamFS")
	print("4. Eliminar archivo de FiUnamFS")
	print("5. Salir")

	seleccion = input("\n\nIngresa una opción: ")

	if seleccion == "1":
		Listado(sistemaArchivos, cluster)

	elif seleccion == "2":
		Copiar_a_sistema(sistemaArchivos, cluster)

	elif seleccion == "3":
		Copiar_a_fiunamfs(sistemaArchivos, tamano_sistemaArchivos, cluster)

	elif seleccion == "4":
		Eliminar(sistemaArchivos, cluster)

	#se debe cerrar el archivo en cada ciclo para mostrar los cambios 
	sistemaArchivos.close()
