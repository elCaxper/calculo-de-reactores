import sys
import numpy as np
import pyqtgraph as pg
import scipy.integrate as integrate
from scipy.integrate import odeint
from PySide import QtCore, QtGui
from ventana_FP_general import Ui_Form
import matplotlib as mpl

mpl.use('Qt4Agg')
mpl.rcParams['backend.qt4']='PySide'
import matplotlib.pyplot as plt
from show_cursor import SnaptoCursor, Cursor

class Reactor_FP_general(QtGui.QWidget, Ui_Form):

    def __init__(self):

        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.le_molA.setText('1')
        self.le_molB.setText('2')
        self.rb_endo.setChecked(True)
        self.cb_orden.setCurrentIndex(1)
        self.le_temp_ini.setText('303')
        self.le_concentracion_ini.setText('0.402')
        self.le_ener_act.setText('99773.66')
        self.le_k.setText('2.78E12')
        self.le_caudal.setText('0.2764')
        self.le_diametro.setText('1.5')
        self.le_longitud.setText('80')
        self.le_coef_U.setText('1.34')
        self.le_temp_inter.setText('300')
        self.le_ah.setText('50208')
        self.le_cp.setText('334.94')
        self.le_conv_ini.setText('0')
        self.le_conv_fin.setText('0.5')

        self.deltaT = 0.005
        self.R = 8.3143

        self.plotX.setLabel('left', 'Conversión')
        self.plotX.setLabel('bottom', 'Longitud', units='m')
        self.plotT.setLabel('left', 'Temperatura', units='K')
        self.plotT.setLabel('bottom', 'Longitud', units='m')

        self.btn_mostrar_resultados.setDisabled(True)

        self.btn_ejecutar.clicked.connect(self.ejecutar)
        self.btn_mostrar_resultados.clicked.connect(self.mostrar_resultado)
        self.btn_reset.clicked.connect(self.resetear)
        self.btn_cerrar.clicked.connect(self.close)


    def leerDatos(self):

        self.molA = float(self.le_molA.text())
        self.molB = float(self.le_molB.text())
        self.orden = int(self.cb_orden.currentText()[0].strip())
        self.temp_ini = float(self.le_temp_ini.text())
        self.cao = float(self.le_concentracion_ini.text())
        self.ener_act = float(self.le_ener_act.text())
        self.k = float(self.le_k.text())
        self.caudal = float(self.le_caudal.text())
        self.diametro = float(self.le_diametro.text())
        self.longitud = float(self.le_longitud.text())
        self.coef_U = float(self.le_coef_U.text())
        self.temp_inter = float(self.le_temp_inter.text())

        if (self.rb_exo.isChecked()):
            self.ah = float(self.le_ah.text())
        else:
            self.ah = -float(self.le_ah.text())

        self.cp = float(self.le_cp.text())
        self.conv_ini = float(self.le_conv_ini.text())
        self.conv_fin = float(self.le_conv_fin.text())


    def calcularFactorExpansion(self):

        self.reactivos = self.molA
        self.productos = self.molB

        if (self.reactivos >= self.productos):
            self.factor_exp = (self.reactivos - self.productos)/self.productos
        else:
            self.factor_exp = (self.productos - self.reactivos) / self.reactivos


    def sistema(self, state, l):

        y1, y2 = state

        dy1 = ((self.k * np.exp(-self.ener_act / (self.R * y2))) * ((self.cao * ((1 - self.molA * y1) / (1 + self.factor_exp * y1))) ** (self.orden - 1)) * np.pi * (self.diametro ** 2) * l) / 4 / self.caudal

        dy2 = (self.ah * dy1 / self.cp) + (((self.coef_U * np.pi * self.diametro * (self.temp_inter - y2)) / self.caudal / (self.cao * ((1 - self.molA * y1) / (1 + self.factor_exp * y1))) / self.cp))

        return [dy1, dy2]


    def plotear(self):

        self.x = np.arange(0.05, self.longitud+self.deltaT, self.deltaT)

        init_state = [self.conv_ini, self.temp_ini]
        self.state = odeint(self.sistema, init_state, self.x)

        self.plotX.clear()
        self.plotT.clear()

        curveX = self.plotX.plot(self.x, self.state[:,0], pen=None)  ## setting pen=None disables line drawing
        curveX.curve.setClickable(True)
        curveX.setPen('w')  ## white pen
        curveX.setShadowPen(pg.mkPen((70, 70, 30), width=6, cosmetic=True))

        curveT = self.plotT.plot(self.x, self.state[:,1], pen=None)  ## setting pen=None disables line drawing
        curveT.curve.setClickable(True)
        curveT.setPen('w')  ## white pen
        curveT.setShadowPen(pg.mkPen((70, 70, 30), width=6, cosmetic=True))


    def resetear(self):

        self.le_molA.clear()
        self.le_molB.clear()
        self.rb_exo.setChecked(True)
        self.cb_orden.setCurrentIndex(0)
        self.le_temp_ini.clear()
        self.le_concentracion_ini.clear()
        self.le_ener_act.clear()
        self.le_k.clear()
        self.le_caudal.clear()
        self.le_diametro.clear()
        self.le_longitud.clear()
        self.le_coef_U.clear()
        self.le_temp_inter.clear()
        self.le_ah.clear()
        self.le_cp.clear()
        self.le_conv_ini.clear()
        self.le_conv_fin.clear()
        self.le_xa.clear()
        self.le_temperatura.clear()
        self.le_long1.clear()
        self.le_long2.clear()
        self.plotX.clear()
        self.plotT.clear()

        self.btn_mostrar_resultados.setDisabled(True)


    def ejecutar(self):

        if self.le_molA.text() == "" or self.le_molB.text() == "" or self.le_temp_ini.text() == "" or self.le_concentracion_ini.text() == "" or self.le_ener_act.text() == "" or self.le_k.text() == "" or self.le_caudal.text() == "" or self.le_ah.text() == "" or self.le_cp.text() == "" or self.le_conv_ini.text() == "" or self.le_conv_fin.text() == "":
            QtGui.QMessageBox.warning(self, "Error en la ejecución", "Alguna/s de las celdas de datos está/n vacía/s. Por favor, revise que ha introducido correctamente todos los datos.", QtGui.QMessageBox.Cancel, QtGui.QMessageBox.NoButton)
        else:
            self.leerDatos()
            self.calcularFactorExpansion()
            self.plotear()

            self.le_long1.setText(str(self.longitud))
            self.le_long2.setText(str(self.longitud))
            self.le_xa.setText(str(float("{0:.2f}".format(self.state[-1,0]))))
            self.le_temperatura.setText(str(float("{0:.2f}".format(self.state[-1,1]))))

            self.btn_mostrar_resultados.setEnabled(True)


    def mostrar_resultado(self):

        self.fig, (self.conv, self.temp) = plt.subplots(2, 1, sharex=True)

        self.conv.set_title('RESULTADO')

        self.conv.set_xlim([min(self.x), max(self.x)])
        self.temp.set_xlabel('Longitud (m)')

        self.conv.set_ylim([min(self.state[:,0]), max(self.state[:,0])])
        self.conv.set_ylabel('Conversión')

        # cursor = Cursor(ax)

        self.cursor1 = SnaptoCursor(self.conv, self.x, self.state[:,0])
        plt.connect('motion_notify_event', self.cursor1.mouse_move)

        self.temp.set_ylim([min(self.state[:,1]), max(self.state[:,1])])
        self.temp.set_ylabel('Temperatura (K)')

        self.cursor2 = SnaptoCursor(self.temp, self.x, self.state[:,1])
        plt.connect('motion_notify_event', self.cursor2.mouse_move)

        self.conv.plot(self.x, self.state[:,0], linewidth=2)
        self.temp.plot(self.x, self.state[:,1], linewidth = 2)

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
    ui = Reactor_FP_general()
    # ui.setupUi(MainWindow)
    ui.show()
    app.exec_()
