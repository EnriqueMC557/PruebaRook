import sys
from PruebaRook import Ui_Form
from DataBase import RookDataBase
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer, QThread

class gui(QWidget):
    def __init__(self, parent=None):
        # Inicializador de GUI
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.figure = self.ui.PlotCanvas.canvas
        self.BDD = RookDataBase()

        # Inicializador de QTimer
        self.timer = QTimer()
        self.timer.start(60000) # Reinicio cada 1 minuto (60 segundos)

        # Conexion de señal de Qtimer con slot
        self.timer.timeout.connect(self.cambioHora)
        self.timer.timeout.connect(self.cambioTemperatura)
        self.timer.timeout.connect(self.cambioCarga)

        # Conexion de señal de botón con slot
        self.ui.PlotButton.clicked.connect(self.plotData)

    def cambioHora(self):
        self.BDD.localTime()
        self.ui.TimeText.setText(f'{self.BDD.time}')

    def cambioTemperatura(self):
        self.BDD.insertTemperature()
        self.ui.TemperatureText.setText(f'{self.BDD.temp}')

    def cambioCarga(self):
        self.BDD.insertCPUload()
        self.ui.LoadText.setText(f'{self.BDD.loadCPU}')

    def plotData(self):
        self.BDD.select_all()
        self.figure.ax.clear()
        self.figure.ax.plot(self.BDD.temperatureValues)
        self.figure.ax.plot(self.BDD.loadValues)
        self.figure.ax.legend(['Temperatura', 'Carga CPU'])
        self.figure.ax.grid(True)
        self.figure.draw()
        
    def closeEvent(self, event):
        self.BDD.close()

if __name__ == '__main__':
    # crea la instancia de la aplicación
    app = QApplication(sys.argv)
    # crea la instancia de la GUI
    gui = gui()
    # nuestra la GUI
    gui.show()
    # ejecuta la aplicación
    sys.exit(app.exec_())
