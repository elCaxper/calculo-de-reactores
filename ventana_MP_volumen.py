# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_MP_volumen.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1022, 501)
        self._2 = QtGui.QHBoxLayout(Form)
        self._2.setContentsMargins(-1, 20, -1, 25)
        self._2.setObjectName(_fromUtf8("_2"))
        spacerItem = QtGui.QSpacerItem(12, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self._2.addItem(spacerItem)
        self.Izquierda = QtGui.QVBoxLayout()
        self.Izquierda.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.Izquierda.setContentsMargins(0, -1, -1, -1)
        self.Izquierda.setObjectName(_fromUtf8("Izquierda"))
        self.Reaccion = QtGui.QGroupBox(Form)
        self.Reaccion.setMinimumSize(QtCore.QSize(400, 110))
        self.Reaccion.setMaximumSize(QtCore.QSize(400, 110))
        self.Reaccion.setObjectName(_fromUtf8("Reaccion"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.Reaccion)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.lb_cao_12 = QtGui.QLabel(self.Reaccion)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.lb_cao_12.setFont(font)
        self.lb_cao_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_cao_12.setObjectName(_fromUtf8("lb_cao_12"))
        self.verticalLayout_4.addWidget(self.lb_cao_12)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lb_cao_13 = QtGui.QLabel(self.Reaccion)
        self.lb_cao_13.setObjectName(_fromUtf8("lb_cao_13"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lb_cao_13)
        self.le_molA = QtGui.QLineEdit(self.Reaccion)
        self.le_molA.setMaximumSize(QtCore.QSize(70, 16777215))
        self.le_molA.setObjectName(_fromUtf8("le_molA"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.le_molA)
        self.horizontalLayout_14.addLayout(self.formLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.lb_cao_14 = QtGui.QLabel(self.Reaccion)
        self.lb_cao_14.setObjectName(_fromUtf8("lb_cao_14"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.lb_cao_14)
        self.le_molB = QtGui.QLineEdit(self.Reaccion)
        self.le_molB.setMaximumSize(QtCore.QSize(70, 16777215))
        self.le_molB.setObjectName(_fromUtf8("le_molB"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.le_molB)
        self.horizontalLayout_14.addLayout(self.formLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.Izquierda.addWidget(self.Reaccion)
        self.Parmetros_entrada = QtGui.QGroupBox(Form)
        self.Parmetros_entrada.setMinimumSize(QtCore.QSize(400, 0))
        self.Parmetros_entrada.setMaximumSize(QtCore.QSize(400, 16777215))
        self.Parmetros_entrada.setObjectName(_fromUtf8("Parmetros_entrada"))
        self.verticalLayout = QtGui.QVBoxLayout(self.Parmetros_entrada)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.lb_cao_6 = QtGui.QLabel(self.Parmetros_entrada)
        self.lb_cao_6.setObjectName(_fromUtf8("lb_cao_6"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.lb_cao_6)
        self.lb_cao_5 = QtGui.QLabel(self.Parmetros_entrada)
        self.lb_cao_5.setObjectName(_fromUtf8("lb_cao_5"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.lb_cao_5)
        self.lb_cao_9 = QtGui.QLabel(self.Parmetros_entrada)
        self.lb_cao_9.setObjectName(_fromUtf8("lb_cao_9"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.lb_cao_9)
        self.lb_cao_4 = QtGui.QLabel(self.Parmetros_entrada)
        self.lb_cao_4.setObjectName(_fromUtf8("lb_cao_4"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.lb_cao_4)
        self.lb_cao_7 = QtGui.QLabel(self.Parmetros_entrada)
        self.lb_cao_7.setObjectName(_fromUtf8("lb_cao_7"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.lb_cao_7)
        self.lb_cao_8 = QtGui.QLabel(self.Parmetros_entrada)
        self.lb_cao_8.setObjectName(_fromUtf8("lb_cao_8"))
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.LabelRole, self.lb_cao_8)
        self.lb_cao = QtGui.QLabel(self.Parmetros_entrada)
        self.lb_cao.setObjectName(_fromUtf8("lb_cao"))
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.LabelRole, self.lb_cao)
        self.cb_orden = QtGui.QComboBox(self.Parmetros_entrada)
        self.cb_orden.setMinimumSize(QtCore.QSize(146, 27))
        self.cb_orden.setObjectName(_fromUtf8("cb_orden"))
        self.cb_orden.addItem(_fromUtf8(""))
        self.cb_orden.addItem(_fromUtf8(""))
        self.cb_orden.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.cb_orden)
        self.le_concentracion_ini = QtGui.QLineEdit(self.Parmetros_entrada)
        self.le_concentracion_ini.setMinimumSize(QtCore.QSize(146, 27))
        self.le_concentracion_ini.setObjectName(_fromUtf8("le_concentracion_ini"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.le_concentracion_ini)
        self.le_temp_fin = QtGui.QLineEdit(self.Parmetros_entrada)
        self.le_temp_fin.setMinimumSize(QtCore.QSize(146, 27))
        self.le_temp_fin.setObjectName(_fromUtf8("le_temp_fin"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.le_temp_fin)
        self.le_ener_act = QtGui.QLineEdit(self.Parmetros_entrada)
        self.le_ener_act.setMinimumSize(QtCore.QSize(146, 27))
        self.le_ener_act.setObjectName(_fromUtf8("le_ener_act"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.le_ener_act)
        self.le_k = QtGui.QLineEdit(self.Parmetros_entrada)
        self.le_k.setMinimumSize(QtCore.QSize(146, 27))
        self.le_k.setObjectName(_fromUtf8("le_k"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.FieldRole, self.le_k)
        self.le_caudal = QtGui.QLineEdit(self.Parmetros_entrada)
        self.le_caudal.setMinimumSize(QtCore.QSize(146, 27))
        self.le_caudal.setObjectName(_fromUtf8("le_caudal"))
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.FieldRole, self.le_caudal)
        self.le_conv_fin = QtGui.QLineEdit(self.Parmetros_entrada)
        self.le_conv_fin.setMinimumSize(QtCore.QSize(146, 27))
        self.le_conv_fin.setObjectName(_fromUtf8("le_conv_fin"))
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.FieldRole, self.le_conv_fin)
        spacerItem2 = QtGui.QSpacerItem(20, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.formLayout_3.setItem(7, QtGui.QFormLayout.LabelRole, spacerItem2)
        spacerItem3 = QtGui.QSpacerItem(20, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.formLayout_3.setItem(1, QtGui.QFormLayout.LabelRole, spacerItem3)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.btn_reset = QtGui.QPushButton(self.Parmetros_entrada)
        self.btn_reset.setObjectName(_fromUtf8("btn_reset"))
        self.verticalLayout.addWidget(self.btn_reset)
        self.Izquierda.addWidget(self.Parmetros_entrada)
        self._2.addLayout(self.Izquierda)
        spacerItem4 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self._2.addItem(spacerItem4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem5 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.plot = PlotWidget(Form)
        self.plot.setMinimumSize(QtCore.QSize(500, 0))
        self.plot.setObjectName(_fromUtf8("plot"))
        self.verticalLayout_2.addWidget(self.plot)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.lb_cao_10 = QtGui.QLabel(Form)
        self.lb_cao_10.setObjectName(_fromUtf8("lb_cao_10"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.lb_cao_10)
        self.le_xa = QtGui.QLineEdit(Form)
        self.le_xa.setMaximumSize(QtCore.QSize(100, 16777215))
        self.le_xa.setObjectName(_fromUtf8("le_xa"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.le_xa)
        self.horizontalLayout_11.addLayout(self.formLayout_4)
        self.formLayout_5 = QtGui.QFormLayout()
        self.formLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.lb_cao_2 = QtGui.QLabel(Form)
        self.lb_cao_2.setObjectName(_fromUtf8("lb_cao_2"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.lb_cao_2)
        self.le_volumen = QtGui.QLineEdit(Form)
        self.le_volumen.setMaximumSize(QtCore.QSize(100, 16777215))
        self.le_volumen.setObjectName(_fromUtf8("le_volumen"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.le_volumen)
        self.horizontalLayout_11.addLayout(self.formLayout_5)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.btn_mostrar_resultados = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mostrar_resultados.sizePolicy().hasHeightForWidth())
        self.btn_mostrar_resultados.setSizePolicy(sizePolicy)
        self.btn_mostrar_resultados.setMinimumSize(QtCore.QSize(0, 20))
        self.btn_mostrar_resultados.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_mostrar_resultados.setFont(font)
        self.btn_mostrar_resultados.setObjectName(_fromUtf8("btn_mostrar_resultados"))
        self.horizontalLayout_11.addWidget(self.btn_mostrar_resultados)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        spacerItem7 = QtGui.QSpacerItem(20, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem7)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.btn_ejecutar = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ejecutar.sizePolicy().hasHeightForWidth())
        self.btn_ejecutar.setSizePolicy(sizePolicy)
        self.btn_ejecutar.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_ejecutar.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btn_ejecutar.setFont(font)
        self.btn_ejecutar.setObjectName(_fromUtf8("btn_ejecutar"))
        self.horizontalLayout_17.addWidget(self.btn_ejecutar)
        self.verticalLayout_5.addLayout(self.horizontalLayout_17)
        spacerItem8 = QtGui.QSpacerItem(20, 50, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem8)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setContentsMargins(0, 20, -1, -1)
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem9)
        self.btn_cerrar = QtGui.QPushButton(Form)
        self.btn_cerrar.setMinimumSize(QtCore.QSize(200, 40))
        self.btn_cerrar.setMaximumSize(QtCore.QSize(200, 40))
        self.btn_cerrar.setObjectName(_fromUtf8("btn_cerrar"))
        self.horizontalLayout_21.addWidget(self.btn_cerrar)
        self.verticalLayout_5.addLayout(self.horizontalLayout_21)
        self._2.addLayout(self.verticalLayout_5)
        spacerItem10 = QtGui.QSpacerItem(12, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self._2.addItem(spacerItem10)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Reactor MP - Cálculo de volumen", None))
        self.Reaccion.setTitle(_translate("Form", "Reacción", None))
        self.lb_cao_12.setText(_translate("Form", "aA ---> bR", None))
        self.lb_cao_13.setText(_translate("Form", "a [mol]", None))
        self.lb_cao_14.setText(_translate("Form", "b [mol]", None))
        self.Parmetros_entrada.setTitle(_translate("Form", "Parámetros de entrada", None))
        self.lb_cao_6.setText(_translate("Form", "Orden de reacción", None))
        self.lb_cao_5.setText(_translate("Form", "Concentración inicial [mol/L]", None))
        self.lb_cao_9.setText(_translate("Form", "Temperatura final [K]", None))
        self.lb_cao_4.setText(_translate("Form", "Energía de activación [J/mol]", None))
        self.lb_cao_7.setText(_translate("Form", "Constante ko", None))
        self.lb_cao_8.setText(_translate("Form", "Caudal [L/s]", None))
        self.lb_cao.setText(_translate("Form", "Conversión final", None))
        self.cb_orden.setItemText(0, _translate("Form", "0", None))
        self.cb_orden.setItemText(1, _translate("Form", "1", None))
        self.cb_orden.setItemText(2, _translate("Form", "2", None))
        self.btn_reset.setText(_translate("Form", "Resetear parámetros", None))
        self.lb_cao_10.setText(_translate("Form", "Xa", None))
        self.lb_cao_2.setText(_translate("Form", "Volumen [L]", None))
        self.btn_mostrar_resultados.setText(_translate("Form", "Mostrar Resultados", None))
        self.btn_ejecutar.setText(_translate("Form", "CALCULAR", None))
        self.btn_cerrar.setText(_translate("Form", "Volver al menú principal", None))

from pyqtgraph import PlotWidget
