# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created: Sun Jan 15 17:18:51 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ventana_principal(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(541, 374)
        self.lb_titulo = QtGui.QLabel(Form)
        self.lb_titulo.setGeometry(QtCore.QRect(30, 60, 471, 111))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setWeight(75)
        font.setBold(True)
        self.lb_titulo.setFont(font)
        self.lb_titulo.setTextFormat(QtCore.Qt.PlainText)
        self.lb_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_titulo.setWordWrap(True)
        self.lb_titulo.setObjectName("lb_titulo")
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 190, 301, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_foto_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.lb_foto_2.setObjectName("lb_foto_2")
        self.horizontalLayout.addWidget(self.lb_foto_2)
        self.lb_foto_1 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.lb_foto_1.setObjectName("lb_foto_1")
        self.horizontalLayout.addWidget(self.lb_foto_1)
        self.btn_empezar = QtGui.QPushButton(Form)
        self.btn_empezar.setGeometry(QtCore.QRect(60, 330, 99, 27))
        self.btn_empezar.setObjectName("btn_empezar")
        self.btn_salir = QtGui.QPushButton(Form)
        self.btn_salir.setGeometry(QtCore.QRect(200, 330, 99, 27))
        self.btn_salir.setObjectName("btn_salir")
        self.mostrar_guia = QtGui.QPushButton(Form)
        self.mostrar_guia.setGeometry(QtCore.QRect(350, 330, 99, 27))
        self.mostrar_guia.setObjectName("mostrar_guia")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "DIRe", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_titulo.setText(QtGui.QApplication.translate("Form", "Diseño de Reactores Ideales", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_foto_2.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_foto_1.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_empezar.setText(QtGui.QApplication.translate("Form", "Empezar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_salir.setText(QtGui.QApplication.translate("Form", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.mostrar_guia.setText(QtGui.QApplication.translate("Form", "Guia Usuario", None, QtGui.QApplication.UnicodeUTF8))

