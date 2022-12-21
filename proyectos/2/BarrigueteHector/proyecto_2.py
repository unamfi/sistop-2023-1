import os

global lista_archivos, lista_clusters
lista_archivos = []
lista_clusters = []

def mostrar_contenido(file_system, cluster_size):
    print("\n------------ CONTENIDO ------------")
    print("    Nombre\tCreacion del archivo\tUltima modificacion")
    file_system.seek(cluster_size)
    
    for i in range(0, cluster_size * 4, 64):
        file_system.seek(cluster_size + i)
        file = file_system.read(16).decode("utf-8")
        
        j = 0

        if file[j] ==  '-':
            while(file[j] == " " or file[j] == "-"):
                if j == 15:
                    break
                else:
                    j += 1
            
            if j < 15:
                print("-", file[j:15], end = "\t")
                
                j = 0
                j = 15 + 9
                file_system.seek(cluster_size + i + j)
                j = 0

                #CREACION
                file = file_system.read(4).decode("utf-8") #Year
                print(file, end = "-")
                file = file_system.read(2).decode("utf-8") #Month
                print(file, end = "-")
                file = file_system.read(2).decode("utf-8") #Day
                print(file, end = " ")
                file = file_system.read(2).decode("utf-8") #Hour
                print(file, end = ":")
                file = file_system.read(2).decode("utf-8") #Minute
                print(file, end = ":")
                file = file_system.read(2).decode("utf-8") #Second
                print(file, end = "\t")

                #MODIFICACION
                file = file_system.read(4).decode("utf-8") #Year
                print(file, end = "-")
                file = file_system.read(2).decode("utf-8") #Month
                print(file, end = "-")
                file = file_system.read(2).decode("utf-8") #Day
                print(file, end = " ")
                file = file_system.read(2).decode("utf-8") #Hour
                print(file, end = ":")
                file = file_system.read(2).decode("utf-8") #Minute
                print(file, end = ":")
                file = file_system.read(2).decode("utf-8") #Second
                print(file, end = "\n")

def copiar_al_sistema():
    pass

def copiar_a_fiunamfs():
    pass

def eliminar_archivo(file_system, cluster_size):
    print("\n------------ ELIMINAR ARCHIVO DE fiunamfs ------------")
    
    file_delete = input("Ingresa el nombre del archivo a eliminar (incluya la extensión): ")

    if file_delete in lista_archivos:
        file_system.seek(cluster_size)

        for i in range(0, cluster_size * 4, 64):
            file_system.seek(cluster_size + i)
            file = file_system.read(16).decode("utf-8")
            
            j = 0

            if file[j] ==  '-':
                while(file[j] == " " or file[j] == "-"):
                    if j == 15:
                        break
                    else:
                        j += 1
            
            if j < 15:
                file = file[j:15]

                if file == file_delete:                    
                    #NOMBRE
                    file_system.seek(cluster_size + i)
                    file_system.write("---------------".encode("utf-8"))
                    #TAMAÑO
                    file_system.seek(cluster_size + i + 16)
                    file_system.write("0000".encode("utf-8"))
                    #CLUSTER INICIAL
                    file_system.seek(cluster_size + i + 19)
                    file_system.write("000".encode("utf-8"))
                    #FECHA DE CREACION Y MODIFICACION
                    file_system.seek(cluster_size + i + 24)
                    file_system.write("0000000000000000000000000000".encode("utf-8"))

                    lista_archivos.remove(file_delete)

                    print("\n¡¡¡¡¡ Archivo eliminado exitosamente !!!!!")
                    break
    else:
        print("\n!!!!! El archivo no existe en el sistema de archivos ¡¡¡¡¡")

def index_cluster(file_system, cluster_size):
    file_system.seek(cluster_size)
        
    for i in range(0, cluster_size * 4, 64):
        file_system.seek(cluster_size + i)
        lista_clusters.append(cluster_size + i)
    
def archivos_iniciales(file_system, cluster_size):
    lista_archivos.clear()
    
    file_system.seek(cluster_size)
    
    j = 0

    for i in range(0, cluster_size * 4, 64):
        file_system.seek(cluster_size + i)
        file = file_system.read(15).decode("utf-8")
        
        if file == "---------------":
            lista_archivos.append("---")
        else:
            while(file[j] == " " or file[j] == "-"):
                j += 1
            
            lista_archivos.append(file[j:15])
            j = 0

def main():
    sector_size = 256
    cluster_size = sector_size * 4
    
    opcion = 0
    file_system = open("fiunamfs.img", "r+b")

    print("\n********************* SISTEMA DE ARCHIVOS: FiUnamFs *********************")
    file_system.seek(0)    
    print("\n\nNombre del sistema de archivos:", file_system.read(8).decode("utf-8"))

    file_system.seek(10)
    version = file_system.read(4).decode("utf-8")
    print("Versión de la implementación:", version)
    
    file_system.seek(21)
    print("Etiqueta del volumen:", file_system.read(14).decode("utf-8"))
    
    # ERROR
    file_system.seek(40)
    print("Tamaño del cluster (en bytes):", file_system.read(3).decode("utf-8"))
    
    # ERROR
    file_system.seek(47)
    print("Número de clusters que mide el directorio:",  file_system.read(3).decode("utf-8"))
    
    # SUPER ERROR
    #file_system.seek(52)
    #print("Número de clusters que mide la unidad completa:", file_system.read(3).decode("utf-8"))

    #COMPROBACION DE LA VERSION 
    path_version = "version.img"
    file_version = open(path_version, "r+b")
    file_version.seek(0)
    f_version = file_version.read(4).decode("utf-8")
    
    if (f_version in version):
        archivos_iniciales(file_system, cluster_size)
        index_cluster(file_system, cluster_size)
    else:
        opcion = 5
        print("\n¡¡¡¡¡ La versión del sistema de archivos no es compatible con la versión del programa !!!!!\nNo es posible iniciar el sistema de archivos\n")

    file_version.close()

    while int(opcion) != 5:
        opcion = input("\n\n------------ MENU ------------\n1. Listar contenido\n2. Copiar archivo de FiUnamFS hacia este sistema\n3. Copiar archivo de este sistema hacia FiUnamFS\n4. Eliminar un archivo de FiUnamFS\n5. Salir\nIngresa una opcion: ")

        file_system = open("fiunamfs.img", "r+b")
        file_size = os.stat("fiunamfs.img").st_size
    
        if int(opcion) == 1:
            mostrar_contenido()
        elif int(opcion) == 2:
            copiar_al_sistema()
        elif int(opcion) == 3:
            copiar_a_fiunamfs()
        elif int(opcion) == 4:
            eliminar_archivo()
        else:
            print("\n************ CERRANDO SISTEMA DE ARCHIVOS ************\n")

        file_system.close()

main()