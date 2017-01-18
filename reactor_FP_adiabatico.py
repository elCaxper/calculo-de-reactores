import sys
import numpy as np
import pyqtgraph as pg
import scipy.integrate as integrate
from PySide import QtCore, QtGui
from ventana_FP_adiabatico import Ui_Form
import matplotlib as mpl

mpl.use('Qt4Agg')
mpl.rcParams['backend.qt4']='PySide'
import matplotlib.pyplot as plt
from show_cursor import SnaptoCursor, Cursor

class Reactor_FP_adiabatico(QtGui.QWidget, Ui_Form):

    def __init__(self):

        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.le_molA.setText('1')
        self.le_molB.setText('1')
        self.le_inerte.setText('0')
        self.rb_exo.setChecked(True)
        self.cb_orden.setCurrentIndex(1)
        self.le_temp_ini.setText('303')
        self.le_concentracion_ini.setText('0.402')
        self.le_ener_act.setText('99773.66')
        self.le_k.setText('2.78E12')
        self.le_caudal.setText('0.2764')
        self.le_ah.setText('50208')
        self.le_cp.setText('334.94')
        self.le_conv_ini.setText('0')
        self.le_conv_fin.setText('0.5')

        self.deltaT = 0.005
        self.R = 8.3143

        self.plotV.setLabel('left', 'Conversión')
        self.plotV.setLabel('bottom', 'Volumen', units='L')
        self.plotT.setLabel('left', 'Temperatura', units='K')
        self.plotT.setLabel('bottom', 'Conversión')

        self.btn_mostrar_resultados.setDisabled(True)

        self.btn_ejecutar.clicked.connect(self.ejecutar)
        self.btn_mostrar_resultados.clicked.connect(self.mostrar_resultado)
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

        if (self.rb_exo.isChecked()):
            self.ah = float(self.le_ah.text())
        else:
            self.ah = -float(self.le_ah.text())

        self.cp = float(self.le_cp.text())
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


    def f0(self, conv):

        T = lambda xa: self.temp_ini + (self.ah * (xa - self.conv_ini) / self.cp)

        K = lambda conv: self.k * np.exp(-self.ener_act / (self.R * T(conv)))

        Ca = lambda conv: self.cao * ((1 - self.molA * conv) / (1 + self.factor_exp * conv))

        integral = lambda conv: (self.caudal * self.cao) / ((self.k * np.exp(-self.ener_act / (self.R * (self.temp_ini + (self.ah * (conv - self.conv_ini) / self.cp)))))*(self.cao * ((1 - self.molA * conv) / (1 + self.factor_exp * conv)))**self.orden)

        resultado = integrate.quad(integral, self.conv_ini, conv)
        temp = T(conv)

        return resultado[0], temp


    def plotear(self):

        self.x = np.arange(0.05, self.conv_fin+self.deltaT, self.deltaT)

        f = np.vectorize(self.f0)

        self.y = f(self.x)

        self.plotV.clear()
        self.plotT.clear()

        curveV = self.plotV.plot(self.y[0], self.x, pen=None)  ## setting pen=None disables line drawing
        curveV.curve.setClickable(True)
        curveV.setPen('w')  ## white pen
        curveV.setShadowPen(pg.mkPen((70, 70, 30), width=6, cosmetic=True))

        curveT = self.plotT.plot(self.x, self.y[1], pen=None)  ## setting pen=None disables line drawing
        curveT.curve.setClickable(True)
        curveT.setPen('w')  ## white pen
        curveT.setShadowPen(pg.mkPen((70, 70, 30), width=6, cosmetic=True))


    def resetear(self):

        self.le_molA.clear()
        self.le_molB.clear()
        self.le_inerte.clear()
        self.rb_exo.setChecked(True)
        self.cb_orden.setCurrentIndex(0)
        self.le_temp_ini.clear()
        self.le_concentracion_ini.clear()
        self.le_ener_act.clear()
        self.le_k.clear()
        self.le_caudal.clear()
        self.le_ah.clear()
        self.le_cp.clear()
        self.le_conv_ini.clear()
        self.le_conv_fin.clear()
        self.le_volumen.clear()
        self.le_temperatura.clear()
        self.le_xa1.clear()
        self.le_xa2.clear()
        self.plotV.clear()
        self.plotT.clear()

        self.btn_mostrar_resultados.setDisabled(True)


    def ejecutar(self):

        if self.le_molA.text() == "" or self.le_molB.text() == "" or self.le_inerte.text() == "" or self.le_temp_ini.text() == "" or self.le_concentracion_ini.text() == "" or self.le_ener_act.text() == "" or self.le_k.text() == "" or self.le_caudal.text() == "" or self.le_ah.text() == "" or self.le_cp.text() == "" or self.le_conv_ini.text() == "" or self.le_conv_fin.text() == "":
            QtGui.QMessageBox.warning(self, "Error en la ejecución", "Alguna/s de las celdas de datos está/n vacía/s. Por favor, revise que ha introducido correctamente todos los datos.", QtGui.QMessageBox.Cancel, QtGui.QMessageBox.NoButton)
        else:
            self.leerDatos()
            self.calcularFactorExpansion()
            self.plotear()

            self.le_xa1.setText(str(self.conv_fin))
            self.le_xa2.setText(str(self.conv_fin))
            self.le_volumen.setText(str(float("{0:.2f}".format(self.f0(self.conv_fin)[0]))))
            self.le_temperatura.setText(str(float("{0:.2f}".format(self.f0(self.conv_fin)[1]))))

            self.btn_mostrar_resultados.setEnabled(True)


    def mostrar_resultado(self):

        self.fig, (self.vol, self.temp) = plt.subplots(2, 1)

        self.vol.set_title('RESULTADO')

        self.vol.set_xlim([min(self.y[0]), max(self.y[0])])
        self.vol.set_ylim([min(self.x), max(self.x)])
        self.vol.set_xlabel('Volumen (L)')
        self.vol.set_ylabel('Conversión')

        # cursor = Cursor(ax)

        self.cursor1 = SnaptoCursor(self.vol, self.y[0], self.x)
        plt.connect('motion_notify_event', self.cursor1.mouse_move)

        self.vol.plot(self.y[0], self.x, linewidth=2)


        self.temp.set_ylim([min(self.y[1]), max(self.y[1])])
        self.temp.set_xlabel('Conversión')
        self.temp.set_ylabel('Temperatura (K)')

        self.cursor2 = SnaptoCursor(self.temp, self.x, self.y[1])
        plt.connect('motion_notify_event', self.cursor2.mouse_move)



        self.temp.plot(self.x, self.y[1], linewidth = 2)

        # Hace que matlplolib controle todas las figuras con sus propios hilos de forma independiente a la gui principal
        # sustituye a la funcion plt.show()
        plt.ion()
        plt.show()


if __name__ == '__main__':

    try:
        app = QtGui.QApplication(sys.argv)
    except RuntimeError:
        pass


    # MainWindow = QtGui.QWidget()
    ui = Reactor_FP_adiabatico()
    # ui.setupUi(MainWindow)
    ui.show()
    app.exec_()
