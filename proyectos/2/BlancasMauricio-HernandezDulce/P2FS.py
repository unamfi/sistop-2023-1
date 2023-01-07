
import os
import math

#Abrimos el archivo, lo leemos y obtenemos su tamaño
fs = open('fiunamfs.img', 'r+b')
rd = fs.read(60).decode('utf-8')
tam = int(rd[40:46].rstrip('\x00'))

#Obtenemos el número de archivos por directorio
indicearch = int((int(rd[47:50].rstrip('\x00'))) * 8 * 256 / 64)


def fileunam(): 
	lista = []
	tamaux = tam 

	for i in range(indicearch):
		fs.seek(tamaux)
		rd2 = fs.read(64).decode('utf-8')
		if rd2[0:16] != '...............\x00':
			lista2 = []
			lista2.append(rd2[0:16].rstrip('\x00').lstrip(' '))
			lista2.append(int(rd2[16:25].rstrip('\x00')))
			lista2.append(int(rd2[25:31].rstrip('\x00')))
			lista2.append(rd2[31:35])
			lista2.append(rd2[35:37])
			lista2.append(rd2[37:39])
			lista2.append(rd2[39:41])
			lista2.append(rd2[41:43])
			lista2.append(math.ceil(lista2[1] / 2048 + lista2[2]))
			lista2.append(rd2[43:45])
			lista.append(lista2)
		tamaux += 64
	
	return lista


def ordenar():
	lista = fileunam()

	for z in lista:
		print('\nNombre:', z[0])
		print('\nTamaño:', z[1])
		print('\nCluster inicio:', z[2])
		print('\nAño creación:', z[3])
		print('\nMes creación:', z[4])
		print('\nDía creación:', z[5])
		print('\nHora creación:', z[6])
		print('\nMinuto creación:', z[7])
		print('\nCluster final:', z[8])
		print('\nSegundo creación:', z[9])
			


def fiPC():

	nombre1 = input('Dame el nombre del archivo: ')
	nombre2 = input('Dame el nuevo nombre')

	lista = fileunam()
	existe = -1
	#Recorremos la lista y si el primer elemento es igual al nombre del archivo entonces usamos nuestra variable de existencia
	for z in lista:
		if z[0] == nombre1:
			flen = z[1]
			existe = z[2]
			break

	if existe != -1:
		fs.seek(existe * tam)
		rd = fs.read(flen)
		newfile1 = open(nombre2, 'wb')
		newfile1.write(rd)
		newfile1.close()
		print('\nCopiado')


def borrar():
	nombre1 = input('Dame el nombre del archivo: ')
	lista = fileunam()

	existe = -1
	for z in lista:
		if z[0] == nombre1:
			flen = z[1]
			existe = z[2]
			break

	if existe != -1:
		fs.seek(existe * tam)
		for i in range(flen):
			fs.write(('\x00').encode('utf-8'))

		tamaux = tam
		for i in range(indicearch):
			fs.seek(tamaux)
			rd2 = fs.read(64).decode('utf-8')
			if rd2[0:16].lstrip(' ').rstrip('\x00') == nombre1:
				fs.seek(tamaux)
				fs.write(('...............\x0000000000\x0000000\x0000000000000000\x0000000000000000\x00\x00\x00\x00').encode('utf-8'))
				break
			tamaux += 64
		print('\nBorrado.')

op = 10
while op != 0:

	print('MENU')
	print('0. SALIR')
	print('1. Contenido')
	print('2. Copiar de FIUNAM a PC')
	print('3. Eliminar archivo de FIUNAM')
	print('4. Desfragmentar')

	op = int(input('Ingrese la opción: '))

	if op == 0:
		print('\nbai')
	elif op == 1:
		ordenar()
	elif op == 2:
		fiPC()
	elif op == 3:
		borrar()
	elif op == 4:
		print('No funciona la banda :c')
	else:
		print('\nVuelve a intentarlo')

fs.close()