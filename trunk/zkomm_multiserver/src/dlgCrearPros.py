# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgCrearPros.ui'
#
# Created: Sun Dec 02 17:44:13 2007
#      by: PyQt4 UI code generator 4.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_dlgCrearPros(object):
    def setupUi(self, dlgCrearPros):
        dlgCrearPros.setObjectName("dlgCrearPros")
        dlgCrearPros.resize(QtCore.QSize(QtCore.QRect(0,0,499,309).size()).expandedTo(dlgCrearPros.minimumSizeHint()))

        self.gridlayout = QtGui.QGridLayout(dlgCrearPros)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.spnProxPeriodo = QtGui.QGroupBox(dlgCrearPros)
        self.spnProxPeriodo.setObjectName("spnProxPeriodo")

        self.gridlayout1 = QtGui.QGridLayout(self.spnProxPeriodo)
        self.gridlayout1.setMargin(9)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.spnProsPeriodoAl = QtGui.QSpinBox(self.spnProxPeriodo)
        self.spnProsPeriodoAl.setObjectName("spnProsPeriodoAl")
        self.gridlayout1.addWidget(self.spnProsPeriodoAl,6,2,1,1)

        self.spnProsCargaAl = QtGui.QSpinBox(self.spnProxPeriodo)
        self.spnProsCargaAl.setObjectName("spnProsCargaAl")
        self.gridlayout1.addWidget(self.spnProsCargaAl,2,2,1,1)

        self.spnProsCarga = QtGui.QSpinBox(self.spnProxPeriodo)
        self.spnProsCarga.setObjectName("spnProsCarga")
        self.gridlayout1.addWidget(self.spnProsCarga,1,1,1,2)

        self.spnProxPeriodo1 = QtGui.QDoubleSpinBox(self.spnProxPeriodo)
        self.spnProxPeriodo1.setObjectName("spnProxPeriodo1")
        self.gridlayout1.addWidget(self.spnProxPeriodo1,5,1,1,2)

        self.label_4 = QtGui.QLabel(self.spnProxPeriodo)
        self.label_4.setObjectName("label_4")
        self.gridlayout1.addWidget(self.label_4,2,3,1,1)

        self.label_7 = QtGui.QLabel(self.spnProxPeriodo)
        self.label_7.setObjectName("label_7")
        self.gridlayout1.addWidget(self.label_7,6,3,1,1)

        self.label_2 = QtGui.QLabel(self.spnProxPeriodo)
        self.label_2.setObjectName("label_2")
        self.gridlayout1.addWidget(self.label_2,2,1,1,1)

        self.label_5 = QtGui.QLabel(self.spnProxPeriodo)
        self.label_5.setObjectName("label_5")
        self.gridlayout1.addWidget(self.label_5,6,1,1,1)

        self.label = QtGui.QLabel(self.spnProxPeriodo)
        self.label.setObjectName("label")
        self.gridlayout1.addWidget(self.label,0,1,1,2)

        self.label_10 = QtGui.QLabel(self.spnProxPeriodo)
        self.label_10.setObjectName("label_10")
        self.gridlayout1.addWidget(self.label_10,0,0,1,1)

        self.label_3 = QtGui.QLabel(self.spnProxPeriodo)
        self.label_3.setObjectName("label_3")
        self.gridlayout1.addWidget(self.label_3,1,3,1,1)

        self.label_6 = QtGui.QLabel(self.spnProxPeriodo)
        self.label_6.setObjectName("label_6")
        self.gridlayout1.addWidget(self.label_6,5,3,1,1)

        self.label_11 = QtGui.QLabel(self.spnProxPeriodo)
        self.label_11.setObjectName("label_11")
        self.gridlayout1.addWidget(self.label_11,4,1,1,3)

        self.line = QtGui.QFrame(self.spnProxPeriodo)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridlayout1.addWidget(self.line,3,1,1,3)

        self.txtProsCodigo = QtGui.QTextEdit(self.spnProxPeriodo)
        self.txtProsCodigo.setObjectName("txtProsCodigo")
        self.gridlayout1.addWidget(self.txtProsCodigo,1,0,6,1)
        self.gridlayout.addWidget(self.spnProxPeriodo,0,0,1,4)

        self.buttonBox = QtGui.QDialogButtonBox(dlgCrearPros)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox,1,3,1,1)

        self.label_9 = QtGui.QLabel(dlgCrearPros)
        self.label_9.setObjectName("label_9")
        self.gridlayout.addWidget(self.label_9,1,2,1,1)

        self.spnNumPros = QtGui.QSpinBox(dlgCrearPros)
        self.spnNumPros.setObjectName("spnNumPros")
        self.gridlayout.addWidget(self.spnNumPros,1,1,1,1)

        self.label_8 = QtGui.QLabel(dlgCrearPros)
        self.label_8.setObjectName("label_8")
        self.gridlayout.addWidget(self.label_8,1,0,1,1)

        self.retranslateUi(dlgCrearPros)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),dlgCrearPros.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),dlgCrearPros.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgCrearPros)

    def retranslateUi(self, dlgCrearPros):
        dlgCrearPros.setWindowTitle(QtGui.QApplication.translate("dlgCrearPros", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.spnProxPeriodo.setTitle(QtGui.QApplication.translate("dlgCrearPros", "Datos del proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("dlgCrearPros", "Unds", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("dlgCrearPros", "seg.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dlgCrearPros", "+ Aleatorio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("dlgCrearPros", "+ Aleatorio", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dlgCrearPros", "Carga del proceso:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("dlgCrearPros", "Código del proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("dlgCrearPros", "Unds", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("dlgCrearPros", "seg.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("dlgCrearPros", "Crear cada", None, QtGui.QApplication.UnicodeUTF8))
        self.txtProsCodigo.setHtml(QtGui.QApplication.translate("dlgCrearPros", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:9pt;\">print \"Hola, mundo!\"</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("dlgCrearPros", "procesos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("dlgCrearPros", "Crear", None, QtGui.QApplication.UnicodeUTF8))

