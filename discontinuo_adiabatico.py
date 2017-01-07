import sys
from PySide import QtCore, QtGui
from ventana_disc_adiabatico import Ui_Form
import numpy as np
import scipy.integrate as integrate
import pyqtgraph as pg
import pyqtgraph as pg


class Reactor_discontinuo_adiabatico(QtGui.QWidget,Ui_Form):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

        self.btn_calcular.clicked.connect(self.leer)
        # self.btn_ejecutar.clicked.connect(self.leer)

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

        res = integrate.quad(integral, self.conv_ini, conv)

        return res[0]


    def plotear(self):
        x = np.arange(self.conv_ini,self.conv_fin,self.deltaT)

        f = np.vectorize(self.f0)

        y = f(x)
        print(self.K)
        self.plot.clear()

        curve = self.plot.plot(y, x, pen=None)  ## setting pen=None disables line drawing
        curve.curve.setClickable(True)
        curve.setPen('w')  ## white pen
        curve.setShadowPen(pg.mkPen((70, 70, 30), width=6, cosmetic=True))


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