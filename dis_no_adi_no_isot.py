import sys
from PySide import QtCore, QtGui
from ventana_disc_no_iso_no_adi import Ventana_dis_no_iso_no_adi
import numpy as np
import scipy.integrate as integrate
import pyqtgraph as pg
import pyqtgraph as pg
from scipy.integrate import odeint
from numpy import arange

class Reactor_disc_no_adi_no_iso(QtGui.QWidget,Ventana_dis_no_iso_no_adi):
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

        dy1 = (self.Cao/(self.k*np.exp(-self.ener_act/self.R/y2)*np.power(self.Cao, self.orden)*np.power((1-x), self.orden)))
        dy2 = ((self.signo*self.calor_reaccion*self.Cao)/(self.densidad*self.calor_especifico))\
              +((self.Cao*self.coef_transmision*self.area*(self.temp_inter-y2))
                /(self.volumen*self.densidad*self.k*np.exp(-self.ener_act/self.R/y2)*np.power(self.Cao, self.orden)*np.power((1-x), self.orden)))


        return [dy1, dy2]


    def plotear(self):
        x = np.arange(self.conv_ini,self.conv_fin,self.deltaT)
        # curve = self.plot.plot(x[:], x[:], pen=None)  ## setting pen=None disables line drawing

        # f = np.vectorize(self.sistema)
        init_state = [self.conv_ini, self.temp_ini]
        state = odeint(self.sistema, init_state, x)


        # y = f(x)
        print(self.K)
        self.plot.clear()

        curve = self.plot.plot(state[:,0],x[:], pen=None)  ## setting pen=None disables line drawing
        curve.curve.setClickable(True)
        curve.setPen('w')  ## white pen
        curve.setShadowPen(pg.mkPen((70, 70, 30), width=6, cosmetic=True))



try:
    app = QtGui.QApplication(sys.argv)
except RuntimeError:
    pass

# MainWindow = QtGui.QWidget()
ui = Reactor_disc_no_adi_no_iso()
# ui.setupUi(MainWindow)
ui.show()
app.exec_()