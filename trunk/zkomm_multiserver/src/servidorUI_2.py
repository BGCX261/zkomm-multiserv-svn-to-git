# -*- coding: utf8 -*-

# Form implementation generated from reading ui file '..\ui\servidorUI_2.ui'
#
# Created: Fri Nov 16 13:46:30 2007
#      by: PyQt4 UI code generator 4.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,725,432).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setMinimumSize(QtCore.QSize(725,432))
        MainWindow.setMaximumSize(QtCore.QSize(725,432))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.tabs = QtGui.QTabWidget(self.centralwidget)
        self.tabs.setObjectName("tabs")

        self.tabAdminNodo = QtGui.QWidget()
        self.tabAdminNodo.setObjectName("tabAdminNodo")

        self.gridlayout1 = QtGui.QGridLayout(self.tabAdminNodo)
        self.gridlayout1.setMargin(9)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.grpbNodoConectar = QtGui.QGroupBox(self.tabAdminNodo)
        self.grpbNodoConectar.setObjectName("grpbNodoConectar")

        self.gridlayout2 = QtGui.QGridLayout(self.grpbNodoConectar)
        self.gridlayout2.setMargin(9)
        self.gridlayout2.setSpacing(6)
        self.gridlayout2.setObjectName("gridlayout2")

        self.txtNodoNombre = QtGui.QLineEdit(self.grpbNodoConectar)
        self.txtNodoNombre.setMaxLength(256)
        self.txtNodoNombre.setObjectName("txtNodoNombre")
        self.gridlayout2.addWidget(self.txtNodoNombre,0,1,1,3)

        self.txtNodoIP = QtGui.QLineEdit(self.grpbNodoConectar)
        self.txtNodoIP.setAlignment(QtCore.Qt.AlignHCenter)
        self.txtNodoIP.setObjectName("txtNodoIP")
        self.gridlayout2.addWidget(self.txtNodoIP,1,1,1,1)

        self.spnNodoPuerto = QtGui.QSpinBox(self.grpbNodoConectar)
        self.spnNodoPuerto.setAlignment(QtCore.Qt.AlignRight)
        self.spnNodoPuerto.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.spnNodoPuerto.setAccelerated(True)
        self.spnNodoPuerto.setMinimum(1)
        self.spnNodoPuerto.setMaximum(65535)
        self.spnNodoPuerto.setObjectName("spnNodoPuerto")
        self.gridlayout2.addWidget(self.spnNodoPuerto,1,3,1,1)

        self.lblTNodoIP = QtGui.QLabel(self.grpbNodoConectar)
        self.lblTNodoIP.setObjectName("lblTNodoIP")
        self.gridlayout2.addWidget(self.lblTNodoIP,1,0,1,1)

        self.lblTNodoPuerto = QtGui.QLabel(self.grpbNodoConectar)
        self.lblTNodoPuerto.setObjectName("lblTNodoPuerto")
        self.gridlayout2.addWidget(self.lblTNodoPuerto,1,2,1,1)

        self.lblTNodoNombre = QtGui.QLabel(self.grpbNodoConectar)
        self.lblTNodoNombre.setObjectName("lblTNodoNombre")
        self.gridlayout2.addWidget(self.lblTNodoNombre,0,0,1,1)
        self.gridlayout1.addWidget(self.grpbNodoConectar,0,0,1,1)

        self.grpbProcNodo = QtGui.QGroupBox(self.tabAdminNodo)
        self.grpbProcNodo.setObjectName("grpbProcNodo")

        self.gridlayout3 = QtGui.QGridLayout(self.grpbProcNodo)
        self.gridlayout3.setMargin(9)
        self.gridlayout3.setSpacing(6)
        self.gridlayout3.setObjectName("gridlayout3")

        self.pshAgregarProcs = QtGui.QPushButton(self.grpbProcNodo)
        self.pshAgregarProcs.setObjectName("pshAgregarProcs")
        self.gridlayout3.addWidget(self.pshAgregarProcs,1,0,1,1)

        self.admNodoProcTree = QtGui.QTreeView(self.grpbProcNodo)
        self.admNodoProcTree.setObjectName("admNodoProcTree")
        self.gridlayout3.addWidget(self.admNodoProcTree,0,0,1,1)
        self.gridlayout1.addWidget(self.grpbProcNodo,1,0,1,1)

        self.groupBox = QtGui.QGroupBox(self.tabAdminNodo)
        self.groupBox.setObjectName("groupBox")

        self.gridlayout4 = QtGui.QGridLayout(self.groupBox)
        self.gridlayout4.setMargin(9)
        self.gridlayout4.setSpacing(6)
        self.gridlayout4.setObjectName("gridlayout4")

        self.chkConectarRed = QtGui.QCheckBox(self.groupBox)
        self.chkConectarRed.setObjectName("chkConectarRed")
        self.gridlayout4.addWidget(self.chkConectarRed,0,0,1,4)

        self.txtIpServidor = QtGui.QLineEdit(self.groupBox)
        self.txtIpServidor.setEnabled(False)
        self.txtIpServidor.setAlignment(QtCore.Qt.AlignHCenter)
        self.txtIpServidor.setObjectName("txtIpServidor")
        self.gridlayout4.addWidget(self.txtIpServidor,1,1,1,1)

        self.lblTNodoIP_2 = QtGui.QLabel(self.groupBox)
        self.lblTNodoIP_2.setEnabled(True)
        self.lblTNodoIP_2.setObjectName("lblTNodoIP_2")
        self.gridlayout4.addWidget(self.lblTNodoIP_2,1,0,1,1)

        self.spnPuerto_Red_existente = QtGui.QSpinBox(self.groupBox)
        self.spnPuerto_Red_existente.setEnabled(False)
        self.spnPuerto_Red_existente.setAlignment(QtCore.Qt.AlignRight)
        self.spnPuerto_Red_existente.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.spnPuerto_Red_existente.setAccelerated(True)
        self.spnPuerto_Red_existente.setMinimum(1)
        self.spnPuerto_Red_existente.setMaximum(65535)
        self.spnPuerto_Red_existente.setObjectName("spnPuerto_Red_existente")
        self.gridlayout4.addWidget(self.spnPuerto_Red_existente,1,3,1,1)

        self.lblTNodoPuerto_2 = QtGui.QLabel(self.groupBox)
        self.lblTNodoPuerto_2.setObjectName("lblTNodoPuerto_2")
        self.gridlayout4.addWidget(self.lblTNodoPuerto_2,1,2,1,1)
        self.gridlayout1.addWidget(self.groupBox,0,1,1,1)

        self.btnIniciarServ = QtGui.QPushButton(self.tabAdminNodo)
        self.btnIniciarServ.setEnabled(False)
        self.btnIniciarServ.setObjectName("btnIniciarServ")
        self.gridlayout1.addWidget(self.btnIniciarServ,1,1,1,1)
        self.tabs.addTab(self.tabAdminNodo,"")

        self.tabProcesadores = QtGui.QWidget()
        self.tabProcesadores.setObjectName("tabProcesadores")

        self.gridlayout5 = QtGui.QGridLayout(self.tabProcesadores)
        self.gridlayout5.setMargin(9)
        self.gridlayout5.setSpacing(6)
        self.gridlayout5.setObjectName("gridlayout5")

        self.groupBox_2 = QtGui.QGroupBox(self.tabProcesadores)
        self.groupBox_2.setObjectName("groupBox_2")

        self.gridlayout6 = QtGui.QGridLayout(self.groupBox_2)
        self.gridlayout6.setMargin(9)
        self.gridlayout6.setSpacing(6)
        self.gridlayout6.setObjectName("gridlayout6")

        self.treeView_4 = QtGui.QTreeView(self.groupBox_2)
        self.treeView_4.setObjectName("treeView_4")
        self.gridlayout6.addWidget(self.treeView_4,0,0,1,1)
        self.gridlayout5.addWidget(self.groupBox_2,0,1,1,1)

        self.grpbProcsOcup = QtGui.QGroupBox(self.tabProcesadores)
        self.grpbProcsOcup.setObjectName("grpbProcsOcup")

        self.gridlayout7 = QtGui.QGridLayout(self.grpbProcsOcup)
        self.gridlayout7.setMargin(9)
        self.gridlayout7.setSpacing(6)
        self.gridlayout7.setObjectName("gridlayout7")

        self.treeView_3 = QtGui.QTreeView(self.grpbProcsOcup)
        self.treeView_3.setObjectName("treeView_3")
        self.gridlayout7.addWidget(self.treeView_3,0,0,1,1)
        self.gridlayout5.addWidget(self.grpbProcsOcup,0,0,1,1)
        self.tabs.addTab(self.tabProcesadores,"")

        self.tabProcesos = QtGui.QWidget()
        self.tabProcesos.setObjectName("tabProcesos")

        self.gridlayout8 = QtGui.QGridLayout(self.tabProcesos)
        self.gridlayout8.setMargin(9)
        self.gridlayout8.setSpacing(6)
        self.gridlayout8.setObjectName("gridlayout8")

        self.label_2 = QtGui.QLabel(self.tabProcesos)
        self.label_2.setObjectName("label_2")
        self.gridlayout8.addWidget(self.label_2,0,0,1,1)

        self.btnProcsCrear = QtGui.QPushButton(self.tabProcesos)
        self.btnProcsCrear.setObjectName("btnProcsCrear")
        self.gridlayout8.addWidget(self.btnProcsCrear,1,1,1,1)

        self.treeProcesosPropios = QtGui.QTreeView(self.tabProcesos)
        self.treeProcesosPropios.setObjectName("treeProcesosPropios")
        self.gridlayout8.addWidget(self.treeProcesosPropios,1,0,1,1)
        self.tabs.addTab(self.tabProcesos,"")

        self.tabNodos = QtGui.QWidget()
        self.tabNodos.setObjectName("tabNodos")

        self.line = QtGui.QFrame(self.tabNodos)
        self.line.setGeometry(QtCore.QRect(10,60,681,20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")

        self.treeNodosConocidos = QtGui.QTreeView(self.tabNodos)
        self.treeNodosConocidos.setGeometry(QtCore.QRect(10,110,681,231))
        self.treeNodosConocidos.setUniformRowHeights(True)
        self.treeNodosConocidos.setSortingEnabled(True)
        self.treeNodosConocidos.setAllColumnsShowFocus(True)
        self.treeNodosConocidos.setObjectName("treeNodosConocidos")
        self.tabs.addTab(self.tabNodos,"")

        self.tabCalendarizador = QtGui.QWidget()
        self.tabCalendarizador.setObjectName("tabCalendarizador")

        self.gridlayout9 = QtGui.QGridLayout(self.tabCalendarizador)
        self.gridlayout9.setMargin(9)
        self.gridlayout9.setSpacing(6)
        self.gridlayout9.setObjectName("gridlayout9")

        self.grpbProcDisponibles = QtGui.QGroupBox(self.tabCalendarizador)
        self.grpbProcDisponibles.setObjectName("grpbProcDisponibles")

        self.gridlayout10 = QtGui.QGridLayout(self.grpbProcDisponibles)
        self.gridlayout10.setMargin(9)
        self.gridlayout10.setSpacing(6)
        self.gridlayout10.setObjectName("gridlayout10")

        self.tvProcDisponibles = QtGui.QTreeView(self.grpbProcDisponibles)
        self.tvProcDisponibles.setObjectName("tvProcDisponibles")
        self.gridlayout10.addWidget(self.tvProcDisponibles,0,0,1,1)
        self.gridlayout9.addWidget(self.grpbProcDisponibles,1,1,1,1)

        self.grpbProsEspera = QtGui.QGroupBox(self.tabCalendarizador)
        self.grpbProsEspera.setObjectName("grpbProsEspera")

        self.gridlayout11 = QtGui.QGridLayout(self.grpbProsEspera)
        self.gridlayout11.setMargin(9)
        self.gridlayout11.setSpacing(6)
        self.gridlayout11.setObjectName("gridlayout11")

        self.tvProsEspera = QtGui.QTreeView(self.grpbProsEspera)
        self.tvProsEspera.setObjectName("tvProsEspera")
        self.gridlayout11.addWidget(self.tvProsEspera,0,0,1,1)
        self.gridlayout9.addWidget(self.grpbProsEspera,1,0,1,1)

        self.grpbAlgoritmoCal = QtGui.QGroupBox(self.tabCalendarizador)
        self.grpbAlgoritmoCal.setObjectName("grpbAlgoritmoCal")

        self.gridlayout12 = QtGui.QGridLayout(self.grpbAlgoritmoCal)
        self.gridlayout12.setMargin(9)
        self.gridlayout12.setSpacing(6)
        self.gridlayout12.setObjectName("gridlayout12")

        self.gridlayout13 = QtGui.QGridLayout()
        self.gridlayout13.setMargin(0)
        self.gridlayout13.setSpacing(6)
        self.gridlayout13.setObjectName("gridlayout13")

        self.rdbAlgoritmo1 = QtGui.QRadioButton(self.grpbAlgoritmoCal)
        self.rdbAlgoritmo1.setObjectName("rdbAlgoritmo1")
        self.gridlayout13.addWidget(self.rdbAlgoritmo1,0,0,1,1)

        self.rdbAlgoritmo2 = QtGui.QRadioButton(self.grpbAlgoritmoCal)
        self.rdbAlgoritmo2.setObjectName("rdbAlgoritmo2")
        self.gridlayout13.addWidget(self.rdbAlgoritmo2,0,1,1,1)

        self.rdbAlgoritmo3 = QtGui.QRadioButton(self.grpbAlgoritmoCal)
        self.rdbAlgoritmo3.setObjectName("rdbAlgoritmo3")
        self.gridlayout13.addWidget(self.rdbAlgoritmo3,1,0,1,1)

        self.rdbAlgoritmo4 = QtGui.QRadioButton(self.grpbAlgoritmoCal)
        self.rdbAlgoritmo4.setObjectName("rdbAlgoritmo4")
        self.gridlayout13.addWidget(self.rdbAlgoritmo4,1,1,1,1)
        self.gridlayout12.addLayout(self.gridlayout13,0,0,1,1)

        self.pushButton = QtGui.QPushButton(self.grpbAlgoritmoCal)
        self.pushButton.setObjectName("pushButton")
        self.gridlayout12.addWidget(self.pushButton,1,0,1,1)
        self.gridlayout9.addWidget(self.grpbAlgoritmoCal,0,0,1,1)

        self.grpbNodos = QtGui.QGroupBox(self.tabCalendarizador)
        self.grpbNodos.setObjectName("grpbNodos")

        self.gridlayout14 = QtGui.QGridLayout(self.grpbNodos)
        self.gridlayout14.setMargin(9)
        self.gridlayout14.setSpacing(6)
        self.gridlayout14.setObjectName("gridlayout14")

        self.tvCalendNodos = QtGui.QTreeView(self.grpbNodos)
        self.tvCalendNodos.setObjectName("tvCalendNodos")
        self.gridlayout14.addWidget(self.tvCalendNodos,0,0,1,1)
        self.gridlayout9.addWidget(self.grpbNodos,0,1,1,1)
        self.tabs.addTab(self.tabCalendarizador,"")
        self.gridlayout.addWidget(self.tabs,1,0,1,2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.mnubMain = QtGui.QMenuBar(MainWindow)
        self.mnubMain.setGeometry(QtCore.QRect(0,0,725,21))
        self.mnubMain.setObjectName("mnubMain")
        MainWindow.setMenuBar(self.mnubMain)

        self.stsbMain = QtGui.QStatusBar(MainWindow)
        self.stsbMain.setObjectName("stsbMain")
        MainWindow.setStatusBar(self.stsbMain)
        self.lblTNodoNombre.setBuddy(self.txtNodoNombre)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "libZkomm", None, QtGui.QApplication.UnicodeUTF8))
        self.grpbNodoConectar.setTitle(QtGui.QApplication.translate("MainWindow", "Datos del nodo", None, QtGui.QApplication.UnicodeUTF8))
        self.txtNodoIP.setInputMask(QtGui.QApplication.translate("MainWindow", "###.###.###.###; ", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTNodoIP.setText(QtGui.QApplication.translate("MainWindow", "IP:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTNodoPuerto.setText(QtGui.QApplication.translate("MainWindow", "Puerto:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTNodoNombre.setText(QtGui.QApplication.translate("MainWindow", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.grpbProcNodo.setTitle(QtGui.QApplication.translate("MainWindow", "Procesadores del nodo", None, QtGui.QApplication.UnicodeUTF8))
        self.pshAgregarProcs.setText(QtGui.QApplication.translate("MainWindow", "Agregar procesadores", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Otros nodos", None, QtGui.QApplication.UnicodeUTF8))
        self.chkConectarRed.setText(QtGui.QApplication.translate("MainWindow", "Conectar a una red existente", None, QtGui.QApplication.UnicodeUTF8))
        self.txtIpServidor.setInputMask(QtGui.QApplication.translate("MainWindow", "###.###.###.###; ", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTNodoIP_2.setText(QtGui.QApplication.translate("MainWindow", "IP:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTNodoPuerto_2.setText(QtGui.QApplication.translate("MainWindow", "Puerto:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnIniciarServ.setText(QtGui.QApplication.translate("MainWindow", "Iniciar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tabAdminNodo), QtGui.QApplication.translate("MainWindow", "Administrar nodo", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Procesadores Disponibles", None, QtGui.QApplication.UnicodeUTF8))
        self.grpbProcsOcup.setTitle(QtGui.QApplication.translate("MainWindow", "Procesadores Ocupados", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tabProcesadores), QtGui.QApplication.translate("MainWindow", "Procesadores", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Procesos de este nodo:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnProcsCrear.setText(QtGui.QApplication.translate("MainWindow", "Crear proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tabProcesos), QtGui.QApplication.translate("MainWindow", "Procesos", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tabNodos), QtGui.QApplication.translate("MainWindow", "Nodos", None, QtGui.QApplication.UnicodeUTF8))
        self.grpbProcDisponibles.setTitle(QtGui.QApplication.translate("MainWindow", "Procesadores Disponibles", None, QtGui.QApplication.UnicodeUTF8))
        self.grpbProsEspera.setTitle(QtGui.QApplication.translate("MainWindow", "Procesos en Espera", None, QtGui.QApplication.UnicodeUTF8))
        self.grpbAlgoritmoCal.setTitle(QtGui.QApplication.translate("MainWindow", "Algoritmo de calendarización", None, QtGui.QApplication.UnicodeUTF8))
        self.rdbAlgoritmo1.setText(QtGui.QApplication.translate("MainWindow", "Algoritmo 1", None, QtGui.QApplication.UnicodeUTF8))
        self.rdbAlgoritmo2.setText(QtGui.QApplication.translate("MainWindow", "Algoritmo 2", None, QtGui.QApplication.UnicodeUTF8))
        self.rdbAlgoritmo3.setText(QtGui.QApplication.translate("MainWindow", "Algoritmo 3", None, QtGui.QApplication.UnicodeUTF8))
        self.rdbAlgoritmo4.setText(QtGui.QApplication.translate("MainWindow", "Algoritmo 4", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Convertir en administrador", None, QtGui.QApplication.UnicodeUTF8))
        self.grpbNodos.setTitle(QtGui.QApplication.translate("MainWindow", "Estado de los nodos", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tabCalendarizador), QtGui.QApplication.translate("MainWindow", "Calendarizador", None, QtGui.QApplication.UnicodeUTF8))

