import threading
import time
import random
mutex = threading.Semaphore(1)
elementos = threading.Semaphore(0)
max_buffer = threading.Semaphore(10)
buffer = []

class Evento:
    def __init__(self):
        self.ident = random.random()
        print("Generando evento %1.3f. El buffer tiene %d." %
              (self.ident, len(buffer)))
        time.sleep(self.ident/2)
    def process(self):
        time.sleep(self.ident/2)
        print("Procesando evento %1.3f. El buffer tiene %d." %
              (self.ident, len(buffer)))


def productor():
    while True:
        event = Evento()
        max_buffer.acquire()
        mutex.acquire()
        buffer.append(event)
        mutex.release()
        elementos.release()

def consumidor():
    while True:
        elementos.acquire()
        mutex.acquire()
        event = buffer.pop()
        mutex.release()
        max_buffer.release()
        event.process()

threading.Thread(target=consumidor, args=[]).start()
for i in range(10):
    threading.Thread(target=productor, args=[]).start()
    
