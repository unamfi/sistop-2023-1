import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QDialog
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from threading import Semaphore, Thread
import time
import random

num_parrillas_delanteras = 0
num_parrillas_traseras = 0
cocinero = Semaphore(1)
sartenes = 0
olla_delante = 0
olla_atras = 0

class MiApp(QDialog): #clase que controla la ventana

	num_parrillas_delanteras = 0
	num_parrillas_traseras = 0
	num_sartenes = 5
	num_ollas = 10
	global sartenes

	def __init__(self): #constructor
		super(MiApp, self).__init__()
		loadUi('menu.ui', self)

	def setupUi(self, MainWindow): #funcion que conecta los botones con las funciones posteriormente establecidas
		MainWindow.setObjectName("Proyecto")
		self.buttonBox_5.clicked.connect(self.set_parrillas_delanteras)
		self.buttonBox_4.clicked.connect(self.set_parrillas_traseras)
		self.pushButton_4.clicked.connect(self.iniciar)
		self.pushButton_3.clicked.connect(self.set_sartenes_ollas)
		self.label_9.setText(str(sartenes))
		self.label_8.setText(str(olla_delante))
		self.label_10.setText(str(olla_atras))
		self.pushButton_5.clicked.connect(self.actualizar)

	def set_parrillas_delanteras(self): #funcion para establecer x parrillas delanteras
		global parrillas_delanteras
		if(self.buttonBox_5.clicked):
			self.num_parrillas_delanteras = int(self.lineEdit.text())
			num_parrillas_delanteras = self.num_parrillas_delanteras
			parrillas_delanteras = Semaphore(num_parrillas_delanteras) #multiplex de parrillas delanteras
			print(num_parrillas_delanteras,"parrillas delanteras fueron agregadas")

	def set_parrillas_traseras(self): #funcion para establecer y parrillas traseras
		global parrillas_traseras
		if(self.buttonBox_4.clicked):
			self.num_parrillas_traseras = int(self.lineEdit_2.text())
			num_parrillas_traseras = self.num_parrillas_traseras
			parrillas_traseras = Semaphore(num_parrillas_traseras) #Multiplex de parillas traseras
			print(num_parrillas_traseras,"parrillas traseras fueron agregadas")

	def set_sartenes_ollas(self): #funcion para establecer el numero de sartenes y ollas
		self.num_ollas = int(self.lineEdit_3.text())
		self.num_sartenes = int(self.lineEdit_3.text())
		print(self.num_sartenes,"sartenes fueron agregados y ", self.num_ollas, "ollas fueron agregadas")

	def iniciar(self): #funcion que inicia el proceso de los hilos
		if(self.pushButton_4.clicked):
			if(self.num_parrillas_delanteras > 0 and self.num_parrillas_traseras > 0):
				for i in range(self.num_sartenes):
					Thread(target=sarten, args=[i]).start()
					Thread(target=olla, args=[i]).start()


	def actualizar(self): #funcion que refresca el conteo de ollas y sartenes en la interfaz
		self.label_9.setText(str(sartenes))
		self.label_8.setText(str(olla_delante))
		self.label_10.setText(str(olla_atras))


def sarten(id_sarten): #funcion que define el comportamiento de los sartenes
	global platillos, sartenes
	#cocinero.acquire()
	#cocinero.release()
	parrillas_delanteras.acquire()
	print("Se cocina en sarten")
	time.sleep(5)
	sartenes += 1
	parrillas_delanteras.release()



def olla(id_olla): #funcion que define el comportamiento de las ollas, se usa un numero al azar para ver si se pone en parrilla delantera o trasera
	global platillos, olla_delante, olla_atras
	num = random.randint(1,10)
	#cocinero.acquire()
	if(num > 5):
		parrillas_delanteras.acquire()
		print("Se cocina en olla")
		time.sleep(3)
		olla_delante += 1
		parrillas_delanteras.release()
	else:
		parrillas_traseras.acquire()
		print("Se cocina en olla")
		time.sleep(3)
		olla_atras += 1
		parrillas_traseras.release()
	#cocinero.release()

if __name__ == "__main__":
     app = QApplication(sys.argv)
     MainWindow = QtWidgets.QMainWindow()
     mi_app = MiApp()
     mi_app.setupUi(MainWindow)
     mi_app.show()
     sys.exit(app.exec_())	


