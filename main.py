import os
import sys
from PySide import QtCore, QtGui
from ventana_principal import Ventana_principal
from ventana_seleccion import Ventana_seleccion
from PySide.QtGui import QMainWindow, QApplication, QLabel, QPixmap

from disc_isotermo import Reactor_discontinuo_isotermo
from discontinuo_adiabatico import Reactor_discontinuo_adiabatico
from dis_no_adi_no_isot import Reactor_disc_no_adi_no_iso
from condiciones_optimas import Reac_dis_cond_optimas

from reactor_FP_isotermo import Reactor_FP_isotermo
from reactor_FP_adiabatico import Reactor_FP_adiabatico
from reactor_FP_general import Reactor_FP_general
from reactor_MP_conversion import Reactor_mp_conversion
from reactor_MP_volumen import Reactor_mp_volumen

from visor_ayuda import Visor_documentacion
import numpy as np
import pyqtgraph as pg

class Seleccionar_reactor(QtGui.QWidget, Ventana_seleccion):
    def __init__(self,parent):
        self.parent = parent
        QtGui.QWidget.__init__(self, None)
        self.setupUi(self)
        self.center()

        self.btn_dis_iso.clicked.connect(self.ejecutar_dis_iso)
        self.btn_dis_adi.clicked.connect(self.ejecutar_dis_adi)
        self.btn_dis_no_iso_no_adi.clicked.connect(self.ejecutar_dis_no_iso_no_adi)
        self.btn_dis_con.clicked.connect(self.ejecutar_dis_con)

        self.btn_con_iso.clicked.connect(self.ejecutar_con_iso)
        self.btn_con_adi.clicked.connect(self.ejecutar_con_adi)
        self.btn_con_no_iso_no_adi.clicked.connect(self.ejecutar_con_no_iso_no_adi)

        self.btn_fijo_conv.clicked.connect(self.ejecutar_fijo_con)
        self.btn_fijo_vol.clicked.connect(self.ejecutar_fijo_vol)


        self.btn_salir.clicked.connect(self.close)

        self.reac_dis_iso = None
        self.reac_dis_adi = None
        self.reac_dis_no_iso_no_adi = None
        self.reac_dis_cond = None

        self.reac_con_iso = None
        self.reac_con_adi = None
        self.reac_con_no_iso_no_adi = None

        self.reac_fijo_con = None
        self.reac_fijo_vol = None

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        self.parent.show()

    def ejecutar_dis_iso(self):
        if self.reac_dis_iso == None:
            self.reac_dis_iso = Reactor_discontinuo_isotermo()
        self.reac_dis_iso.show()

    def ejecutar_dis_adi(self):
        if self.reac_dis_adi == None:
            self.reac_dis_adi = Reactor_discontinuo_adiabatico()
        self.reac_dis_adi.show()

    def ejecutar_dis_no_iso_no_adi(self):
        if self.reac_dis_no_iso_no_adi == None:
            self.reac_dis_no_iso_no_adi = Reactor_disc_no_adi_no_iso()
        self.reac_dis_no_iso_no_adi.show()

    def ejecutar_dis_con(self):
        if self.reac_dis_cond == None:
            self.reac_dis_cond = Reac_dis_cond_optimas()
        self.reac_dis_cond.show()

    def ejecutar_con_iso(self):
        if self.reac_con_iso == None:
            self.reac_con_iso = Reactor_FP_isotermo()
        self.reac_con_iso.show()

    def ejecutar_con_adi(self):
        if self.reac_con_adi == None:
            self.reac_con_adi = Reactor_FP_adiabatico()
        self.reac_con_adi.show()

    def ejecutar_con_no_iso_no_adi(self):
        if self.reac_con_no_iso_no_adi == None:
            self.reac_con_no_iso_no_adi = Reactor_FP_general()
        self.reac_con_no_iso_no_adi.show()

    def ejecutar_fijo_con(self):
        if self.reac_fijo_con == None:
            self.reac_fijo_con = Reactor_mp_conversion()
        self.reac_fijo_con.show()

    def ejecutar_fijo_vol(self):
        if self.reac_fijo_vol == None:
            self.reac_fijo_vol = Reactor_mp_volumen()
        self.reac_fijo_vol.show()


class Crear_programa(QMainWindow, Ventana_principal):
    def __init__(self):
        super(Crear_programa, self).__init__(None)
        self.setupUi(self)

        fn = os.path.join(os.path.dirname(__file__), 'imagenes')

        logo_etsii = QtGui.QPixmap(fn+"/LogoETSII.png")
        logo_uclm = QtGui.QPixmap(fn+"/logouclm_NUEVO.png")
        self.lb_foto_2.setPixmap(QtGui.QPixmap(logo_etsii))
        self.lb_foto_1.setPixmap(QtGui.QPixmap(logo_uclm))

        x, y, w, h = 50, 50, 100, 100
        self.lb_foto_2.setGeometry(x, y, w, h)
        # self.lb_foto_2.resize(w, h)
        self.lb_foto_2.setScaledContents(True)
        self.lb_foto_1.setScaledContents(True)
        self.lb_foto_2.resize(0.1 * self.lb_foto_2.pixmap().size())
        self.lb_foto_1.resize(0.1 * self.lb_foto_2.pixmap().size())

        self.btn_salir.clicked.connect(self.close)

        self.btn_empezar.clicked.connect(self.empezar)

        self.mostrar_guia.clicked.connect(self.mostrar_ayuda)

        self.visor_ayuda =None


        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



    def empezar(self):
        self.pantalla_seleccion = Seleccionar_reactor(self)
        # pantalla_seleccion.setupUi(self)
        self.pantalla_seleccion.show()
        # self.wid = QtGui.QWidget()
        # self.wid.resize(250, 150)
        # self.wid.setWindowTitle('NewWindow')
        self.hide()


        print("HOLA")


    def closeEvent(self, event):
        print("event")
        box = QtGui.QMessageBox()
        box.setIcon(QtGui.QMessageBox.Question)
        box.setWindowTitle('Salir!')
        box.setText('Quieres salir de la aplicación?')
        box.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        buttonY = box.button(QtGui.QMessageBox.Yes)
        buttonY.setText('Si')
        buttonN = box.button(QtGui.QMessageBox.No)
        buttonN.setText('No')
        box.exec_()

        if  box.clickedButton()== buttonY:
            event.accept()
        else:
            event.ignore()

    def mostrar_ayuda(self):
        print("Mostrando ayuda")
        if self.visor_ayuda == None:
            self.visor_ayuda = Visor_documentacion()
        self.visor_ayuda.show()


if __name__ == '__main__':
    try:
        app = QtGui.QApplication(sys.argv)
    except RuntimeError:
        pass

    # MainWindow = QtGui.QWidget()
    ui = Crear_programa()
    # ui.setupUi(MainWindow)
    ui.show()
    app.exec_()

