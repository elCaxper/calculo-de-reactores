import sys
import numpy as np
import pyqtgraph as pg
from PySide import QtCore, QtGui
from ventana_MP_conversion import Ui_Form
import matplotlib as mpl

mpl.use('Qt4Agg')
mpl.rcParams['backend.qt4']='PySide'
import matplotlib.pyplot as plt
from show_cursor import SnaptoCursor, Cursor


class Reactor_mp_conversion(QtGui.QWidget, Ui_Form):

    def __init__(self):

        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.le_molA.setText('1')
        self.le_molB.setText('1')
        self.cb_orden.setCurrentIndex(2)
        self.le_temp_fin.setText('393')
        self.le_concentracion_ini.setText('6.65')
        self.le_ener_act.setText('83680')
        self.le_k.setText('55000000')
        self.le_volumen_2.setText('912')
        self.le_caudal.setText('1.26')

        self.deltaT = 0.5
        self.R = 8.3143
        self.plot.setLabel('left', 'Conversión')
        self.plot.setLabel('bottom', 'Volumen', units='L')

        self.btn_mostrar_resultados.setDisabled(True)

        self.btn_ejecutar.clicked.connect(self.ejecutar)
        self.btn_mostrar_resultados.clicked.connect(self.mostrar_resultado)
        self.btn_reset.clicked.connect(self.resetear)
        self.btn_cerrar.clicked.connect(self.close)


    def leerDatos(self):

        self.molA = float(self.le_molA.text())
        self.molB = float(self.le_molB.text())
        self.orden = int(self.cb_orden.currentText()[0].strip())
        self.temp_fin = float(self.le_temp_fin.text())
        self.cao = float(self.le_concentracion_ini.text())
        self.ener_act = float(self.le_ener_act.text())
        self.k = float(self.le_k.text())
        self.volumen = float(self.le_volumen_2.text())
        self.caudal = float(self.le_caudal.text())


    def calcularK(self):

        self.K = self.k * np.exp(-self.ener_act / (self.R * self.temp_fin))


    def f0(self, vol):
        return vol * self.K / self.caudal / self.cao


    def f1(self, vol):
        return vol * self.K / (self.caudal + self.molA * vol * self.K)


    def f2(self, vol):

        a = 1
        b = -((2 / self.molA) + (self.caudal / vol / self.K / self.cao))
        c = 1 / (self.molA ** 2)

        xf1 = (-b + ((b ** 2 - 4 * a * c)) ** 0.5) / (2 * a)
        xf2 = (-b - ((b ** 2 - 4 * a * c)) ** 0.5) / (2 * a)

        if xf1 <= 1:
            return xf1
        else:
            return xf2


    def plotear(self):

        self.x = np.arange(0.5, self.volumen+self.deltaT, self.deltaT)
        print(self.x)
        if self.orden == 0:
            f = np.vectorize(self.f0)

        elif self.orden == 1:
            f = np.vectorize(self.f1)

        else:
            f = np.vectorize(self.f2)


        self.y = f(self.x)

        self.plot.clear()
        curve = self.plot.plot(self.x, self.y, pen=None)  ## setting pen=None disables line drawing
        curve.curve.setClickable(True)
        curve.setPen('w')  ## white pen

        curve.setShadowPen(pg.mkPen((70, 70, 30), width=6, cosmetic=True))


    def resetear(self):

        self.le_molA.clear()
        self.le_molB.clear()
        self.cb_orden.setCurrentIndex(0)
        self.le_temp_fin.clear()
        self.le_concentracion_ini.clear()
        self.le_ener_act.clear()
        self.le_k.clear()
        self.le_caudal.clear()
        self.le_volumen.clear()
        self.le_volumen_2.clear()
        self.le_xa.clear()
        self.plot.clear()

        self.btn_mostrar_resultados.setDisabled(True)


    def ejecutar(self):

        if self.le_molA.text() == "" or self.le_molB.text() == "" or self.le_temp_fin.text() == "" or self.le_concentracion_ini.text() == "" or self.le_ener_act.text() == "" or self.le_k.text() == "" or self.le_caudal.text() == "" or self.le_volumen_2.text() == "":
            QtGui.QMessageBox.warning(self, "Error en la ejecución", "Alguna/s de las celdas de datos está/n vacía/s. Por favor, revise que ha introducido correctamente todos los datos.", QtGui.QMessageBox.Cancel, QtGui.QMessageBox.NoButton)
        else:
            self.leerDatos()
            self.calcularK()
            self.plotear()

            self.le_volumen.setText(str(self.volumen))

            if self.orden == 0:
                self.le_xa.setText(str(float("{0:.2f}".format(self.f0(self.volumen)))))

            elif self.orden == 1:
                self.le_xa.setText(str(float("{0:.2f}".format(self.f1(self.volumen)))))

            else:
                self.le_xa.setText(str(float("{0:.2f}".format(self.f2(self.volumen)))))

        self.btn_mostrar_resultados.setEnabled(True)


    def mostrar_resultado(self):

        self.fig, self.conv = plt.subplots()

        self.conv.set_title('RESULTADO')

        self.conv.set_xlim([min(self.x), max(self.x)])
        self.conv.set_ylim([min(self.y), max(self.y)])

        self.conv.set_xlabel('Volumen (L)')
        self.conv.set_ylabel('Conversión')

        # cursor = Cursor(ax)
        self.cursor = SnaptoCursor(self.conv, self.x, self.y)
        plt.connect('motion_notify_event', self.cursor.mouse_move)

        self.conv.plot(self.x, self.y, linewidth = 2)

        # Hace que matlplolib controle todas las figuras con sus propios hilos de forma independiente a la gui principal
        # sustituye a la funcion plt.show()
        plt.ion()
        plt.show()


try:
    app = QtGui.QApplication(sys.argv)
except RuntimeError:
    pass


# MainWindow = QtGui.QWidget()
ui = Reactor_mp_conversion()
# ui.setupUi(MainWindow)
ui.show()
app.exec_()
