import sys
import time
from PruebaRook import Ui_Form
from DataBase import RookDataBase
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QThread, pyqtSignal

class gui(QWidget):
    def __init__(self, parent=None):
        # Inicializador de GUI
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.figure = self.ui.PlotCanvas.canvas
        self.BDD = RookDataBase()
        
        # Inicialización de thread para temperatura
        self.thread1 = Thread1()
        self.thread1.newTimeTemperature.connect(self.cambioTemperatura)
        self.thread1.start()
        
        # Inicialización de thread para carga
        self.thread2 = Thread2()
        self.thread2.newTimeLoad.connect(self.cambioCarga)
        self.thread2.start()

        # Conexion de señal de botón con slot
        self.ui.PlotButton.clicked.connect(self.plotData)

    def cambioTemperatura(self, time, temperature):
        # Cambia texto de tiempo y temperatura
        self.ui.TimeText.setText(time)
        self.ui.TemperatureText.setText(temperature)

    def cambioCarga(self, time, load):
        # Cambia texto de tiempo y carga
        self.ui.TimeText.setText(time)
        self.ui.LoadText.setText(load)

    def plotData(self):
        # Consulta datos de temperatura y carga de las ultimas 8 hrs
        self.BDD.select_all()
        # Grafica los datos
        self.figure.ax.clear()
        self.figure.ax.plot_date(self.BDD.timeValues, self.BDD.temperatureValues, '-')
        self.figure.ax.plot_date(self.BDD.timeValues, self.BDD.loadValues, '-')
        self.figure.ax.tick_params('x', labelrotation = 10, labelsize = 8)
        self.figure.ax.legend(['Temperatura (°C)', 'Carga CPU (%)'])
        self.figure.ax.set_xlabel('Marca de tiempo (YYYY-MM-DD HH:MM:SS)')
        self.figure.ax.set_ylabel('Valor')
        self.figure.ax.grid(True)
        self.figure.draw()
        
    def closeEvent(self, event):
        # Termina conexiones con BDD
        self.BDD.close()
        self.thread1.BDD.close()
        self.thread2.BDD.close()
        

class Thread1(QThread):
    # Señal para envío de tiempo y temperatura
    newTimeTemperature = pyqtSignal(str, str)
    # Conexión a BDD
    BDD = RookDataBase()
        
    def run(self):
        while True:
            # Espera 1 minuto (60 segundos)
            time.sleep(60)
            # Consulta e inserta tiempo y temperatura
            self.BDD.insertTemperature()
            # Envía señal con tiempo y temperatura
            self.newTimeTemperature.emit(self.BDD.time[11:], str(self.BDD.temp))

class Thread2(QThread):
    # Señal para envío de tiempo y carga
    newTimeLoad = pyqtSignal(str, str)
    # Conexión a BDD
    BDD = RookDataBase()
    
    def run(self):
        while True:
            # Espera 1 minuto (60 segundos)
            time.sleep(60)
            # Consulta e inserta tiempo y carga
            self.BDD.insertCPUload()
            # Envía señal con tiempo y carga
            self.newTimeLoad.emit(self.BDD.time[11:], str(self.BDD.loadCPU))
                
if __name__ == '__main__':
    # Crea la instancia de la aplicación
    app = QApplication(sys.argv)
    # Crea la instancia de la GUI
    gui = gui()
    # Muestra la GUI
    gui.show()
    # Ejecuta la aplicación
    sys.exit(app.exec_())
