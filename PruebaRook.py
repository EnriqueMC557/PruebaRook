# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PruebaRook.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from QPyQt5Canvas import QPyQt5Canvas


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(627, 457)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 370, 561, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TimeLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.TimeLabel.setObjectName("TimeLabel")
        self.horizontalLayout.addWidget(self.TimeLabel)
        self.TimeText = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.TimeText.setObjectName("TimeText")
        self.horizontalLayout.addWidget(self.TimeText)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.TemperatureLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.TemperatureLabel.setWordWrap(True)
        self.TemperatureLabel.setObjectName("TemperatureLabel")
        self.horizontalLayout.addWidget(self.TemperatureLabel)
        self.TemperatureText = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TemperatureText.sizePolicy().hasHeightForWidth())
        self.TemperatureText.setSizePolicy(sizePolicy)
        self.TemperatureText.setObjectName("TemperatureText")
        self.horizontalLayout.addWidget(self.TemperatureText)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.LoadLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.LoadLabel.setObjectName("LoadLabel")
        self.horizontalLayout.addWidget(self.LoadLabel)
        self.LoadText = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.LoadText.setObjectName("LoadText")
        self.horizontalLayout.addWidget(self.LoadText)
        self.PlotButton = QtWidgets.QPushButton(Form)
        self.PlotButton.setGeometry(QtCore.QRect(250, 420, 121, 25))
        self.PlotButton.setObjectName("PlotButton")
        self.PlotCanvas = QPyQt5Canvas(Form)
        self.PlotCanvas.setGeometry(QtCore.QRect(40, 20, 561, 331))
        self.PlotCanvas.setObjectName("PlotCanvas")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Prueba DAQ Developer"))
        self.TimeLabel.setText(_translate("Form", "Hora actual:"))
        self.TimeText.setText(_translate("Form", "HH:MM:SS"))
        self.TemperatureLabel.setText(_translate("Form", "Temperatura del sistema"))
        self.TemperatureText.setText(_translate("Form", "AA.DDD"))
        self.LoadLabel.setText(_translate("Form", "Carga de CPU"))
        self.LoadText.setText(_translate("Form", "DD"))
        self.PlotButton.setText(_translate("Form", "Graficar datos"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
