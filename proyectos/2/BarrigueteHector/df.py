global lista_clusters, lista_archivos
lista_archivos = []
lista_clusters = []

def desfragmentar(file_system, cluster_size):    
    new_pos = 0
    old_pos = 0
    lista_index = []
    bandera = True
    banderaDos = True

    #Recorremos la lista de archivos para obtener los indices de los archivos
    for archivo in lista_archivos: 
        if archivo != "---":
            lista_index.append(lista_archivos.index(archivo))

    while bandera == True:
        #Recorremos la lista de archivos para obtener el indice de de los espacios vacios
        new_pos = 0
        old_pos = 0
        
        for archivo in lista_archivos:
            if archivo == "---":
                new_pos = lista_archivos.index(archivo)

                #Recorremos la lista de indices para saber si se puede mover un archivo
                for i in lista_index:
                    #¿La nueva posición es menor a la actual del archivo?
                    if new_pos < i: 
                        old_pos = i
                        break
            
            if new_pos != 0 and old_pos != 0:
                break

        #Actualización del file system
        if new_pos < old_pos:
            lista_index = []
            
            for archivo in lista_archivos: 
                if archivo != "---":
                    lista_index.append(lista_archivos.index(archivo))

            pos_one = lista_clusters[new_pos]
            pos_two = lista_clusters[old_pos]
            
            file_system.seek(pos_two)
            file = file_system.read(64)

            clean_registre = open("registro_vacio.img", "rb+")
            clean = clean_registre.read(64)
            file_system.seek(pos_two)
            file_system.write(clean)

            file_system.seek(pos_one)
            file_system.write(file)

            archivos_iniciales(file_system, 1024)

            for archivo in lista_archivos: 
                if archivo != "---" and banderaDos == True:
                    pass
                elif archivo == "---" and banderaDos == True:
                    banderaDos = False
                    
                if banderaDos == False and archivo == "---":
                    bandera = False
                    pass
                elif banderaDos == False and archivo != "---":
                    bandera = True
                    break

            if bandera == True:
                banderaDos = True
                
        print("\n******** Desfragmentacion exitosa ********\n")

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

if __name__ == '__main__':
    print("\nDESFRAGMENTANDO...")
    file_system = open("fiunamfs.img", "r+b")

    sector_size = 256
    cluster_size = sector_size * 4

    index_cluster(file_system, cluster_size)
    archivos_iniciales(file_system, cluster_size)
    desfragmentar(file_system, cluster_size)

    file_system.close()