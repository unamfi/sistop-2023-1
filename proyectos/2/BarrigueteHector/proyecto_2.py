import os

global lista_archivos, lista_clusters
lista_archivos = []
lista_clusters = []

def mostrar_contenido():
    pass

def copiar_al_sistema():
    pass

def copiar_a_fiunamfs():
    pass

def eliminar_archivo():
    pass

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
        print("\nLa versión del sistema de archivos es compatible con la versión del programa\n")
    else:
        opcion = 6
        print("\n¡¡¡¡¡ La versión del sistema de archivos no es compatible con la versión del programa !!!!!\nNo es posible iniciar el sistema de archivos\n")

    file_version.close()

    while int(opcion) != 5:
        opcion = input("\n\n------------ MENU ------------\n1. Listar contenido\n2. Copiar archivo de FiUnamFS hacia este sistema\n3. Copiar archivo de este sistema hacia FiUnamFS\n4. Eliminar un archivo de FiUnamFS\n5. Desfragmentar\n6. Salir\nIngresa una opcion: ")

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