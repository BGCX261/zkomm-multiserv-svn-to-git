#lista_procesadores.procesador
#clase con la que trabaja cada nodo. Se utiliza para identificar
#cada uno de los procesadores existentes
#NOTA: En el modelo no se tienen en cuenta los factores de
#carga, proceso o estado. Estos datos son locales al nodo

import thread
import time
import random

class procesador:
	PROC_WORKING = True
	PROC_IDLE = False

	def __init__(self, id_nodo, ident, velocidad, verbose=0):
		self.id_nodo = id_nodo
		self.ident = ident
		self.velocidad = velocidad
		self.carga = 0
		self.proceso = 0
		self.estado = self.PROC_IDLE
		self.verbose = verbose
		if (self.verbose>0):
			print "Velocidad del procesador:", self.velocidad

	def hilo_proceso(self):
		self.carga = self.proceso.carga
		while (self.carga > 1):
			if (self.verbose>0):
				print "carga actual: ", self.carga
			time.sleep(1.0/self.velocidad)
			self.carga = self.carga - 1
		time.sleep(self.carga/self.velocidad)
		if (self.verbose>0):
			print "carga actual: ", self.carga
		self.carga = 0
		self.proceso.resultado = random.randint(0,10)
		self.estado = self.PROC_IDLE

	def procesar(self, proceso):
		if (not self.estado):
			self.estado = self.PROC_WORKING
			self.proceso = proceso
			thread.start_new_thread(self.hilo_proceso, ())

#Pruebas
#from lista_procesos_proceso import *
#import sys
#lista = [proceso(1,1,"palabras",random.randint(10,25)),proceso(1,2,"palabras miles",random.randint(10,25))]
#mi_procesador=procesador(1,3,random.randint(1,15),1)
#for i in lista:
	#while (mi_procesador.estado):
		#pass
	#mi_procesador.procesar(i)
#cad=raw_input("Para salir presione ENTER")
#sys.exit(0)