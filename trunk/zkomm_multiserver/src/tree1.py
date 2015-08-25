# Form implementation generated from reading ui file 'Tree1.ui'
#
# Created: Mon Nov 12 15:31:50 2007
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

import sys
import time
from PyQt4 import QtCore, QtGui
from modelo_lista_procesadores import *
from lista_procesadores_procesador import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,800,600).size()).expandedTo(MainWindow.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(20,20,681,541))
        self.treeView.setObjectName("treeView")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,800,27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))


app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
ui = Ui_MainWindow()
modelo = modelo_lista_procesadores(window, (procesador("idnodo1", "ident1", 1001), procesador("idnodo2", "ident1", 2002)))
ui.setupUi(window)
window.show()
ui.treeView.setModel(modelo.m)
time.sleep(3)
modelo.m.setHeaderData(0,QtCore.Qt.Horizontal,QtCore.QVariant("Columna1"))
time.sleep(1)
sys.exit(app.exec_())
