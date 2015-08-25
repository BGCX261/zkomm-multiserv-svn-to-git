# Form implementation generated from reading ui file 'ServidorUI.ui'
#
# Created: Sun Oct 21 19:11:54 2007
#      by: PyQt4 UI code generator 4.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,725,432).size()).expandedTo(MainWindow.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setObjectName("gridlayout")

        self.tabwMainTabs = QtGui.QTabWidget(self.centralwidget)
        self.tabwMainTabs.setObjectName("tabwMainTabs")

        self.tabNodos = QtGui.QWidget()
        self.tabNodos.setObjectName("tabNodos")

        self.grpbNodoConectar = QtGui.QGroupBox(self.tabNodos)
        self.grpbNodoConectar.setGeometry(QtCore.QRect(10,10,681,81))
        self.grpbNodoConectar.setObjectName("grpbNodoConectar")

        self.lblTNodoNombre = QtGui.QLabel(self.grpbNodoConectar)
        self.lblTNodoNombre.setGeometry(QtCore.QRect(10,20,51,21))
        self.lblTNodoNombre.setObjectName("lblTNodoNombre")

        self.txtNodoNombre = QtGui.QLineEdit(self.grpbNodoConectar)
        self.txtNodoNombre.setGeometry(QtCore.QRect(70,20,121,20))
        self.txtNodoNombre.setMaxLength(256)
        self.txtNodoNombre.setObjectName("txtNodoNombre")

        self.lblTNodoIP = QtGui.QLabel(self.grpbNodoConectar)
        self.lblTNodoIP.setGeometry(QtCore.QRect(210,20,21,21))
        self.lblTNodoIP.setObjectName("lblTNodoIP")

        self.txtNodoIP = QtGui.QLineEdit(self.grpbNodoConectar)
        self.txtNodoIP.setGeometry(QtCore.QRect(240,20,110,20))
        self.txtNodoIP.setAlignment(QtCore.Qt.AlignCenter)
        self.txtNodoIP.setObjectName("txtNodoIP")

        self.lblTNodoPuerto = QtGui.QLabel(self.grpbNodoConectar)
        self.lblTNodoPuerto.setGeometry(QtCore.QRect(370,20,46,21))
        self.lblTNodoPuerto.setObjectName("lblTNodoPuerto")

        self.spnNodoPuerto = QtGui.QSpinBox(self.grpbNodoConectar)
        self.spnNodoPuerto.setGeometry(QtCore.QRect(420,20,61,22))
        self.spnNodoPuerto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnNodoPuerto.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.spnNodoPuerto.setAccelerated(True)
        self.spnNodoPuerto.setMinimum(1)
        self.spnNodoPuerto.setMaximum(65535)
        self.spnNodoPuerto.setObjectName("spnNodoPuerto")

        self.lblTNodoNumProc = QtGui.QLabel(self.grpbNodoConectar)
        self.lblTNodoNumProc.setGeometry(QtCore.QRect(500,20,97,21))
        self.lblTNodoNumProc.setObjectName("lblTNodoNumProc")

        self.spnNodoNumProc = QtGui.QSpinBox(self.grpbNodoConectar)
        self.spnNodoNumProc.setGeometry(QtCore.QRect(610,20,46,22))
        self.spnNodoNumProc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnNodoNumProc.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.spnNodoNumProc.setMinimum(1)
        self.spnNodoNumProc.setObjectName("spnNodoNumProc")

        self.btnEscanearRed = QtGui.QPushButton(self.grpbNodoConectar)
        self.btnEscanearRed.setGeometry(QtCore.QRect(10,50,191,24))
        self.btnEscanearRed.setObjectName("btnEscanearRed")

        self.chkNodoIniciar = QtGui.QCheckBox(self.grpbNodoConectar)
        self.chkNodoIniciar.setGeometry(QtCore.QRect(480,50,70,21))
        self.chkNodoIniciar.setObjectName("chkNodoIniciar")

        self.btnNodoConectar = QtGui.QPushButton(self.grpbNodoConectar)
        self.btnNodoConectar.setGeometry(QtCore.QRect(544,50,111,24))
        self.btnNodoConectar.setObjectName("btnNodoConectar")

        self.tbleTablaNodos = QtGui.QTableWidget(self.tabNodos)
        self.tbleTablaNodos.setGeometry(QtCore.QRect(10,110,681,231))
        self.tbleTablaNodos.setObjectName("tbleTablaNodos")

        self.line = QtGui.QFrame(self.tabNodos)
        self.line.setGeometry(QtCore.QRect(10,90,681,20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabwMainTabs.addTab(self.tabNodos,"")

        self.tabProcesos = QtGui.QWidget()
        self.tabProcesos.setObjectName("tabProcesos")

        self.btnProcsCrear = QtGui.QPushButton(self.tabProcesos)
        self.btnProcsCrear.setGeometry(QtCore.QRect(10,10,191,24))
        self.btnProcsCrear.setObjectName("btnProcsCrear")

        self.tbleTablaProcesos = QtGui.QTableWidget(self.tabProcesos)
        self.tbleTablaProcesos.setGeometry(QtCore.QRect(10,40,681,301))
        self.tbleTablaProcesos.setObjectName("tbleTablaProcesos")
        self.tabwMainTabs.addTab(self.tabProcesos,"")

        self.tabCalendarizador = QtGui.QWidget()
        self.tabCalendarizador.setObjectName("tabCalendarizador")

        self.grpbAlgoritmoCal = QtGui.QGroupBox(self.tabCalendarizador)
        self.grpbAlgoritmoCal.setGeometry(QtCore.QRect(10,10,341,80))
        self.grpbAlgoritmoCal.setObjectName("grpbAlgoritmoCal")

        self.gridLayout = QtGui.QWidget(self.grpbAlgoritmoCal)
        self.gridLayout.setGeometry(QtCore.QRect(10,20,321,51))
        self.gridLayout.setObjectName("gridLayout")

        self.gridlayout1 = QtGui.QGridLayout(self.gridLayout)
        self.gridlayout1.setObjectName("gridlayout1")

        self.rdbAlgoritmo1 = QtGui.QRadioButton(self.gridLayout)
        self.rdbAlgoritmo1.setObjectName("rdbAlgoritmo1")
        self.gridlayout1.addWidget(self.rdbAlgoritmo1,0,0,1,1)

        self.rdbAlgoritmo2 = QtGui.QRadioButton(self.gridLayout)
        self.rdbAlgoritmo2.setObjectName("rdbAlgoritmo2")
        self.gridlayout1.addWidget(self.rdbAlgoritmo2,0,1,1,1)

        self.rdbAlgoritmo3 = QtGui.QRadioButton(self.gridLayout)
        self.rdbAlgoritmo3.setObjectName("rdbAlgoritmo3")
        self.gridlayout1.addWidget(self.rdbAlgoritmo3,1,0,1,1)

        self.rdbAlgoritmo4 = QtGui.QRadioButton(self.gridLayout)
        self.rdbAlgoritmo4.setObjectName("rdbAlgoritmo4")
        self.gridlayout1.addWidget(self.rdbAlgoritmo4,1,1,1,1)

        self.grpbPrssEspera = QtGui.QGroupBox(self.tabCalendarizador)
        self.grpbPrssEspera.setGeometry(QtCore.QRect(10,100,341,241))
        self.grpbPrssEspera.setObjectName("grpbPrssEspera")

        self.tbleCalProcEspera = QtGui.QTableWidget(self.grpbPrssEspera)
        self.tbleCalProcEspera.setGeometry(QtCore.QRect(10,20,321,211))
        self.tbleCalProcEspera.setObjectName("tbleCalProcEspera")

        self.grpbProcsDisp = QtGui.QGroupBox(self.tabCalendarizador)
        self.grpbProcsDisp.setGeometry(QtCore.QRect(350,100,341,241))
        self.grpbProcsDisp.setObjectName("grpbProcsDisp")

        self.tbleCalProcsDisp = QtGui.QTableWidget(self.grpbProcsDisp)
        self.tbleCalProcsDisp.setGeometry(QtCore.QRect(10,20,321,211))
        self.tbleCalProcsDisp.setObjectName("tbleCalProcsDisp")
        self.tabwMainTabs.addTab(self.tabCalendarizador,"")

        self.tabProcesadores = QtGui.QWidget()
        self.tabProcesadores.setObjectName("tabProcesadores")

        self.grpbProcsOcup = QtGui.QGroupBox(self.tabProcesadores)
        self.grpbProcsOcup.setGeometry(QtCore.QRect(10,10,381,331))
        self.grpbProcsOcup.setObjectName("grpbProcsOcup")

        self.tableWidget = QtGui.QTableWidget(self.grpbProcsOcup)
        self.tableWidget.setGeometry(QtCore.QRect(10,20,361,301))
        self.tableWidget.setObjectName("tableWidget")

        self.groupBox_2 = QtGui.QGroupBox(self.tabProcesadores)
        self.groupBox_2.setGeometry(QtCore.QRect(390,10,301,331))
        self.groupBox_2.setObjectName("groupBox_2")

        self.tableWidget_2 = QtGui.QTableWidget(self.groupBox_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(10,20,281,301))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tabwMainTabs.addTab(self.tabProcesadores,"")
        self.gridlayout.addWidget(self.tabwMainTabs,0,0,1,1)
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
        self.tabwMainTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "libZkomm", None, QtGui.QApplication.UnicodeUTF8))
        self.grpbNodoConectar.setTitle(QtGui.QApplication.translate("MainWindow", "Conectar a un nodo", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTNodoNombre.setText(QtGui.QApplication.translate("MainWindow", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTNodoIP.setText(QtGui.QApplication.translate("MainWindow", "IP:", None, QtGui.QApplication.UnicodeUTF8))
        self.txtNodoIP.setInputMask(QtGui.QApplication.translate("MainWindow", "###.###.###.###; ", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTNodoPuerto.setText(QtGui.QApplication.translate("MainWindow", "Puerto:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTNodoNumProc.setText(QtGui.QApplication.translate("MainWindow", "Num. Procesadores:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEscanearRed.setText(QtGui.QApplication.translate("MainWindow", "Escanear la red por nodos", None, QtGui.QApplication.UnicodeUTF8))
        self.chkNodoIniciar.setText(QtGui.QApplication.translate("MainWindow", "Iniciar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNodoConectar.setText(QtGui.QApplication.translate("MainWindow", "Conectar a nodo", None, QtGui.QApplication.UnicodeUTF8))
        self.tbleTablaNodos.setRowCount(10)
        self.tbleTablaNodos.setColumnCount(4)
        self.tbleTablaNodos.clear()
        self.tbleTablaNodos.setColumnCount(4)
        self.tbleTablaNodos.setRowCount(10)

        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(QtGui.QApplication.translate("MainWindow", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tbleTablaNodos.setHorizontalHeaderItem(0,headerItem)

        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(QtGui.QApplication.translate("MainWindow", "IP", None, QtGui.QApplication.UnicodeUTF8))
        self.tbleTablaNodos.setHorizontalHeaderItem(1,headerItem1)

        headerItem2 = QtGui.QTableWidgetItem()
        headerItem2.setText(QtGui.QApplication.translate("MainWindow", "Puerto", None, QtGui.QApplication.UnicodeUTF8))
        self.tbleTablaNodos.setHorizontalHeaderItem(2,headerItem2)

        headerItem3 = QtGui.QTableWidgetItem()
        headerItem3.setText(QtGui.QApplication.translate("MainWindow", "Procesadores", None, QtGui.QApplication.UnicodeUTF8))
        self.tbleTablaNodos.setHorizontalHeaderItem(3,headerItem3)
        self.tabwMainTabs.setTabText(self.tabwMainTabs.indexOf(self.tabNodos), QtGui.QApplication.translate("MainWindow", "Nodos", None, QtGui.QApplication.UnicodeUTF8))
        self.btnProcsCrear.setText(QtGui.QApplication.translate("MainWindow", "Crear proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.tbleTablaProcesos.setRowCount(10)
        self.tbleTablaProcesos.setColumnCount(6)
        self.tbleTablaProcesos.clear()
        self.tbleTablaProcesos.setColumnCount(6)
        self.tbleTablaProcesos.setRowCount(10)

        headerItem4 = QtGui.QTableWidgetItem()
        headerItem4.setText(QtGui.QApplication.translate("MainWindow", "PId", None, QtGui.QApplication.UnicodeUTF8))
        self.tbleTablaProcesos.setHorizontalHeaderItem(0,headerItem4)

        headerItem5 = QtGui.QTableWidgetItem()
        headerItem5.setText(QtGui.QApplication.translate("MainWindow", "Ejec", None, QtGui.QApplication.UnicodeUTF8))
        self.tbleTablaProcesos.setHorizontalHeaderItem(1,headerItem5)

        headerItem6 = QtGui.QTableWidgetItem()
        headerItem6.setText(QtGui.QApplication.translate("MainWindow", "PId General", None, QtGui.QApplication.UnicodeUTF8))
        self.tbleTablaProcesos.setHorizontalHeaderItem(2,headerItem6)

        headerItem7 = QtGui.QTableWidgetItem()
        headerItem7.setText(QtGui.QApplication.translate("MainWindow", "Nodo", None, QtGui.QApplication.UnicodeUTF8))
        self.tbleTablaProcesos.setHorizontalHeaderItem(3,headerItem7)

        headerItem8 = QtGui.QTableWidgetItem()
        headerItem8.setText(QtGui.QApplication.translate("MainWindow", "Codigo", None, QtGui.QApplication.UnicodeUTF8))
        self.tbleTablaProcesos.setHorizontalHeaderItem(4,headerItem8)

        headerItem9 = QtGui.QTableWidgetItem()
        headerItem9.setText(QtGui.QApplication.translate("MainWindow", "ERT", None, QtGui.QApplication.UnicodeUTF8))
        self.tbleTablaProcesos.setHorizontalHeaderItem(5,headerItem9)
        self.tabwMainTabs.setTabText(self.tabwMainTabs.indexOf(self.tabProcesos), QtGui.QApplication.translate("MainWindow", "Procesos", None, QtGui.QApplication.UnicodeUTF8))
        self.grpbAlgoritmoCal.setTitle(QtGui.QApplication.translate("MainWindow", "Algoritmo de calendarización", None, QtGui.QApplication.UnicodeUTF8))
        self.rdbAlgoritmo1.setText(QtGui.QApplication.translate("MainWindow", "Algoritmo 1", None, QtGui.QApplication.UnicodeUTF8))
        self.rdbAlgoritmo2.setText(QtGui.QApplication.translate("MainWindow", "Algoritmo 2", None, QtGui.QApplication.UnicodeUTF8))
        self.rdbAlgoritmo3.setText(QtGui.QApplication.translate("MainWindow", "Algoritmo 3", None, QtGui.QApplication.UnicodeUTF8))
        self.rdbAlgoritmo4.setText(QtGui.QApplication.translate("MainWindow", "Algoritmo 4", None, QtGui.QApplication.UnicodeUTF8))
        self.grpbPrssEspera.setTitle(QtGui.QApplication.translate("MainWindow", "Procesos en Espera", None, QtGui.QApplication.UnicodeUTF8))
        self.tbleCalProcEspera.setRowCount(10)
        self.tbleCalProcEspera.setColumnCount(2)
        self.tbleCalProcEspera.clear()
        self.tbleCalProcEspera.setColumnCount(2)
        self.tbleCalProcEspera.setRowCount(10)

        headerItem10 = QtGui.QTableWidgetItem()
        headerItem10.setText(QtGui.QApplication.translate("MainWindow", "PId", None, QtGui.QApplication.UnicodeUTF8))
        self.tbleCalProcEspera.setHorizontalHeaderItem(0,headerItem10)

        headerItem11 = QtGui.QTableWidgetItem()
        headerItem11.setText(QtGui.QApplication.translate("MainWindow", "Nodo", None, QtGui.QApplication.UnicodeUTF8))
        self.tbleCalProcEspera.setHorizontalHeaderItem(1,headerItem11)
        self.grpbProcsDisp.setTitle(QtGui.QApplication.translate("MainWindow", "Procesadores Disponibles", None, QtGui.QApplication.UnicodeUTF8))
        self.tbleCalProcsDisp.setRowCount(10)
        self.tbleCalProcsDisp.setColumnCount(2)
        self.tbleCalProcsDisp.clear()
        self.tbleCalProcsDisp.setColumnCount(2)
        self.tbleCalProcsDisp.setRowCount(10)

        headerItem12 = QtGui.QTableWidgetItem()
        headerItem12.setText(QtGui.QApplication.translate("MainWindow", "Nodo", None, QtGui.QApplication.UnicodeUTF8))
        self.tbleCalProcsDisp.setHorizontalHeaderItem(0,headerItem12)

        headerItem13 = QtGui.QTableWidgetItem()
        headerItem13.setText(QtGui.QApplication.translate("MainWindow", "Proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.tbleCalProcsDisp.setHorizontalHeaderItem(1,headerItem13)
        self.tabwMainTabs.setTabText(self.tabwMainTabs.indexOf(self.tabCalendarizador), QtGui.QApplication.translate("MainWindow", "Calendarizador", None, QtGui.QApplication.UnicodeUTF8))
        self.grpbProcsOcup.setTitle(QtGui.QApplication.translate("MainWindow", "Procesadores Ocupados", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(10)

        headerItem14 = QtGui.QTableWidgetItem()
        headerItem14.setText(QtGui.QApplication.translate("MainWindow", "ProcId", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(0,headerItem14)

        headerItem15 = QtGui.QTableWidgetItem()
        headerItem15.setText(QtGui.QApplication.translate("MainWindow", "PId", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(1,headerItem15)

        headerItem16 = QtGui.QTableWidgetItem()
        headerItem16.setText(QtGui.QApplication.translate("MainWindow", "Nodo", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(2,headerItem16)

        headerItem17 = QtGui.QTableWidgetItem()
        headerItem17.setText(QtGui.QApplication.translate("MainWindow", "ETA*", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(3,headerItem17)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Procesadores Disponibles", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setRowCount(10)
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.clear()
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(10)

        headerItem18 = QtGui.QTableWidgetItem()
        headerItem18.setText(QtGui.QApplication.translate("MainWindow", "PId", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setHorizontalHeaderItem(0,headerItem18)

        headerItem19 = QtGui.QTableWidgetItem()
        headerItem19.setText(QtGui.QApplication.translate("MainWindow", "Nodo", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setHorizontalHeaderItem(1,headerItem19)
        self.tabwMainTabs.setTabText(self.tabwMainTabs.indexOf(self.tabProcesadores), QtGui.QApplication.translate("MainWindow", "Procesadores", None, QtGui.QApplication.UnicodeUTF8))

