#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Oscar Yáñez Suárez, 2020

This work is licensed under the Creative Commons Attribution 4.0
International License. To view a copy of this license, visit
http://creativecommons.org/licenses/by/4.0/ or send a letter to
Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

class PyQt5Canvas(FigureCanvasQTAgg):
    """
    Clase derivada de FigureCanvas para hacer gráficas en Qt con matplotlib
    """
    def __init__(self):
        """
        Constructor
        """
        # Crea una figura de matplotlib
        self.fig = Figure(facecolor='0.94')
        # Agrega unos ejes
        self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8])
        # invoca al constructor de la clase
        FigureCanvasQTAgg.__init__(self, self.fig)

class QPyQt5Canvas(QWidget):
    """
    Widget básico de Qt con un PyQt5Canvas dentro de un layout vertical
    """
    def __init__(self, parent=None):
        """
        Constructor
        """
        QWidget.__init__(self, parent)
        self.canvas = PyQt5Canvas()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)
