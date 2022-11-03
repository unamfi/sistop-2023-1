import random
import string
import re

def Liberar(memoria, letra):
	for i in range (len(memoria)):
		if memoria[i] == letra:
			memoria[i] = "-"
	return memoria

def Compactacion(memoria):
	memoria = sorted([i for i in memoria if not str(i).isdigit()]) + sorted([i for i in memoria if str(i).isdigit()])

def Contar_memoria(ubicacion,memoria, cantidad, referencia):
	espacio = 0
	maximo_espacio = 0 
	localidad = 0
	bandera = ubicacion
	global mem_ub

	for j in range (ubicacion, len(memoria)):
		if memoria[j] == "-":
			espacio += 1
			bandera += 1
		else:
			bandera += 1
			break
	if espacio > maximo_espacio:
		maximo_espacio = espacio
		print("maximo_espacio: " + str(maximo_espacio))
		
	if maximo_espacio < cantidad:
		localidad = bandera
		if localidad == len(memoria):
			mem_ub = -1
			return
		for i in range (bandera, len(memoria)):
			localidad = i
			if memoria[i] == "-":
				print("ubicacion" + str(i))
				break
		Contar_memoria(localidad, memoria, cantidad, maximo_espacio)

	else:
		print(ubicacion)
		mem_ub = ubicacion
		return


def Agregar_proceso(ubicacion,memoria,cantidad, letra):
	for i in range (ubicacion, ubicacion+cantidad):
		if memoria[i] == "-": 
			memoria[i] = letra

def Asignacion(memoria, letra, cantidad):
	espacio = 1
	compactacion = 1
	for i in range (len(memoria)):
		if memoria[i] == "-":
			espacio = 1
			Contar_memoria(i, memoria, cantidad, 0)
			compactacion = mem_ub
			print("el valor de compactacion es: " + str(compactacion))
			if compactacion == -1:
				print("Compactacion requerida")
				memoria.sort()
				print(memoria)
				Asignacion(memoria, letra, cantidad)
				break
			else:
				Agregar_proceso(compactacion, memoria, cantidad, letra)
				break


memoria = [0]*30
letra_espacio = ""

for i in range (len(memoria)):
	memoria[i] = random.choice("A"+"B"+"C"+"D"+"E"+"F"+"G")

memoria.sort()
letra_espacio = random.choice("A"+"B"+"C"+"D"+"E"+"F"+"G")

for i in range (len(memoria)):
	if letra_espacio == memoria[i]:
		memoria[i] = "-"


print("Memoria actual")
print(memoria)

opcion = 0

while(opcion != 3):

	print("Asignar(0) o Liberar (1) o Salir (3)\n")
	entrada  = re.search(r"\d+", input())
	opcion = int(entrada.group(0)) if entrada is not None else None

	if opcion == 0:
		print("Escribe letra del proceso")
		entrada  = input()
		letra = str(entrada)
		print("Escribe cantidad de memoria")
		entrada  = input()
		cantidad = int(entrada)
		Asignacion(memoria, letra, cantidad)
		print(memoria)

	elif opcion == 1:
		print("Escribe letra del proceso")
		entrada  = input()
		letra = str(entrada)
		memoria = Liberar(memoria, letra)
		print(memoria)

	elif opcion == 3:
		continue 

	else:
		print("opcion no valida")



















