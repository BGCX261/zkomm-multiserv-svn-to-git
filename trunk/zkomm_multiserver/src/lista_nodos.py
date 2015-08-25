#Lista encargada de la informacion de los nodos conocidos


from lista_nodos_nodo import nodo
from modelo_lista_nodos import modelo_lista_nodos
from PyQt4 import QtCore

class lista_nodos:
	def __init__(self, l = [], padre = QtCore.QObject()):
		self.lista = l
		self.modelo = modelo_lista_nodos(padre, self.lista)

	def agregar_nodo(self, n):
		if (n.ident == None):
			n.ident = len(self.lista)
		self.lista.append(n)
		self.modelo.actualizar_lista(self.lista)
		return True

	def actualizar_datos_nodo(self, nad):
		ind = 0
		print "Actualizar nodo con id",nad.ident,"puerto",nad.puerto
		for nod in self.lista:
	 		if nod.ip == nad.ip:
	 			if nod.puerto == nad.puerto:
	 				self.lista[ind] = nad
				 	self.modelo.actualizar_lista(self.lista)
	 				return True
	 		ind = ind + 1
	 	self.agregar_nodo(nad)

	def ya_existe(self, nad):
		existe = False
		for ned in self.lista:
			if ((ned.ip == nad.ip) and (ned.puerto == nad.puerto)):
				existe = True
		return existe

	def cant(self):
		return len(self.lista)

	def model(self):
		return (self.modelo.m)
