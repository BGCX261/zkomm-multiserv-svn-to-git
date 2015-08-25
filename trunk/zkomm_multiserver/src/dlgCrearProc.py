# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgCrearProc.ui'
#
# Created: Sun Dec 02 17:44:06 2007
#      by: PyQt4 UI code generator 4.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_dlgCrearProc(object):
    def setupUi(self, dlgCrearProc):
        dlgCrearProc.setObjectName("dlgCrearProc")
        dlgCrearProc.resize(QtCore.QSize(QtCore.QRect(0,0,263,173).size()).expandedTo(dlgCrearProc.minimumSizeHint()))

        self.gridlayout = QtGui.QGridLayout(dlgCrearProc)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.btnAceptar = QtGui.QPushButton(dlgCrearProc)
        self.btnAceptar.setObjectName("btnAceptar")
        self.gridlayout.addWidget(self.btnAceptar,3,0,1,2)

        self.btnCancelar = QtGui.QPushButton(dlgCrearProc)
        self.btnCancelar.setObjectName("btnCancelar")
        self.gridlayout.addWidget(self.btnCancelar,3,2,1,2)

        self.spnProcCant = QtGui.QSpinBox(dlgCrearProc)
        self.spnProcCant.setObjectName("spnProcCant")
        self.gridlayout.addWidget(self.spnProcCant,0,1,1,2)

        self.label = QtGui.QLabel(dlgCrearProc)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,0,0,1,1)

        self.spnProcVel = QtGui.QSpinBox(dlgCrearProc)
        self.spnProcVel.setObjectName("spnProcVel")
        self.gridlayout.addWidget(self.spnProcVel,1,1,1,2)

        self.label_2 = QtGui.QLabel(dlgCrearProc)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,0,3,1,1)

        self.label_5 = QtGui.QLabel(dlgCrearProc)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5,2,3,1,1)

        self.label_4 = QtGui.QLabel(dlgCrearProc)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4,1,3,1,1)

        self.label_6 = QtGui.QLabel(dlgCrearProc)
        self.label_6.setObjectName("label_6")
        self.gridlayout.addWidget(self.label_6,2,0,1,1)

        self.label_3 = QtGui.QLabel(dlgCrearProc)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3,1,0,1,1)

        self.spinBox = QtGui.QSpinBox(dlgCrearProc)
        self.spinBox.setObjectName("spinBox")
        self.gridlayout.addWidget(self.spinBox,2,1,1,2)

        self.retranslateUi(dlgCrearProc)
        QtCore.QObject.connect(self.btnAceptar,QtCore.SIGNAL("clicked()"),dlgCrearProc.accept)
        QtCore.QObject.connect(self.btnCancelar,QtCore.SIGNAL("clicked()"),dlgCrearProc.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgCrearProc)

    def retranslateUi(self, dlgCrearProc):
        dlgCrearProc.setWindowTitle(QtGui.QApplication.translate("dlgCrearProc", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAceptar.setText(QtGui.QApplication.translate("dlgCrearProc", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancelar.setText(QtGui.QApplication.translate("dlgCrearProc", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dlgCrearProc", "Crear:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dlgCrearProc", "procesadores", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("dlgCrearProc", "U/s aleatorias", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("dlgCrearProc", "U/s", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("dlgCrearProc", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("dlgCrearProc", "Con velocidad", None, QtGui.QApplication.UnicodeUTF8))

