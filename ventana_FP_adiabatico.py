# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_FP_adiabatico.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

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
        Form.resize(1239, 778)
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
        self.Reaccion.setMinimumSize(QtCore.QSize(400, 0))
        self.Reaccion.setMaximumSize(QtCore.QSize(400, 170))
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
        self.lb_cao_13 = QtGui.QLabel(self.Reaccion)
        self.lb_cao_13.setObjectName(_fromUtf8("lb_cao_13"))
        self.horizontalLayout_14.addWidget(self.lb_cao_13, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.le_molA = QtGui.QLineEdit(self.Reaccion)
        self.le_molA.setMinimumSize(QtCore.QSize(146, 27))
        self.le_molA.setObjectName(_fromUtf8("le_molA"))
        self.horizontalLayout_14.addWidget(self.le_molA, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.lb_cao_14 = QtGui.QLabel(self.Reaccion)
        self.lb_cao_14.setObjectName(_fromUtf8("lb_cao_14"))
        self.horizontalLayout_16.addWidget(self.lb_cao_14, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.le_molB = QtGui.QLineEdit(self.Reaccion)
        self.le_molB.setMinimumSize(QtCore.QSize(146, 27))
        self.le_molB.setObjectName(_fromUtf8("le_molB"))
        self.horizontalLayout_16.addWidget(self.le_molB, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.lb_cao_15 = QtGui.QLabel(self.Reaccion)
        self.lb_cao_15.setObjectName(_fromUtf8("lb_cao_15"))
        self.horizontalLayout_15.addWidget(self.lb_cao_15, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.le_inerte = QtGui.QLineEdit(self.Reaccion)
        self.le_inerte.setMinimumSize(QtCore.QSize(146, 27))
        self.le_inerte.setObjectName(_fromUtf8("le_inerte"))
        self.horizontalLayout_15.addWidget(self.le_inerte, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.Izquierda.addWidget(self.Reaccion)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 58))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_20 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.rb_exo = QtGui.QRadioButton(self.groupBox)
        self.rb_exo.setObjectName(_fromUtf8("rb_exo"))
        self.horizontalLayout_20.addWidget(self.rb_exo)
        self.rb_endo = QtGui.QRadioButton(self.groupBox)
        self.rb_endo.setObjectName(_fromUtf8("rb_endo"))
        self.horizontalLayout_20.addWidget(self.rb_endo)
        self.Izquierda.addWidget(self.groupBox)
        self.Parmetros_entrada = QtGui.QGroupBox(Form)
        self.Parmetros_entrada.setMinimumSize(QtCore.QSize(400, 0))
        self.Parmetros_entrada.setMaximumSize(QtCore.QSize(400, 16777215))
        self.Parmetros_entrada.setObjectName(_fromUtf8("Parmetros_entrada"))
        self.verticalLayout = QtGui.QVBoxLayout(self.Parmetros_entrada)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.lb_cao_6 = QtGui.QLabel(self.Parmetros_entrada)
        self.lb_cao_6.setObjectName(_fromUtf8("lb_cao_6"))
        self.horizontalLayout_7.addWidget(self.lb_cao_6, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.cb_orden = QtGui.QComboBox(self.Parmetros_entrada)
        self.cb_orden.setMinimumSize(QtCore.QSize(146, 27))
        self.cb_orden.setObjectName(_fromUtf8("cb_orden"))
        self.cb_orden.addItem(_fromUtf8(""))
        self.cb_orden.addItem(_fromUtf8(""))
        self.cb_orden.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.cb_orden, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.lb_cao_9 = QtGui.QLabel(self.Parmetros_entrada)
        self.lb_cao_9.setObjectName(_fromUtf8("lb_cao_9"))
        self.horizontalLayout_10.addWidget(self.lb_cao_9, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_temp_ini = QtGui.QLineEdit(self.Parmetros_entrada)
        self.le_temp_ini.setMinimumSize(QtCore.QSize(146, 27))
        self.le_temp_ini.setObjectName(_fromUtf8("le_temp_ini"))
        self.horizontalLayout_10.addWidget(self.le_temp_ini, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.lb_cao_5 = QtGui.QLabel(self.Parmetros_entrada)
        self.lb_cao_5.setObjectName(_fromUtf8("lb_cao_5"))
        self.horizontalLayout_6.addWidget(self.lb_cao_5, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_concentracion_ini = QtGui.QLineEdit(self.Parmetros_entrada)
        self.le_concentracion_ini.setObjectName(_fromUtf8("le_concentracion_ini"))
        self.horizontalLayout_6.addWidget(self.le_concentracion_ini, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lb_cao_4 = QtGui.QLabel(self.Parmetros_entrada)
        self.lb_cao_4.setObjectName(_fromUtf8("lb_cao_4"))
        self.horizontalLayout_5.addWidget(self.lb_cao_4, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_ener_act = QtGui.QLineEdit(self.Parmetros_entrada)
        self.le_ener_act.setMinimumSize(QtCore.QSize(146, 27))
        self.le_ener_act.setObjectName(_fromUtf8("le_ener_act"))
        self.horizontalLayout_5.addWidget(self.le_ener_act, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.lb_cao_7 = QtGui.QLabel(self.Parmetros_entrada)
        self.lb_cao_7.setObjectName(_fromUtf8("lb_cao_7"))
        self.horizontalLayout_8.addWidget(self.lb_cao_7, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_k = QtGui.QLineEdit(self.Parmetros_entrada)
        self.le_k.setMinimumSize(QtCore.QSize(146, 27))
        self.le_k.setObjectName(_fromUtf8("le_k"))
        self.horizontalLayout_8.addWidget(self.le_k, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.lb_cao_8 = QtGui.QLabel(self.Parmetros_entrada)
        self.lb_cao_8.setObjectName(_fromUtf8("lb_cao_8"))
        self.horizontalLayout_9.addWidget(self.lb_cao_8, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_caudal = QtGui.QLineEdit(self.Parmetros_entrada)
        self.le_caudal.setMinimumSize(QtCore.QSize(146, 27))
        self.le_caudal.setObjectName(_fromUtf8("le_caudal"))
        self.horizontalLayout_9.addWidget(self.le_caudal, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.lb_cao_11 = QtGui.QLabel(self.Parmetros_entrada)
        self.lb_cao_11.setObjectName(_fromUtf8("lb_cao_11"))
        self.horizontalLayout_18.addWidget(self.lb_cao_11, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_ah = QtGui.QLineEdit(self.Parmetros_entrada)
        self.le_ah.setMinimumSize(QtCore.QSize(146, 27))
        self.le_ah.setObjectName(_fromUtf8("le_ah"))
        self.horizontalLayout_18.addWidget(self.le_ah, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.lb_cao_16 = QtGui.QLabel(self.Parmetros_entrada)
        self.lb_cao_16.setObjectName(_fromUtf8("lb_cao_16"))
        self.horizontalLayout_19.addWidget(self.lb_cao_16, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_cp = QtGui.QLineEdit(self.Parmetros_entrada)
        self.le_cp.setMinimumSize(QtCore.QSize(146, 27))
        self.le_cp.setObjectName(_fromUtf8("le_cp"))
        self.horizontalLayout_19.addWidget(self.le_cp, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lb_cao_3 = QtGui.QLabel(self.Parmetros_entrada)
        self.lb_cao_3.setObjectName(_fromUtf8("lb_cao_3"))
        self.horizontalLayout_4.addWidget(self.lb_cao_3, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_conv_ini = QtGui.QLineEdit(self.Parmetros_entrada)
        self.le_conv_ini.setMinimumSize(QtCore.QSize(146, 27))
        self.le_conv_ini.setObjectName(_fromUtf8("le_conv_ini"))
        self.horizontalLayout_4.addWidget(self.le_conv_ini, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.lb_cao = QtGui.QLabel(self.Parmetros_entrada)
        self.lb_cao.setObjectName(_fromUtf8("lb_cao"))
        self.horizontalLayout_13.addWidget(self.lb_cao, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_conv_fin = QtGui.QLineEdit(self.Parmetros_entrada)
        self.le_conv_fin.setMinimumSize(QtCore.QSize(146, 27))
        self.le_conv_fin.setObjectName(_fromUtf8("le_conv_fin"))
        self.horizontalLayout_13.addWidget(self.le_conv_fin, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
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
        self.plotV = PlotWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotV.sizePolicy().hasHeightForWidth())
        self.plotV.setSizePolicy(sizePolicy)
        self.plotV.setMinimumSize(QtCore.QSize(685, 0))
        self.plotV.setObjectName(_fromUtf8("plotV"))
        self.verticalLayout_2.addWidget(self.plotV)
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem5)
        self.lb_cao_17 = QtGui.QLabel(Form)
        self.lb_cao_17.setObjectName(_fromUtf8("lb_cao_17"))
        self.horizontalLayout_23.addWidget(self.lb_cao_17, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.le_xa1 = QtGui.QLineEdit(Form)
        self.le_xa1.setMinimumSize(QtCore.QSize(146, 27))
        self.le_xa1.setObjectName(_fromUtf8("le_xa1"))
        self.horizontalLayout_23.addWidget(self.le_xa1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem7)
        self.lb_cao_18 = QtGui.QLabel(Form)
        self.lb_cao_18.setObjectName(_fromUtf8("lb_cao_18"))
        self.horizontalLayout_24.addWidget(self.lb_cao_18, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.le_volumen = QtGui.QLineEdit(Form)
        self.le_volumen.setMinimumSize(QtCore.QSize(146, 27))
        self.le_volumen.setObjectName(_fromUtf8("le_volumen"))
        self.horizontalLayout_24.addWidget(self.le_volumen, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_24)
        spacerItem9 = QtGui.QSpacerItem(20, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem9)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.plotT = PlotWidget(Form)
        self.plotT.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotT.sizePolicy().hasHeightForWidth())
        self.plotT.setSizePolicy(sizePolicy)
        self.plotT.setMinimumSize(QtCore.QSize(685, 0))
        self.plotT.setObjectName(_fromUtf8("plotT"))
        self.horizontalLayout_22.addWidget(self.plotT)
        self.verticalLayout_2.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.lb_cao_10 = QtGui.QLabel(Form)
        self.lb_cao_10.setObjectName(_fromUtf8("lb_cao_10"))
        self.horizontalLayout_11.addWidget(self.lb_cao_10, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.le_xa2 = QtGui.QLineEdit(Form)
        self.le_xa2.setMinimumSize(QtCore.QSize(146, 27))
        self.le_xa2.setObjectName(_fromUtf8("le_xa2"))
        self.horizontalLayout_11.addWidget(self.le_xa2, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.lb_cao_2 = QtGui.QLabel(Form)
        self.lb_cao_2.setObjectName(_fromUtf8("lb_cao_2"))
        self.horizontalLayout_3.addWidget(self.lb_cao_2, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.le_temp = QtGui.QLineEdit(Form)
        self.le_temp.setMinimumSize(QtCore.QSize(146, 27))
        self.le_temp.setObjectName(_fromUtf8("le_temp"))
        self.horizontalLayout_3.addWidget(self.le_temp, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem14 = QtGui.QSpacerItem(20, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem14)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        spacerItem15 = QtGui.QSpacerItem(80, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem15)
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
        spacerItem16 = QtGui.QSpacerItem(80, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem16)
        self.verticalLayout_5.addLayout(self.horizontalLayout_17)
        spacerItem17 = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem17)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setContentsMargins(0, 20, -1, -1)
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem18)
        self.btn_cerrar = QtGui.QPushButton(Form)
        self.btn_cerrar.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_cerrar.setMaximumSize(QtCore.QSize(100, 40))
        self.btn_cerrar.setObjectName(_fromUtf8("btn_cerrar"))
        self.horizontalLayout_21.addWidget(self.btn_cerrar)
        self.verticalLayout_5.addLayout(self.horizontalLayout_21)
        self._2.addLayout(self.verticalLayout_5)
        spacerItem19 = QtGui.QSpacerItem(12, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self._2.addItem(spacerItem19)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Reactor FP Adiabático", None))
        self.Reaccion.setTitle(_translate("Form", "Reacción", None))
        self.lb_cao_12.setText(_translate("Form", "aA ---> bR", None))
        self.lb_cao_13.setText(_translate("Form", "a [mol]", None))
        self.lb_cao_14.setText(_translate("Form", "b [mol]", None))
        self.lb_cao_15.setText(_translate("Form", "Inerte [%]", None))
        self.groupBox.setTitle(_translate("Form", "Tipo de reacción", None))
        self.rb_exo.setText(_translate("Form", "Exotérmica", None))
        self.rb_endo.setText(_translate("Form", "Endotérmica", None))
        self.Parmetros_entrada.setTitle(_translate("Form", "Parámetros de entrada", None))
        self.lb_cao_6.setText(_translate("Form", "Orden de reacción", None))
        self.cb_orden.setItemText(0, _translate("Form", "0", None))
        self.cb_orden.setItemText(1, _translate("Form", "1", None))
        self.cb_orden.setItemText(2, _translate("Form", "2", None))
        self.lb_cao_9.setText(_translate("Form", "Temperatura inicial [K]", None))
        self.lb_cao_5.setText(_translate("Form", "Concentración inicial [mol/L]", None))
        self.lb_cao_4.setText(_translate("Form", "Energía de activación [J/mol]", None))
        self.lb_cao_7.setText(_translate("Form", "Constante ko", None))
        self.lb_cao_8.setText(_translate("Form", "Caudal [L/s]", None))
        self.lb_cao_11.setText(_translate("Form", "Calor latente [J/mol]", None))
        self.lb_cao_16.setText(_translate("Form", "Calor específico [J/mol·K]", None))
        self.lb_cao_3.setText(_translate("Form", "Conversión inicial", None))
        self.lb_cao.setText(_translate("Form", "Conversión final", None))
        self.btn_reset.setText(_translate("Form", "Resetear parámetros", None))
        self.lb_cao_17.setText(_translate("Form", "Xa", None))
        self.lb_cao_18.setText(_translate("Form", "Volumen [L]", None))
        self.lb_cao_10.setText(_translate("Form", "Xa", None))
        self.lb_cao_2.setText(_translate("Form", "Temperatura [K]", None))
        self.btn_ejecutar.setText(_translate("Form", "CALCULAR", None))
        self.btn_cerrar.setText(_translate("Form", "VOLVER", None))

from pyqtgraph import PlotWidget