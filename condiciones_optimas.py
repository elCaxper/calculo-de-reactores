import sys
from PySide import QtCore, QtGui
from ventana_optimizacion import Optimizacion
import numpy as np
import scipy.integrate as integrate
import pyqtgraph as pg
import pyqtgraph as pg
from scipy.integrate import odeint
from numpy import arange

class Reac_dis_cond_optimas(QtGui.QWidget,Optimizacion):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

        self.btn_calcular.clicked.connect(self.leer)
        # self.btn_ejecutar.clicked.connect(self.leer)

        self.deltaT = 0.005
        self.R = 8.3143


    def leer(self):
        self.orden = float(self.cb_orden.currentText()[0].strip())
        self.a = float(self.le_a.text())
        self.temp_ini = float(self.le_temp_ini.text())
        self.Cao = float(self.le_concentracion_ini.text())
        self.ener_act = float(self.le_ener_act.text())
        self.k = float(self.le_k.text())
        self.volumen = float(self.le_volumen.text())
        self.coste_reac = float(self.le_coste_reac.text())
        self.aumento_valor = float(self.le_aumento_valor.text())

        self.R = 8.3143
        self.K = self.k * np.exp(-self.ener_act / self.R / self.temp_ini)

        self.calcular()


    def calcular(self):

        self.x_optimo  = 1 - ((self.coste_reac*self.a)/(self.aumento_valor*(self.Cao**self.orden)*self.volumen*self.K))**(1./self.orden)

        if self.orden==1:
            self.t_optimo = (1 / self.K) * np.log(
                (self.aumento_valor * self.Cao * self.volumen * self.K) / (self.coste_reac * self.a))
        else:
            print("orden2")
            self.t_optimo = (1/(self.K*self.Cao))*(self.x_optimo/(1-self.x_optimo))

        print(self.x_optimo)
        print(self.t_optimo)
        self.le_conv_optima.setText(format(self.x_optimo*100, '.4f'))
        self.le_tiempo_optimo.setText(format(self.t_optimo, '.4f'))

if __name__ == '__main__':

    try:
        app = QtGui.QApplication(sys.argv)
    except RuntimeError:
        pass

    # MainWindow = QtGui.QWidget()
    ui = Reac_dis_cond_optimas()
    # ui.setupUi(MainWindow)
    ui.show()
    app.exec_()