#Lista de procesos
# Recordar que Tamashii esta modificando este fuente
from lista_procesos_proceso import proceso
from modelo_lista_procesos import modelo_lista_procesos
from PyQt4 import QtCore, QtGui

class lista_procesos:
	def __init__(self, lista = [], padre = QtCore.QObject()):
		self.lista = lista
		self.modelo = modelo_lista_procesos(padre, self.lista)

	def agregar_proceso(self, pros):
		self.lista.append(pros)
		return True

	def primer_proceso(self):
		pros = self.lista[0]
		return pros

	def mover_al_final(self, pros = None):
		if (pros == None):
			pros = self.primer_proceso()
		self.lista.remove(pros)
		self.lista.append(pros)

	def carga(self):
		carga = 0
		for i in self.lista:
			carga = carga + i.carga
		return carga

	def quitar_proceso(self, elem = None):
		try:
			if (elem == None):
				elem = self.lista[0]
			self.lista.remove(elem)
			sel.modelo.actualizar_lista(self.lista)
		except:
			return False
		return True

	def cambiar_ident_nodo(self, ident):
		for pros in self.lista:
			pros.id_nodo = ident
		self.modelo.actualizar_lista(self.lista)

	def model(self):
		return self.modelo
