#Lista de procesadores
#Clase de administracion de las listas de procesadores

from lista_procesadores_procesador import procesador
from modelo_lista_procesadores import modelo_lista_procesadores
from PyQt4 import QtCore

class lista_procesadores:
	def __init__(self, l = [], padre = QtCore.QObject()):
		self.lista = l
		self.modelo = modelo_lista_procesadores(padre, self.lista)

	def agregar_procesador(self, p):
		for i in self.lista:
			if ((i.ident == p.ident) and (i.id_nodo == p.id_nodo)):
				return False
		self.lista.append(p)
		self.modelo.actualizar_lista(self.lista)
		return True

	def cant(self):
		return len(self.lista)

	def capacidad(self):
		capa = 0
		for i in self.lista:
		    capa = capa + i.velocidad
		return capa

	def carga(self):
		carga = 0
		for pro in self.lista:
		    carga = carga + pro.carga
		return carga

	def cambiar_ident_nodo(self, ident):
		for proc in self.lista:
			proc.id_nodo = ident
		self.modelo.actualizar_lista(self.lista)

	def model(self):
		return (self.modelo.m)

