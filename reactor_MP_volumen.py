import sys
from PySide import QtCore, QtGui
import numpy as np
import pyqtgraph as pg
from ventana_MP_volumen import Ui_Form


class Reactor_mp_volumen(QtGui.QWidget, Ui_Form):

    def __init__(self):

        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.le_molA.setText('1')
        self.le_molB.setText('1')
        self.cb_orden.setCurrentIndex(2)
        self.le_temp_fin.setText('393')
        self.le_concentracion_ini.setText('6.65')
        self.le_ener_act.setText('83680')
        self.le_k.setText('55000000')
        self.le_caudal.setText('1.26')
        self.le_conv_fin.setText('0.5')

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
        self.orden = int(self.cb_orden.currentText()[0].strip())
        self.temp_fin = float(self.le_temp_fin.text())
        self.cao = float(self.le_concentracion_ini.text())
        self.ener_act = float(self.le_ener_act.text())
        self.k = float(self.le_k.text())
        self.caudal = float(self.le_caudal.text())
        self.conv_fin = float(self.le_conv_fin.text())


    def calcularK(self):

        self.K = self.k * np.exp(-self.ener_act / (self.R * self.temp_fin))


    def f0(self, conv):

        Ca = lambda conv: self.cao * (1 - self.molA * conv)

        ra = self.K * (Ca(conv) ** self.orden)

        volumen = self.conv_fin * self.caudal * self.cao / ra

        return volumen


    def plotear(self):

        x = np.arange(0, self.conv_fin, self.deltaT)

        f = np.vectorize(self.f0)

        y = f(x)

        self.plot.clear()
        curve = self.plot.plot(y, x, pen=None)  ## setting pen=None disables line drawing
        curve.curve.setClickable(True)
        curve.setPen('w')  ## white pen

        curve.setShadowPen(pg.mkPen((70, 70, 30), width=6, cosmetic=True))


    def resetear(self):

        self.le_molA.clear()
        self.le_molB.clear()
        self.cb_orden.setCurrentIndex(0)
        self.le_temp_fin.clear()
        self.le_concentracion_ini.clear()
        self.le_ener_act.clear()
        self.le_k.clear()
        self.le_caudal.clear()
        self.le_conv_fin.clear()
        self.le_volumen.clear()
        self.le_xa.clear()
        self.plot.clear()


    def ejecutar(self):

        if self.le_molA.text() == "" or self.le_molB.text() == "" or self.le_temp_fin.text() == "" or self.le_concentracion_ini.text() == "" or self.le_ener_act.text() == "" or self.le_k.text() == "" or self.le_caudal.text() == "" or self.le_conv_fin.text() == "":
            QtGui.QMessageBox.warning(self, "Error en la ejecución", "Alguna/s de las celdas de datos está/n vacía/s. Por favor, revise que ha introducido correctamente todos los datos.", QtGui.QMessageBox.Cancel, QtGui.QMessageBox.NoButton)
        else:
            self.leerDatos()
            self.calcularK()
            self.plotear()

            self.le_xa.setText(str(self.conv_fin))
            self.le_volumen.setText(str(float("{0:.2f}".format(self.f0(self.conv_fin)))))


try:
    app = QtGui.QApplication(sys.argv)
except RuntimeError:
    pass


# MainWindow = QtGui.QWidget()
ui = Reactor_mp_volumen()
# ui.setupUi(MainWindow)
ui.show()
app.exec_()
