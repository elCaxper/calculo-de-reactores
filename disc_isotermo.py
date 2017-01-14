from __future__ import unicode_literals
import sys
from PySide import QtCore, QtGui

from ventana_disc_iso import Ui_Form
import numpy as np

import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
import matplotlib.pyplot as plt

from show_cursor import SnaptoCursor, Cursor



class Reactor_discontinuo_isotermo(QtGui.QWidget,Ui_Form):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

        self.btn_calcular.clicked.connect(self.leer)
        # self.btn_ejecutar.clicked.connect(self.leer)

        self.deltaT = 0.005
        self.R = 8.3143
        self.plot.setLabel('left', 'Conversión')
        self.plot.setLabel('bottom', 'Tiempo', units='s')

        self.btn_mostrar_resultado.clicked.connect(self.mostrar_resultado)
        self.le_xa.editingFinished.connect(self.handleEditingFinished)

    def leer(self):
        self.orden = float(self.cb_orden.currentText()[0].strip())
        self.temp_ini = float(self.le_temp_ini.text())
        self.Cao = float(self.le_concentracion_ini.text())
        self.ener_act = float(self.le_ener_act.text())
        self.k = float(self.le_k.text())
        self.conv_ini = float(self.le_conv_ini.text())
        self.conv_fin = float(self.le_conv_fin.text())

        self.K = self.k*np.exp(-self.ener_act/self.R/self.temp_ini)

        self.plotear()

    def f0(self,conv):
        return self.Cao*(conv-self.conv_ini)

    def f1(self,conv):
        return np.log((1-self.conv_ini)/(1-conv))/self.K

    def f2(self,conv):
        return np.log((conv)/(1-conv))/self.K/self.Cao

    def plotear(self):
        self.x = np.arange(self.conv_ini,self.conv_fin,self.deltaT)
        if self.orden == 0:
            f = np.vectorize(self.f0)
        elif self.orden == 1:
            f = np.vectorize(self.f1)
        else:
            f = np.vectorize(self.f2)
        self.y = f(self.x)
        print(self.K)
        self.plot.clear()
        self.plot.plot(self.y, self.x, pen=None, symbol='o')  ## setting pen=None disables line drawing

    def mostrar_resultado(self):
        # t = np.arange(0.0, 1.0, 0.01)
        # s = np.sin(2 * 2 * np.pi * t)
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim([min(self.y), max(self.y)])
        self.ax.set_ylim([min(self.x), max(self.x)])
        self.ax.set_xlabel('tiempo (s)')
        self.ax.set_ylabel('conversion')
        # cursor = Cursor(ax)
        self.cursor = SnaptoCursor(self.ax, self.y, self.x)
        plt.connect('motion_notify_event', self.cursor.mouse_move)

        self.ax.plot(self.y, self.x, 'o')

        # Hace que matlplolib controle todas las figuras con sus propios hilos de forma independiente a la gui principal
        # sustituye a la funcion plt.show()
        plt.ion()
        plt.show()

    def handleEditingFinished(self):
        if self.le_xa.isModified():
            idx = (np.abs(self.x - float(self.le_xa.text()))).argmin()
            self.le_time.setText(str(self.y[idx]/60))
        self.le_xa.setModified(False)

if __name__ == '__main__':

    try:
        app = QtGui.QApplication(sys.argv)
    except RuntimeError:
        pass

    # MainWindow = QtGui.QWidget()
    ui = Reactor_discontinuo_isotermo()
    ui.show()
    sys.exit(app.exec_())