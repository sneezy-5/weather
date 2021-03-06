# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 791, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.barometer = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.barometer.setMaximumSize(QtCore.QSize(16777215, 25))
        self.barometer.setObjectName("barometer")
        self.verticalLayout.addWidget(self.barometer)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.image = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.image.setText("")
        self.image.setObjectName("image")
        self.horizontalLayout_3.addWidget(self.image)
        self.temperature = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.temperature.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.temperature.setText("")
        self.temperature.setObjectName("temperature")
        self.horizontalLayout_3.addWidget(self.temperature)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.longitude = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.longitude.setText("")
        self.longitude.setObjectName("longitude")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.longitude)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.latitude = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.latitude.setText("")
        self.latitude.setObjectName("latitude")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.latitude)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.vent = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.vent.setText("")
        self.vent.setObjectName("vent")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.vent)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.hour_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hour_1.setObjectName("hour_1")
        self.gridLayout.addWidget(self.hour_1, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 2, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.hour_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hour_5.setObjectName("hour_5")
        self.gridLayout.addWidget(self.hour_5, 0, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 2, 4, 1, 1)
        self.hour_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hour_3.setObjectName("hour_3")
        self.gridLayout.addWidget(self.hour_3, 0, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 4, 1, 1)
        self.hour_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hour_2.setObjectName("hour_2")
        self.gridLayout.addWidget(self.hour_2, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 2, 1, 1)
        self.hour_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hour_4.setObjectName("hour_4")
        self.gridLayout.addWidget(self.hour_4, 0, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.barometer.setText(_translate("MainWindow", "Barometer"))
        self.label.setText(_translate("MainWindow", "Location"))
        self.label_2.setText(_translate("MainWindow", "Pression"))
        self.label_3.setText(_translate("MainWindow", "Humidit??"))
        self.label_4.setText(_translate("MainWindow", "Vent"))
        self.hour_1.setText(_translate("MainWindow", "+1h"))
        self.hour_5.setText(_translate("MainWindow", "+5h"))
        self.hour_3.setText(_translate("MainWindow", "+3h"))
        self.hour_2.setText(_translate("MainWindow", "+2H"))
        self.hour_4.setText(_translate("MainWindow", "+4h"))
