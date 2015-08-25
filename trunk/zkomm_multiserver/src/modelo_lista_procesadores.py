#ZKOMM Multiserver
#Modelos de vistas

from PyQt4 import QtCore,QtGui

class modelo_lista_procesadores:
	def __init__(self, padre, lista_procesadores = []):
		self.m = QtGui.QStandardItemModel(0, 5, padre)
		encabezados = QtCore.QStringList()
		encabezados << "Nodo (ID)" << "Procesador (ID)" << "Velocidad" << "Proceso" << "Estado"
		self.m.setHorizontalHeaderLabels(encabezados)
		self.lista_procesadores = lista_procesadores
		self.actualizar_lista(self.lista_procesadores)

	def actualizar_lista(self,lista_procesadores):
		self.lista_procesadores=lista_procesadores
		row = 0
		self.m.setRowCount(len(self.lista_procesadores))
		for i in self.lista_procesadores:
#			datos=[]
#			datos.append(QtGui.QStandardItem(str(i.id_nodo)))
#			datos.append(QtGui.QStandardItem(str(i.ident)))
#			datos.append(QtGui.QStandardItem(str(i.velocidad)))
#			datos.append(QtGui.QStandardItem(str(i.proceso)))
#			if (i.estado == False):
#				datos.append(QtGui.QStandardItem("Trabajando"))
#			else:
#				datos.append(QtGui.QStandardItem("Libre"))
#			self.m.insertRow(0, datos)

			self.m.setItem(row, 0, QtGui.QStandardItem(str(i.id_nodo)))
			self.m.setItem(row, 1, QtGui.QStandardItem(str(i.ident)))
			self.m.setItem(row, 2, QtGui.QStandardItem(str(i.velocidad)))
			self.m.setItem(row, 3, QtGui.QStandardItem(str(i.proceso)))
			if (i.estado == i.PROC_WORKING):
				self.m.setItem(row, 4, QtGui.QStandardItem("Trabajando"))
			else:
				self.m.setItem(row, 4, QtGui.QStandardItem("Libre"))
			row = row + 1

