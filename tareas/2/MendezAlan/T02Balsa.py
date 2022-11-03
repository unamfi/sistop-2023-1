import time
import threading
import random

numHackers = 4
numSerfs = 4
bHackers = threading.Barrier(2)
bSerfs = threading.Barrier(2)
bBarca = threading.Barrier(4)
bStart = threading.Barrier(4)
balsa = threading.Semaphore(4)

def serfs (id:int):
    while True:
        print('Serf %d quiere subirse a un balsa \n' % id)
        time.sleep(4 * random.random())
        print('Serf %d quiere subirse a un balsa \n' % id)
        bSerfs.wait()
        print('Serf %d esperando subirse al balsa \n' % id)
        bBarca.wait()
        balsa.acquire()
        print('Serf %d HA SUBIDO \n' % id)
        print('Serf %d terminó su cruce \n' % id)
        balsa.release()
        
def hackers (id:int):
    while True:
        time.sleep(4 * random.random())
        print('\t\t\tHacker %d quiere subirse a la balsa \n' % id)
        bHackers.wait()
        print('\t\t\tHacker %d esperando subirse la balsa \n' % id)
        bBarca.wait()
        balsa.acquire()
        print('\t\t\tHacker %d HA SUBIDO \n' % id)
        print('\t\t\tHacker %d terminó su cruce \n' % id)
        balsa.release()


for i in range (numHackers):
    #print(numHackers)
    threading.Thread(target=hackers, args=[i]).start()
for i in range (numSerfs):
    threading.Thread(target=serfs, args=[i]).start()