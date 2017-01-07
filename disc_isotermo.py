import sys
from PySide import QtCore, QtGui
from ventana_disc_iso import Ui_Form
import numpy as np
import pyqtgraph as pg


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
        x = np.arange(self.conv_ini,self.conv_fin,self.deltaT)
        if self.orden == 0:
            f = np.vectorize(self.f0)
        elif self.orden == 1:
            f = np.vectorize(self.f1)
        else:
            f = np.vectorize(self.f2)
        y = f(x)
        print(self.K)
        self.plot.clear()
        self.plot.plot(y, x, pen=None, symbol='o')  ## setting pen=None disables line drawing


if __name__ == '__main__':

    try:
        app = QtGui.QApplication(sys.argv)
    except RuntimeError:
        pass

    # MainWindow = QtGui.QWidget()
    ui = Reactor_discontinuo_isotermo()
    # ui.setupUi(MainWindow)
    ui.show()
    app.exec_()