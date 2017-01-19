import sys
from PySide import QtCore, QtGui
from ventana_disc_adiabatico import Ui_Form
import numpy as np
import scipy.integrate as integrate
import pyqtgraph as pg
import pyqtgraph as pg
import matplotlib

matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
import matplotlib.pyplot as plt

from show_cursor import SnaptoCursor, Cursor


class Reactor_discontinuo_adiabatico(QtGui.QWidget,Ui_Form):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

        self.btn_calcular.clicked.connect(self.leer)
        # self.btn_ejecutar.clicked.connect(self.leer)
        self.btn_mostrar_resultado.clicked.connect(self.mostrar_resultado)
        self.le_xa.editingFinished.connect(self.handleEditingFinished)


        self.deltaT = 0.005
        self.R = 8.3143
        self.plot.setLabel('left', 'Conversión')
        self.plot.setLabel('bottom', 'Tiempo', units='s')

    def leer(self):
        self.orden = float(self.cb_orden.currentText()[0].strip())
        self.temp_ini = float(self.le_temp_ini.text())
        self.Cao = float(self.le_concentracion_ini.text())
        self.ener_act = float(self.le_ener_act.text())
        self.k = float(self.le_k.text())
        self.calor_reaccion = float(self.le_calor_reaccion.text())
        self.peso_molecular = float(self.le_peso_molecular.text())
        self.calor_especifico = float(self.le_calor_especifico.text())
        self.densidad = float(self.le_densidad.text())

        self.conv_ini = float(self.le_conv_ini.text())
        self.conv_fin = float(self.le_conv_fin.text())

        self.K = self.k*np.exp(-self.ener_act/self.R/self.temp_ini)
        # self.Nao = self.Cao*self.V

        if self.rb_endo.isChecked():
            self.signo = -1
        elif self.rb_exo.isChecked():
            self.signo = 1
        else:
            self.signo = 1



        self.plotear()

    def f0(self,conv):

        T = lambda xa: self.temp_ini + (self.signo * self.calor_reaccion * self.Cao * (conv - self.conv_ini)) / (
            self.densidad * self.calor_especifico)

        K = lambda conv: self.k * np.exp(-self.ener_act / self.R / T(conv))

        ra = K(conv)*self.Cao**self.orden*(1-conv)**self.orden

        integral = lambda a: self.Cao/ra

        temp = T(conv)

        res = integrate.quad(integral, self.conv_ini, conv)

        return res[0],temp


    def plotear(self):
        self.x = np.arange(self.conv_ini,self.conv_fin,self.deltaT)

        f = np.vectorize(self.f0)

        self.y = f(self.x)
        print(self.K)
        self.plot.clear()

        curve = self.plot.plot(self.y[0], self.x, pen=None)  ## setting pen=None disables line drawing
        curve.curve.setClickable(True)
        curve.setPen('w')  ## white pen
        curve.setShadowPen(pg.mkPen((70, 70, 30), width=6, cosmetic=True))

    def mostrar_resultado(self):
        # t = np.arange(0.0, 1.0, 0.01)
        # s = np.sin(2 * 2 * np.pi * t)
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, sharex=True)
        self.ax1.set_xlim([min(self.y[0]), max(self.y[0])])
        self.ax1.set_ylim([min(self.x), max(self.x)])
        self.ax1.set_ylabel('conversion')
        # cursor = Cursor(ax)
        self.cursor = SnaptoCursor(self.ax1, self.y[0], self.x)
        plt.connect('motion_notify_event', self.cursor.mouse_move)

        self.ax2.set_xlim([min(self.y[0]), max(self.y[0])])
        self.ax2.set_ylim([min(self.y[1]), max(self.y[1])])
        self.ax2.set_xlabel('tiempo (s)')
        self.ax2.set_ylabel('temperatura')

        self.cursor2 = SnaptoCursor(self.ax2, self.y[0], self.y[1])
        plt.connect('motion_notify_event', self.cursor2.mouse_move)


        self.ax1.plot(self.y[0], self.x, '-')
        self.ax2.plot(self.y[0], self.y[1], '-')

        # Hace que matlplolib controle todas las figuras con sus propios hilos de forma independiente a la gui principal
        # sustituye a la funcion plt.show()
        plt.ion()
        plt.show()

    def handleEditingFinished(self):
        if self.le_xa.isModified():
            idx = (np.abs(self.x - float(self.le_xa.text()))).argmin()
            self.le_time.setText(str(self.y[0][idx]/60))
        self.le_xa.setModified(False)


if __name__ == '__main__':

    try:
        app = QtGui.QApplication(sys.argv)
    except RuntimeError:
        pass

    # MainWindow = QtGui.QWidget()
    ui = Reactor_discontinuo_adiabatico()
    # ui.setupUi(MainWindow)
    ui.show()
    app.exec_()