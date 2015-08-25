#Abrir una conexion usando la libreria ZKOMM
import zkomm_lista_sockets
from multiserver_servidor import *
import socket
import thread
import time
from PyQt4 import QtGui, QtCore
from servidorUI_2 import Ui_MainWindow
from dlgCrearProc import *
from dlgCrearPros import *
import sys

class multiserver(QtGui.QMainWindow):

	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.dlgconfProc = None
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.dlgCrearProc = QtGui.QDialog(self)
		self.dlgCrearProcUi = Ui_dlgCrearProc()
		self.dlgCrearProcUi.setupUi(self.dlgCrearProc)
		self.dlgCrearPros = QtGui.QDialog(self)
		self.dlgCrearProsUi = Ui_dlgCrearPros()
		self.dlgCrearProsUi.setupUi(self.dlgCrearPros)
		self.servicio = servidor(verbose = False)
		self.conectar_modelos()
		self.conectar_eventos()

	def conectar_modelos(self):
		self.ui.admNodoProcTree.setModel(self.servicio.modelo_lista_proc())
		self.ui.treeNodosConocidos.setModel(self.servicio.modelo_lista_nodos())

	def conectar_eventos(self):
		self.connect(self.ui.pshAgregarProcs, QtCore.SIGNAL("clicked()"), self.llamar_dialogo_Proc)
		self.connect(self.ui.btnProcsCrear, QtCore.SIGNAL("clicked()"), self.llamar_dialogo_Pros)
		self.connect(self.ui.admNodoProcTree, QtCore.SIGNAL("dataChanged(const QModelIndex&,const QModelIndex&)"), self.validar_inicio)
		self.connect(self.ui.spnNodoPuerto, QtCore.SIGNAL("valueChanged(int)"), self.validar_inicio)
		self.connect(self.ui.txtNodoNombre, QtCore.SIGNAL("textChanged(const QString&)"), self.validar_inicio)
		self.connect(self.ui.chkConectarRed, QtCore.SIGNAL("toggled(bool)"), self.activar_conexion_red_existente)
		self.connect(self.ui.txtIpServidor, QtCore.SIGNAL("textChanged(const QString&)"), self.validar_inicio)
		self.connect(self.ui.spnPuerto_Red_existente, QtCore.SIGNAL("valueChanged(int)"), self.validar_inicio)
		self.connect(self.ui.btnIniciarServ, QtCore.SIGNAL("clicked()"), self.iniciar_servicio)

	def llamar_dialogo_Proc(self):
		if (self.dlgCrearProc.exec_()):
			cant = self.dlgCrearProcUi.spnProcCant.value()
			Vel = self.dlgCrearProcUi.spnProcVel.value()
			VelRand = self.dlgCrearProcUi.spinBox.value()
			self.servicio.crear_procesadores(cant, Vel, VelRand, True)

	def llamar_dialogo_Pros(self):
		if (self.dlgCrearPros.exec_()):
			cod = self.dlgCrearProsUi.txtProsCodigo.text()
			cant = self.dlgCrearProsUi.spnNumPros.value()
			carga_base = self.dlgCrearProsUi.spnProsCarga.value()
			rand_carga = self.dlgCrearProsUi.spnProsCargaAl.value()
			T = self.dlgCrearProsUi.spnProxPeriodo1.value()
			rand_T = self.dlgCrearProsUi.spnProsPeriodoAl.value()
			self.servicio.crear_procesos(cod, cant, carga_base, rand_carga, T, rand_T)

	def validar_inicio(self):
		habilitar = False
		if (self.ui.spnNodoPuerto.value >=65000):
			if (self.ui.txtNodoIP.text() != "..."):
				if (self.ui.txtNodoNombre.text() != ""):
					if (len(self.servicio.procesadores.lista)>0):
						if (self.ui.chkConectarRed.isChecked()):
							ip = self.ui.txtIpServidor.text()
							puerto = self.ui.spnPuerto_Red_existente.value()
							if (ip != "..."):
								if (puerto != 1):
									habilitar = True
						else:
							habilitar = True
		if (habilitar):
			self.ui.btnIniciarServ.setEnabled(True)

	def activar_conexion_red_existente(self):
		if self.ui.chkConectarRed.isChecked():
			self.ui.txtIpServidor.setEnabled(True)
			self.ui.spnPuerto_Red_existente.setEnabled(True)
		else:
			self.ui.txtIpServidor.setEnabled(False)
			self.ui.spnPuerto_Red_existente.setEnabled(False)

	def iniciar_servicio(self):
		ip = str(self.ui.txtNodoIP.text())
		puerto = self.ui.spnNodoPuerto.value()
		self.servicio.iniciar(ip, puerto)
		self.servicio.crear_nodo_propio(0, ip, puerto, self.ui.txtNodoNombre.text())
		if (self.ui.chkConectarRed.isChecked()):
			ip = self.ui.txtIpServidor.text()
			puerto = self.ui.spnPuerto_Red_existente.value()
			if (ip != "..."):
				if (puerto != 1):
					self.servicio.conectar_a(ip, puerto)
		self.ui.btnIniciarServ.setText("Detener")
		self.disconnect(self.ui.btnIniciarServ, QtCore.SIGNAL("clicked()"), self.iniciar_servicio)
		self.connect(self.ui.btnIniciarServ, QtCore.SIGNAL("clicked()"), self.detener_servicio)

	def detener_servicio(self):
		self.servicio.detener()
		self.ui.btnIniciarServ.setText("Iniciar")
		self.disconnect(self.ui.btnIniciarServ, QtCore.SIGNAL("clicked()"), self.detener_servicio)
		self.connect(self.ui.btnIniciarServ, QtCore.SIGNAL("clicked()"), self.iniciar_servicio)

	def parseargs(self, arr):
		leer = ''
		for i in arr:
			if (leer == 'procesadores'):
				leer = ''
				cant,Vel,VelRand = i.split(',',2)
				cant = eval(cant)
				Vel = eval(Vel)
				VelRand = eval(VelRand)
				self.servicio.crear_procesadores(cant, Vel, VelRand, True)
			if (leer == 'nombre'):
				leer = ''
				self.ui.txtNodoNombre.setText(i)
			if (leer == 'puerto'):
				leer = ''
				self.ui.spnNodoPuerto.setValue(eval(i))
			if (leer == 'direccion'):
				leer = ''
				self.ui.txtNodoIP.setText(i)
			if (leer == 'conexion'):
				leer = ''
				direc,puerto = i.split(',',1)
				self.ui.chkConectarRed.setCheckState(QtCore.Qt.Checked)
				self.ui.txtIpServidor.setText(direc)
				self.ui.spnPuerto_Red_existente.setValue(eval(puerto))
			if (i == '--name'):
				leer = 'nombre'
			if (i == '--port'):
				leer = 'puerto'
			if (i == '--ip'):
				leer = 'direccion'
			if (i == '--proc'):
				leer = 'procesadores'
			if (i == '--connect'):
				leer = 'conexion'

if (__name__ == "__main__"):
	app = QtGui.QApplication(sys.argv)
	mainwin=multiserver()
	mainwin.show()
	if (len(sys.argv) > 3):
		mainwin.parseargs(sys.argv)

	sys.exit(app.exec_())
