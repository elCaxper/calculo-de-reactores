
import sys
from PySide import QtCore, QtGui
from ventana_principal import Ventana_principal
from ventana_seleccion import Ventana_seleccion
from PySide.QtGui import QMainWindow, QApplication, QLabel, QPixmap


import numpy as np
import pyqtgraph as pg

class Seleccionar_reactor(QtGui.QWidget, Ventana_seleccion):
    def __init__(self):
        QtGui.QWidget.__init__(self, None)
        self.setupUi(self)


class Crear_programa(QMainWindow, Ventana_principal):
    def __init__(self):
        super(Crear_programa, self).__init__(None)
        self.setupUi(self)

        logo_etsii = QtGui.QPixmap("./imagenes/LogoETSII.png")
        logo_uclm = QtGui.QPixmap("./imagenes/logouclm_NUEVO.png")
        self.lb_foto_2.setPixmap(QtGui.QPixmap(logo_etsii))
        self.lb_foto_1.setPixmap(QtGui.QPixmap(logo_uclm))

        x, y, w, h = 50, 50, 100, 100
        self.lb_foto_2.setGeometry(x, y, w, h)
        # self.lb_foto_2.resize(w, h)
        self.lb_foto_2.setScaledContents(True)
        self.lb_foto_1.setScaledContents(True)
        self.lb_foto_2.resize(0.1 * self.lb_foto_2.pixmap().size())
        self.lb_foto_1.resize(0.1 * self.lb_foto_2.pixmap().size())

        self.btn_salir.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.btn_empezar.clicked.connect(self.empezar)

    def empezar(self):
        self.pantalla_seleccion = Seleccionar_reactor()
        # pantalla_seleccion.setupUi(self)
        self.pantalla_seleccion.show()
        # self.wid = QtGui.QWidget()
        # self.wid.resize(250, 150)
        # self.wid.setWindowTitle('NewWindow')
        # self.wid.show()

        print("HOLA")


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

