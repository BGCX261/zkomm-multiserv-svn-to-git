#ZKOMM Multiserver
#Modelos de vistas

from PyQt4 import *

class modelo_lista_nodos:
	def __init__(self, padre, lista = []):
		self.m = QtGui.QStandardItemModel(0, 5, padre)
		encabezados = QtCore.QStringList()
		encabezados << "Nodo (ID)" << "Nombre" << "IP" << "Puerto" << "Capacidad" << "Carga" << "Sobrecarga" << "Penalizacion"
		self.m.setHorizontalHeaderLabels(encabezados)
		self.lista_nodos = lista
		self.actualizar_lista(self.lista_nodos)

	def actualizar_lista(self,lista):
		self.lista_nodos=lista
		row = 0
		self.m.setRowCount(len(self.lista_nodos))
		for i in self.lista_nodos:
			self.m.setItem(row, 0, QtGui.QStandardItem(str(i.ident)))
			self.m.setItem(row, 1, QtGui.QStandardItem(str(i.nombre)))
			self.m.setItem(row, 2, QtGui.QStandardItem(str(i.ip)))
			self.m.setItem(row, 3, QtGui.QStandardItem(str(i.puerto)))
			self.m.setItem(row, 4, QtGui.QStandardItem(str(i.capacidad)))
			self.m.setItem(row, 5, QtGui.QStandardItem(str(i.carga)))
			self.m.setItem(row, 6, QtGui.QStandardItem(str(i.sobrecarga)))
			self.m.setItem(row, 7, QtGui.QStandardItem(str(i.penalizacion)))
			row = row + 1


