# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RusQWwNotxTQ1_zUxPB--b5rPAkTtJk7
"""

from google.colab import drive
drive.mount('/content/drive')
file = open("/content/drive/MyDrive/proyecto/fiunamfs.img","r+b")

#Bibliotecas
import os
import struct

#Variables globales
sectores = 256
cluster = sectores * 4

#Funciones
def convertir(datos):
  valor = str(struct.unpack('<I',datos)[0])
  return valor

def printList():
  global cluster
  print("")
  print("")
  print("Tipo-----Nombre-----Tamaño----Cluster inicial----Fecha y hora de creación---Ultima modificacion")

  #Recorre todo el directorio para obtener informacion de los archivos
  for archivoInfo in range(0, (cluster*4), 64):
  
    #cluster inicia en 1026 y no en 1024 , por eso sumo "cluster+2+archivoInfo"
    FSFI.seek(cluster+2+archivoInfo)
    if FSFI.read(14).decode() != '--------------':

      FSFI.seek(cluster+2+archivoInfo)
      print("  "+FSFI.read(1).decode()+" ", end = "")                                                   #Imprime Tipo
      print(""+FSFI.read(14).decode()+"", end = "")                                                     #Imprime Nombre
      print(" "+convertir(FSFI.read(4))+" ", end = "")                                                  #Imprime Tamaño
      print("       "+convertir(FSFI.read(4))+"       ", end = "")                                      #Imprime cluster inicial (error no imprime :C)
      FSFI.seek(cluster+2+24)                                                                           #Evita que los datos de fecha y hora salgan mal
      print("      "+FSFI.read(4).decode()+"-"+FSFI.read(2).decode()+"-"+FSFI.read(2).decode(), end = "")     #Imprime Fecha de creación
      print(" "+FSFI.read(2).decode()+":"+FSFI.read(2).decode()+":"+FSFI.read(2).decode(), end="")      #Imprime Hora de creación
      print("      "+FSFI.read(4).decode()+"-"+FSFI.read(2).decode()+"-"+FSFI.read(2).decode(), end = "") #Imprime Fecha de mod
      print(" "+FSFI.read(2).decode()+":"+FSFI.read(2).decode()+":"+FSFI.read(2).decode())              #Imprime Hora de mod

#Programa principal:
print("----Sistema de archivos FI----")
FSFI = open("/content/drive/MyDrive/proyecto/fiunamfs.img", "r+b")

#Imprime la informacion principal
FSFI.seek(0)
print("Nombre: "+FSFI.read(8).decode())

FSFI.seek(10)
print("Version: "+FSFI.read(4).decode())

#Previene que se abra otra version del sistema de archivos para evitar corrupción
FSFI.seek(10)
if FSFI.read(4).decode() != "23.1":
  print("La version del sistema de archivos no es '23.1', cargue la version actualizada :D")
  FSFI.close()

FSFI.seek(20)
print("Volumen: "+FSFI.read(15).decode())

FSFI.seek(40)
print("Tamano Cluster: "+str(struct.unpack('<I',FSFI.read(4))[0]))

FSFI.seek(45)
print("Tamaño de Cluster en directorio: "+str(struct.unpack('<I',FSFI.read(4))[0]))

FSFI.seek(50)
print("Tamaño Cluster de Unidad Completa: "+str(struct.unpack('<I',FSFI.read(4))[0]))

#Menu General
while True:
  print("")
  print("")
  print("")
  print("¿Que deseas realizar? :)")
  print("Opciones: ")
  print("Mostrar lista de archivos = ''lsar''")
  print("Copiar =                    ''cp-archivo-destino''")
  print("Borrar =                    ''del-archivo''")
  print("Salir =                     ''exit''")
  comando = input()
  comando = comando.split("-")
  
  if comando[0] == 'lsar':
    printList()
  elif comando[0] == 'cp' and len(comando) == 3:
    print("copiado")
  elif comando[0] == 'del' and len(comando) == 2:
    print("borrar")
  if comando[0] == 'exit':
    FSFI.close()
    print("Cerrando...")
    break