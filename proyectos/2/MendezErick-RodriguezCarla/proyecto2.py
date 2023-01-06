import struct
import os
import time
import math
class sist_archivos:
    #Definición de variables globales del sistema de archivos
    nombreSist = " "
    version= " "
    etiqueta= " "
    tamanioCluster = " "
    ClustersxDirectorio = " "
    ClustersTotales = " "
    #Permite leer bytes en un rango de entre todos los bytes que componen la unidad
    def leerBytes(self,file, indiceInf, indiceSup):
        data = " "
        #Se abre el archivo en modo de lectura en bytes
        with open(file, "b+r") as fRange:
            fRange.seek(indiceInf)
            data = fRange.read (indiceSup-indiceInf)
        return data
    #Función que obtiene representación de Bytes en string, para esto se considera el ascii
    def pasaByteaString(self,byte):
        resultado = byte.decode("ascii")
        return resultado
    #Desempaqueta los bytes que representan un entero mediante el formado little endian, esta pensada para solo obtener un entero a la vez
    def convierteByteToInt(self, byte):
        numero = struct.unpack("<I", byte)
        resultado = numero[0]
        return resultado
    #Empaqueta un numero entero mediante formato little endian
    def convierteIntaByte(self, numero):
        byte = struct.pack("<I",numero)
        return byte
    #Obtiene datos acerca del sistema de archivos utilizado
    def obtieneSuperBloque(self, file):
        nombreSist = self.leerBytes(file, 0, 8)
        version = self.leerBytes(file, 10, 14)
        etiqueta = self.leerBytes(file, 20, 35)
        tamanioCluster = self.leerBytes(file, 40, 44)
        ClustersxDirectorio = self.leerBytes(file, 45, 49)
        ClustersTotales = self.leerBytes(file, 50, 54)
        return self.pasaByteaString(nombreSist),self.pasaByteaString(version),self.pasaByteaString(etiqueta),self.convierteByteToInt(tamanioCluster),self.convierteByteToInt(ClustersxDirectorio),self.convierteByteToInt(ClustersTotales)
   #Función que permite obtener los metadatos de los archivos, para esto se accede al directorio. Se ignoran los registros vacios
    def obtenerMetadatos(self,file):
        inicioDirectorio = 1024
        metadatos = [] #Se almacenan en una lista en donde cada indice representa los metadatos de un archivo
        while(inicioDirectorio <= 4096):
            if(self.pasaByteaString(self.leerBytes(file,inicioDirectorio+1, inicioDirectorio+15)) != "--------------"):
                metadatos.append([self.leerBytes(file,inicioDirectorio+1, inicioDirectorio+15)
                ,self.leerBytes(file,inicioDirectorio+16, inicioDirectorio+20)
                ,self.leerBytes(file,inicioDirectorio+20, inicioDirectorio+24)
                ,self.leerBytes(file,inicioDirectorio+24, inicioDirectorio+38)
                ,self.leerBytes(file,inicioDirectorio+38, inicioDirectorio+52)])
            inicioDirectorio += 64
        return metadatos
    #Da formato a las fechas obtenidas, da un string
    def dateFormat(self, bytesFecha):
        fecha = self.pasaByteaString(bytesFecha)
        fecha = fecha[0:4]+"/"+fecha[4:6]+"/"+fecha[6:8]+"-"+fecha[8:10]+":"+fecha[10:12]+":"+fecha[12:]
        return fecha
    #Muestra por consola los contenidos que se tienen en el sistema
    def muestraDocumentos(self,directorio):
        for archivo in directorio:
            print("---------------------------------------------")
            print("---------------------------------------------")
            print("Nombre de Archivo: "+self.pasaByteaString(archivo[0])+"\n")
            print("Tamanio: "+ str(self.convierteByteToInt(archivo[1]))+" bytes\n")
            print("Fecha de creación:"+ self.dateFormat(archivo[3])+"\n")
            print("Ultima fecha de modificación:"+ self.dateFormat(archivo[4])+"\n")
            print("Cluster inicial:"+ str(self.convierteByteToInt(archivo[2]))+"\n")
            print("---------------------------------------------")
            print("---------------------------------------------")
    #Elimina un archivo del sistema, no permite recovery
    def eliminar(self, nombre_Archivo, file):
        directorio = self.obtenerMetadatos(file)
        blanco = b'\x00'
        ##Se abre archivo en modo de escritura (sin sobreeescribir todo el contenido)
        sistema = open(file, "br+")
        for archivo in directorio: 
            ##Aqui empieza la limpieza en el espacio de datos
            if(self.pasaByteaString(archivo[0]).strip() == nombre_Archivo): #Strip elimina espacios al inicio y final del string
                sistema.seek(self.convierteByteToInt(archivo[2]) * 1024) ##Nos posicionamos en el cluster donde inicia el archivo
                for i in range(1,self.convierteByteToInt(archivo[1])):#Se genera cadena de bytes a sobreescribir sobre la información del archivo borrado
                    blanco = blanco + b'\x00'
                sistema.write(blanco)
                inicioDirectorio = 1024
                i=0
                #Aqui empieza la limpieza en el directorio
                while(inicioDirectorio <= 4096):
                    if(self.pasaByteaString(self.leerBytes(file,inicioDirectorio+1, inicioDirectorio+15)).strip() == nombre_Archivo.strip()):#Posicionamos en el cluster donde empiezan los metadatos
                        sistema.seek(inicioDirectorio+1)
                        sistema.write(b'--------------\x00\x00\x00\x00\x00\x00\x00\x00\x000000000000000000000000000000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                    inicioDirectorio += 64
        sistema.close()
    #Copia un archivo desde el sistema de archivos hacia nuestra computadora
    def copiardeSistToEquipo(self, nombre_Archivo, file):
        directorio = self.obtenerMetadatos(file)
        sistema = open(file, "br+")
        for archivo in directorio:
            if(self.pasaByteaString(archivo[0]).strip() == nombre_Archivo.strip()):
                dataFile = self.leerBytes(file,self.convierteByteToInt(archivo[2]) * 1024,(self.convierteByteToInt(archivo[2]) * 1024)+self.convierteByteToInt(archivo[1]))
                newFile = open(self.pasaByteaString(archivo[0]).strip(), "wb")
                newFile.write(dataFile)
                return True
        return False
    #Permite encontrar espacio disponible dentro del directorio, regresa el byte donde debe empezar la entrada en caso de encontrar espacio. Si no hay espacio disponible entonces regresa -1
    def encuentraEspacioDirectorio(self,file):
        inicioDirectorio = 1024
        while(inicioDirectorio <= 4096):
            if(self.pasaByteaString(self.leerBytes(file,inicioDirectorio+1, inicioDirectorio+15)) == "--------------"):
                return inicioDirectorio
            inicioDirectorio += 64
        return -1
    #Encuentra espacio disponible en el "espacio de datos", para esto se requiere como parametro el tamaño del archivo en bytes. Devuelve el inicio del cluster en el que empieza el espacio disponible
    def encuentraEspacioArchivo(self, tamanio, file):
        faltante = tamanio
        inicioEspacioDatos = 5120
        while(inicioEspacioDatos <= 737280):#El rango es: range(InicioEspacioDatos, FinEspacioDatos, EnCuantoAumentar(Lo que es el tamaño de un cluster))
            espacio = self.leerBytes(file,inicioEspacioDatos,inicioEspacioDatos+1)
            if(faltante <= 0):
                return inicioEspacioDatos
            elif(espacio == b'\x00'):
                faltante -= 1024
            else:
                if (faltante != tamanio):
                    faltante += 1024
            inicioEspacioDatos = inicioEspacioDatos + 1024
        return -1
    #Genera registro para ingresar archivo al directorio, regresa el conjunto de bytes a ingresar
    def generaRegistro(self,archivo, tamanio, inicioCluster):
        registro = b"-"
        nombre = bytes(archivo,'ascii')
        tamBytes = self.convierteIntaByte(tamanio)
        inicio = self.convierteIntaByte(inicioCluster)
        horaCreacion = os.path.getctime(archivo)
        auxiliarCreacion = time.ctime(horaCreacion)
        creacion_obj = time.strptime(auxiliarCreacion)
        stringCreacion = time.strftime("%Y%m%d%H%M%S", creacion_obj)
        byteCreacion = stringCreacion.encode('ascii')
        horaModificacion = os.path.getctime(archivo)
        auxiliarModificacion = time.ctime(horaModificacion)
        Modificacion_obj = time.strptime(auxiliarModificacion)
        stringModificacion = time.strftime("%Y%m%d%H%M%S", Modificacion_obj)
        byteModificacion = bytes(stringModificacion,'ascii')
        while(len(nombre)<14):
            nombre= b" "+nombre
        nombre = nombre + b" "
        return registro,nombre,tamBytes,inicio,byteCreacion,byteModificacion
    #Permite copiar un archivo desde la computadora al sistema
    def copiardeEquipoToSist(self, nombre_Archivo, file):
        archivoOrigen = open(nombre_Archivo, "br+")
        infoOrigen = archivoOrigen.read()
        inicioDirec = self.encuentraEspacioDirectorio(file) #Regresa el byte en el que se debe registrar el directorio
        inicioEspacio = self.encuentraEspacioArchivo(len(infoOrigen), file)
        if(inicioDirec != -1 and inicioEspacio != -1):
            sistemaArchivos = open(file,"rb+")
            registroDirectorio=self.generaRegistro(archivoOrigen.name, len(infoOrigen), (int)(inicioEspacio/1024))
            archivoOrigen.close()
            sistemaArchivos.seek(inicioDirec)
            sistemaArchivos.write(registroDirectorio[0])
            sistemaArchivos.write(registroDirectorio[1])
            sistemaArchivos.write(registroDirectorio[2])
            sistemaArchivos.write(registroDirectorio[3])
            sistemaArchivos.write(registroDirectorio[4])
            sistemaArchivos.write(registroDirectorio[5])
            sistemaArchivos.seek(inicioEspacio)
            sistemaArchivos.write(infoOrigen)
            return True
        archivoOrigen.close()
        return False
    #Realiza la desfragmentación del medio
    def desfragmentación(self,file):
        sistemaArchivos = open(file, "br+")
        directorio = self.obtenerMetadatos(file)
        PrimerClusterVacio = -1
        DatosArchivos = ''
        espacioVacio=b""
        noEspacios = 0
        inicioEspacioDatos = 5120
        while(inicioEspacioDatos < 737280):#El rango es: range(InicioEspacioDatos, FinEspacioDatos, EnCuantoAumentar(Lo que es el tamaño de un cluster))
            inicioDirectorio = 1024
            espacio = self.leerBytes(file,inicioEspacioDatos,inicioEspacioDatos+1)
            if(espacio == b'\x00'):
                Clustervacio = True
                for i in range(1,1024):
                    if(self.leerBytes(file,inicioEspacioDatos+i,inicioEspacioDatos+i+1) != b'\x00'):
                        Clustervacio = False
                if(Clustervacio):
                    if(PrimerClusterVacio <0):
                        PrimerClusterVacio =int(inicioEspacioDatos/1024)
                    noEspacios=noEspacios+1
                    inicioEspacioDatos += 1024
                else:
                    inicioEspacioDatos += 1024
            else:
                if(noEspacios > 0):
                    for archivo in directorio:
                        if(1024* self.convierteByteToInt(archivo[2]) == inicioEspacioDatos): #Se compara el primer cluster 
                            DatosArchivos = self.leerBytes(file, inicioEspacioDatos, (inicioEspacioDatos)+self.convierteByteToInt(archivo[1]))
                            sistemaArchivos.seek(int(PrimerClusterVacio*1024))
                            sistemaArchivos.write(DatosArchivos)
                            while(inicioDirectorio <= 4096):
                                if(self.pasaByteaString(self.leerBytes(file,inicioDirectorio+1, inicioDirectorio+15)) == self.pasaByteaString(archivo[0])):
                                    sistemaArchivos.seek(inicioDirectorio+20)#Nos posicionamos en el byte correspondiente al cluster inicial
                                    sistemaArchivos.write(self.convierteIntaByte(PrimerClusterVacio))
                                    while(noEspacios>0):
                                        espacioVacio=espacioVacio+b"\x00"
                                        noEspacios -= 1
                                    sistemaArchivos.seek(self.convierteByteToInt(archivo[1])+PrimerClusterVacio)
                                    sistemaArchivos.write(espacioVacio)
                                inicioDirectorio+=64
                            noEspacios=0
                            inicioEspacioDatos = (math.ceil(self.convierteByteToInt(archivo[1])/1024)*1024)+(PrimerClusterVacio*1024)
                            PrimerClusterVacio = -1
                            
                else:
                    inicioEspacioDatos += 1024
            #print("Inicio datos:"+str(inicioEspacioDatos))

                



        

instancia = sist_archivos()
pasa = -1
archivo = " "
while(pasa ==-1):
    print("Digita el nombre del archivo donde se encuentra el sistema de archivos (puede ser ruta)")
    archivo = input()
    try:
        superBloque = instancia.obtieneSuperBloque(archivo)
        if(superBloque[0]=='FiUnamFS' and superBloque[1]=='23.1'):
            pasa = 0
            print("\nEl sistema actual es:"+superBloque[0]+"/Versión: "
             +superBloque[1]+"\nEtiqueta:"+superBloque[2]+"/Tamaño de clusters en bytes:"+str(superBloque[3])
             +"\nClusters que componen el directorio:"+str(superBloque[4])+"/Clusters totales en el sistema:"+str(superBloque[5]))
        else:
            print("Ese no es un archivo correcto, se esperaba el sistema de archivos FiUnamFS en su versión 23.1")
    except FileNotFoundError:
        print("Ese archivo no existe")
op = -1


while op != 6:
    directorio = instancia.obtenerMetadatos(archivo)
    print("\nBienvenido al sistema de archivos")
    print("Digita una opción:")
    print("1.- Listar archivos del sistema")
    print("2.- Copiar un archivo desde fiunamfs hacia mi computadora")
    print("3.- Copiar un archivo desde mi computadora a fiunamfs")
    print("4.- Borrar un archivo de fiunamfs")
    print("5.- Desfragmentar el volumen")
    print("6.- Salir")
    try:
        op = int(input())
    except ValueError:
        print("\nError: Debes ingresar un numero entero")
    if(op == 1):
        instancia.muestraDocumentos(directorio)
    elif(op == 2):
        print("\nEscribe a continuación el nombre del archivo que deseas copiar")
        nombreArchivo = input()
        if(instancia.copiardeSistToEquipo(nombreArchivo, archivo)):
            print("Archivo copiado satisfactoriamente, se encuentra en el origen donde este programa esta")
        else:
            print("El archivo no existe")
    elif(op == 3):
        print("Ingresa el nombre del archivo que deseas copiar a fiunamfs, este debe estar en la misma raiz que este programa")
        nombreArchivo = input()
        nombreArchivo = nombreArchivo.strip()
        try:
            nombreArchivo.encode("Ascii")
            if(len(nombreArchivo) < 15):
                existe = False
                for archivoRegistrado in directorio:
                    if(nombreArchivo == instancia.pasaByteaString(archivoRegistrado[0]).strip()):
                        print("Error: Ese nombre ya esta registrado en fiunamfs")
                        existe = True
                if existe==False:
                    try:
                        if(instancia.copiardeEquipoToSist(nombreArchivo, archivo)):
                            print("Archivo copiado correctamente hacia fiunamfs")
                        else:
                            print("Error: no fue posible copiar el archivo por falta de almacenamiento contiguo")
                        
                    except FileNotFoundError:
                        print("Error: Archivo no encontrado")

            else:
                print("\n Error: El nombre de archivo debe ser máximo de 15 caracteres")
        except UnicodeEncodeError:
            print("Error: El nombre solo puede contener caracteres de ASCII de 7 bits")
    elif(op == 4):
        print("Ingresa el nombre del archivo que deseas eliminar de fiunamfs")
        nombreArchivo = input()
        nombreArchivo.strip()
        existe = False
        for archivoRegistrado in directorio:
            if(nombreArchivo == instancia.pasaByteaString(archivoRegistrado[0]).strip()):
                existe = True
        if(existe):
            instancia.eliminar(nombreArchivo,archivo)
            print("Archivo eliminado de fiunamfs")
        else:
            print("Ese archivo no se encuentra en el sistema")
    elif(op == 5):
        instancia.desfragmentación(archivo)