#ZKOMM Multiserver
#Modelo de vistas para los procesos

from PyQt4 import QtCore,QtGui

class modelo_lista_procesos:
	def __init__(self, padre, lista_procesos = []):
		self.m = QtGui.QStandardItemModel(0, 5, padre)
		encabezados = QtCore.QStringList()
		encabezados << "Nodo (ID)" << "Proceso (ID)" << "Carga" << "Código" << "Estado"
		self.m.setHorizontalHeaderLabels(encabezados)
		self.lista_procesos = lista_procesos
		self.actualizar_lista(self.lista_procesos)

	def actualizar_lista(self,lista_procesos):
		self.lista_procesos=lista_procesos
		row = 0
		self.m.setRowCount(len(self.lista_procesos))
		for i in self.lista_procesos:
			self.m.setItem(row, 0, QtGui.QStandardItem(str(i.id_nodo)))
			self.m.setItem(row, 1, QtGui.QStandardItem(str(i.ident)))
			self.m.setItem(row, 2, QtGui.QStandardItem(str(i.carga)))
			if (len(i.codigo) > 30):
				stripcodigo = i.codigo[0:30]
			else:
				stripcodigo = i.codigo
			self.m.setItem(row, 3, QtGui.QStandardItem(stripcodigo))
			if (i.estado == i.PROS_EJEC):
<<<<<<< .mine
				self.m.setItem(row, 3, QtGui.QStandardItem("En Ejecucion"))
=======
				self.m.setItem(row, 4, QtGui.QStandardItem("En Ejecución"))
>>>>>>> .r6
			elif (i.estado == i.PROS_LIMBO):
				self.m.setItem(row, 4, QtGui.QStandardItem("En Limbo"))
			else:
				self.m.setItem(row, 4, QtGui.QStandardItem("Listo"))
			row = row + 1

