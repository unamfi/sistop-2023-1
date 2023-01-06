#!/usr/bin/python3
# Implementa un monitor: Una clase que controla mediante
# primitivas de sincronización el acceso concurrente a los
# datos compartidos
import threading

class suma_consistente:
    def __init__(self, i):
        self.mut_i = threading.Semaphore(1)
        self.i = i

    def suma(self,num):
        self.mut_i.acquire()
        self.i += num
        self.mut_i.release()

    def valor(self):
        self.mut_i.acquire()
        res = self.i
        self.mut_i.release()
        return res
