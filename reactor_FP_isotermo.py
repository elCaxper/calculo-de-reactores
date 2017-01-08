import sys
from PySide import QtCore, QtGui
from ventana_FP_isotermo import Ui_Form
import numpy as np
import pyqtgraph as pg


class Reactor_FP_isotermo(QtGui.QWidget,Ui_Form):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

        self.le_molA.setText('1')
        self.le_molB.setText('3')
        self.le_inerte.setText('50')
        self.cb_orden.setCurrentIndex(2)
        self.le_temp_ini.setText('623')
        self.le_concentracion_ini.setText('0.245')
        self.le_ener_act.setText('41572')
        self.le_k.setText('173315.4')
        self.le_caudal.setText('88.89')
        self.le_conv_ini.setText('0')
        self.le_conv_fin.setText('0.8')

        self.deltaT = 0.005
        self.R = 8.3143
        self.plot.setLabel('left', 'Conversión')
        self.plot.setLabel('bottom', 'Volumen', units='L')

        self.btn_ejecutar.clicked.connect(self.ejecutar)
        self.btn_reset.clicked.connect(self.resetear)
        self.btn_cerrar.clicked.connect(self.close)


    def leerDatos(self):

        self.molA = float(self.le_molA.text())
        self.molB = float(self.le_molB.text())
        self.inerte = float(self.le_inerte.text())
        self.orden = int(self.cb_orden.currentText()[0].strip())
        self.temp_ini = float(self.le_temp_ini.text())
        self.cao = float(self.le_concentracion_ini.text())
        self.ener_act = float(self.le_ener_act.text())
        self.k = float(self.le_k.text())
        self.caudal = float(self.le_caudal.text())
        self.conv_ini = float(self.le_conv_ini.text())
        self.conv_fin = float(self.le_conv_fin.text())


    def calcularFactorExpansion(self):

        if (self.inerte != 0):
            self.reactivos = self.molA + 1
            self.productos = self.molB + 1
        else:
            self.reactivos = self.molA
            self.productos = self.molB

        if (self.reactivos >= self.productos):
            self.factor_exp = (self.reactivos - self.productos)/self.productos
        else:
            self.factor_exp = (self.productos - self.reactivos) / self.reactivos


    def calcularK(self):

        self.K = self.k * np.exp(-self.ener_act / (self.R * self.temp_ini))


    def f0(self, conv):
        return self.cao * self.caudal * (conv - self.conv_ini) / self.K


    def f1(self, conv):
        return self.caudal * (((self.molA+self.factor_exp) / self.molA ** 2)*(np.log(np.abs(1 - self.molA * self.conv_ini))-np.log(np.abs(1 - self.molA * conv))) - (self.factor_exp / self.molA) *(conv-self.conv_ini)) / self.K


    def f2(self, conv):
        return self.caudal * ((self.factor_exp ** 2 / self.molA ** 2) * (conv-self.conv_ini) - (((self.molA + self.factor_exp) ** 2) / self.molA ** 3) * ((1 / (self.molA * conv - 1)) - (1 / (self.molA * self.conv_ini - 1))) + ((2 * self.factor_exp * (self.molA + self.factor_exp)) / self.molA ** 3 ) * (np.log(np.abs(1 - self.molA * conv)) - np.log(np.abs(1 - self.molA * self.conv_ini)))) / (self.cao*self.K)


    def plotear(self):

        x = np.arange(0.01, self.conv_fin, self.deltaT)

        if self.orden == 0:
            f = np.vectorize(self.f0)

        elif self.orden == 1:
            f = np.vectorize(self.f1)

        else:
            f = np.vectorize(self.f2)

        y = f(x)
        self.plot.clear()

        curve = self.plot.plot(y, x, pen=None)  ## setting pen=None disables line drawing
        curve.curve.setClickable(True)
        curve.setPen('w')  ## white pen

        curve.setShadowPen(pg.mkPen((70, 70, 30), width=6, cosmetic=True))

    def resetear(self):

        self.le_molA.clear()
        self.le_molB.clear()
        self.le_inerte.clear()
        self.cb_orden.setCurrentIndex(0)
        self.le_temp_ini.clear()
        self.le_concentracion_ini.clear()
        self.le_ener_act.clear()
        self.le_k.clear()
        self.le_caudal.clear()
        self.le_conv_ini.clear()
        self.le_conv_fin.clear()
        self.le_volumen.clear()
        self.le_xa.clear()
        self.plot.clear()

    def ejecutar(self):

        if self.le_molA.text() == "" or self.le_molB.text() == "" or self.le_inerte.text() == "" or self.le_temp_ini.text() == "" or self.le_concentracion_ini.text() == "" or self.le_ener_act.text() == "" or self.le_k.text() == "" or self.le_caudal.text() == "" or self.le_conv_ini.text() == "" or self.le_conv_fin.text() == "":
            QtGui.QMessageBox.warning(self, "Error en la ejecución", "Alguna/s de las celdas de datos está/n vacía/s. Por favor, revise que ha introducido correctamente todos los datos.", QtGui.QMessageBox.Cancel, QtGui.QMessageBox.NoButton)
        else:
            self.leerDatos()
            self.calcularFactorExpansion()
            self.calcularK()
            self.plotear()

            self.le_xa.setText(str(self.conv_fin))

            if self.orden == 0:
                self.le_volumen.setText(str(float("{0:.2f}".format(self.f0(self.conv_fin)))))

            elif self.orden == 1:
                self.le_volumen.setText(str(float("{0:.2f}".format(self.f1(self.conv_fin)))))

            else:
                self.le_volumen.setText(str(float("{0:.2f}".format(self.f2(self.conv_fin)))))


if __name__ == '__main__':
    try:
        app = QtGui.QApplication(sys.argv)
    except RuntimeError:
        pass


    # MainWindow = QtGui.QWidget()
    ui = Reactor_FP_isotermo()
    # ui.setupUi(MainWindow)
    ui.show()
    app.exec_()
