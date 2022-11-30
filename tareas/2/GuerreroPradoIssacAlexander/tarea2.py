from threading import Semaphore, Thread
import time
import random

num_gatos = 3
max_ratones = 20
platos = Semaphore(3)
entra_raton = Semaphore(1)
cuarto_con_ratones = Semaphore(1)
ratones = 0

def gato(id_gato):
	platos.acquire()
	print("gato", id_gato, ": BRRR BRRRR BRRR")
	platos.release()
	if(ratones >= 1):
		print("gato", id_gato, "se comio un raton")
	print("gato",id_gato, "se fue")

def raton(id_raton):
	global ratones
	platos.acquire()
	entra_raton.acquire()
	ratones += 1
	if ratones == 1:
		cuarto_con_ratones.acquire()
	entra_raton.release()

	print("raton", id_raton, ": NAM NAM NAM NAM")

	entra_raton.acquire()
	ratones = ratones - 1
	platos.release()
	if ratones == 0:
		cuarto_con_ratones.release()
	entra_raton.release()
	print("raton",id_raton, "se fue")

while(ratones < max_ratones):

	for i in range(num_gatos):
		Thread(target=gato, args=[i]).start()

	for j in range(max_ratones):
		Thread(target=raton, args=[j]).start()


