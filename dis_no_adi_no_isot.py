import sys
from PySide import QtCore, QtGui
from ventana_disc_no_iso_no_adi import Ventana_dis_no_iso_no_adi
import numpy as np
import scipy.integrate as integrate
import pyqtgraph as pg
import pyqtgraph as pg
from scipy.integrate import odeint
from numpy import arange

import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
import matplotlib.pyplot as plt

from show_cursor import SnaptoCursor, Cursor


class Reactor_disc_no_adi_no_iso(QtGui.QWidget,Ventana_dis_no_iso_no_adi):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

        self.btn_calcular.clicked.connect(self.leer)
        self.btn_mostrar_resultado.clicked.connect(self.mostrar_resultado)
        self.le_xa.editingFinished.connect(self.handleEditingFinished)

        self.deltaT = 0.001
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

        self.coef_transmision = float(self.le_coef_transmision.text())
        self.area = float(self.le_area.text())
        self.volumen = float(self.le_volumen.text())
        self.temp_inter = float(self.le_temp_int.text())


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

    def sistema(self,state,x):
        y1, y2 = state

        dy1 = self.Cao / (self.k * np.exp(-self.ener_act / (self.R * y2)) * (self.Cao ** self.orden) * ((1 - x) ** self.orden))

        # dy2 = (signo*calor_reaccion*Cao*peso_molar)/(densidad*calor_especifico)+(coef_transmision*area*(temp_inter-temp))/\
        #         (volumen*densidad*calor_especifico*k*np.exp(-ener_act/(R*temp))*(Cao**orden)*((1-x)**orden))
        dy2 = ((self.Cao * self.peso_molecular) / (self.densidad * self.calor_especifico)) * (
        (self.signo * self.calor_reaccion) + (self.coef_transmision * self.area * (self.temp_inter - y2)) / \
        (self.volumen * self.k * np.exp(-self.ener_act / (self.R * y2)) * (self.Cao ** self.orden) * ((1 - x) ** self.orden)))

        return [dy1, dy2]


    def plotear(self):
        self.x = np.arange(self.conv_ini,self.conv_fin,self.deltaT)
        # curve = self.plot.plot(x[:], x[:], pen=None)  ## setting pen=None disables line drawing

        # f = np.vectorize(self.sistema)
        init_state = [0, self.temp_ini]
        self.state = odeint(self.sistema, init_state, self.x)

        print("tiempo max",np.max(self.state[:,0]))
        print("constante k0", self.k)

        # y = f(x)
        print(self.K)
        self.plot.clear()

        curve = self.plot.plot(self.state[:,0],self.x[:], pen=None)  ## setting pen=None disables line drawing
        curve.curve.setClickable(True)
        curve.setPen('w')  ## white pen
        curve.setShadowPen(pg.mkPen((70, 70, 30), width=6, cosmetic=True))

    def mostrar_resultado(self):
        # t = np.arange(0.0, 1.0, 0.01)
        # s = np.sin(2 * 2 * np.pi * t)
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, sharex=True)
        self.ax1.set_xlim([min(self.state[:,0])-0.1, max(self.state[:,0])])
        self.ax1.set_ylim([min(self.x[:]-0.1), max(self.x[:])])

        self.ax1.set_ylabel('conversion')
        # cursor = Cursor(ax)
        self.cursor = SnaptoCursor(self.ax1, self.state[:,0],self.x[:])
        plt.connect('motion_notify_event', self.cursor.mouse_move)

        # self.ax2.set_xlim([min(self.state[:, 0])-5, max(self.state[:, 0])])
        self.ax2.set_ylim([min(self.state[:, 1]), max(self.state[:, 1])+10])
        self.ax2.set_ylabel('temperatura (K)')
        self.ax2.set_xlabel('tiempo (s)')

        self.cursor2 = SnaptoCursor(self.ax2, self.state[:, 0], self.state[:, 1])
        plt.connect('motion_notify_event', self.cursor2.mouse_move)

        self.ax1.plot(self.state[:,0],self.x[:], '-')
        self.ax2.plot(self.state[:, 0], self.state[:, 1], '-')

        # Hace que matlplolib controle todas las figuras con sus propios hilos de forma independiente a la gui principal
        # sustituye a la funcion plt.show()
        plt.ion()
        plt.show()

    def handleEditingFinished(self):
        if self.le_xa.isModified():
            idx = (np.abs(self.x - float(self.le_xa.text()))).argmin()
            self.le_time.setText(str(self.state[idx, 0]/60))
            self.le_temp_b.setText(str(self.state[idx, 1]))
        self.le_xa.setModified(False)


if __name__ == '__main__':
    try:
        app = QtGui.QApplication(sys.argv)
    except RuntimeError:
        pass

    # MainWindow = QtGui.QWidget()
    ui = Reactor_disc_no_adi_no_iso()
    # ui.setupUi(MainWindow)
    ui.show()
    app.exec_()