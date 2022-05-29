# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Laboratornaya.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LabMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1800, 960)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(67, 15, 222, 255), stop:1 rgba(156, 20, 222, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setHorizontalSpacing(30)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 700))
        self.graphicsView.setStyleSheet("background-color: rgb(153, 135, 255);")
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_2.addWidget(self.graphicsView, 0, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(500, 500))
        self.widget.setStyleSheet("background-color: rgb(153, 135, 255);")
        self.widget.setObjectName("widget")
        self.verticalLayout_4.addWidget(self.widget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(156, 20, 222, 255);\n"
"background-color: white;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(60)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout.addWidget(self.radioButton_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(156, 20, 222, 255);\n"
"background-color: white;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(60)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_13 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_13.setFont(font)
        self.radioButton_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_13.setObjectName("radioButton_13")
        self.verticalLayout.addWidget(self.radioButton_13)
        self.radioButton_15 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_15.setFont(font)
        self.radioButton_15.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_15.setObjectName("radioButton_15")
        self.verticalLayout.addWidget(self.radioButton_15)
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout.addWidget(self.radioButton_6)
        self.radioButton_9 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_9.setFont(font)
        self.radioButton_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_9.setObjectName("radioButton_9")
        self.verticalLayout.addWidget(self.radioButton_9)
        self.radioButton_12 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_12.setFont(font)
        self.radioButton_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_12.setObjectName("radioButton_12")
        self.verticalLayout.addWidget(self.radioButton_12)
        self.radioButton_10 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_10.setFont(font)
        self.radioButton_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_10.setObjectName("radioButton_10")
        self.verticalLayout.addWidget(self.radioButton_10)
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_7.setObjectName("radioButton_7")
        self.verticalLayout.addWidget(self.radioButton_7)
        self.radioButton_16 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_16.setFont(font)
        self.radioButton_16.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_16.setObjectName("radioButton_16")
        self.verticalLayout.addWidget(self.radioButton_16)
        self.radioButton_11 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_11.setFont(font)
        self.radioButton_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_11.setObjectName("radioButton_11")
        self.verticalLayout.addWidget(self.radioButton_11)
        self.radioButton_14 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_14.setFont(font)
        self.radioButton_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_14.setObjectName("radioButton_14")
        self.verticalLayout.addWidget(self.radioButton_14)
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout.addWidget(self.radioButton_5)
        self.radioButton_8 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_8.setChecked(True)
        self.radioButton_8.setObjectName("radioButton_8")
        self.verticalLayout.addWidget(self.radioButton_8)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_17 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_17.setFont(font)
        self.radioButton_17.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_17.setChecked(False)
        self.radioButton_17.setObjectName("radioButton_17")
        self.verticalLayout_2.addWidget(self.radioButton_17)
        self.radioButton_18 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_18.setFont(font)
        self.radioButton_18.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_18.setObjectName("radioButton_18")
        self.verticalLayout_2.addWidget(self.radioButton_18)
        self.radioButton_19 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_19.setFont(font)
        self.radioButton_19.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_19.setObjectName("radioButton_19")
        self.verticalLayout_2.addWidget(self.radioButton_19)
        self.radioButton_20 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_20.setFont(font)
        self.radioButton_20.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_20.setObjectName("radioButton_20")
        self.verticalLayout_2.addWidget(self.radioButton_20)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_21 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_21.setFont(font)
        self.radioButton_21.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_21.setChecked(False)
        self.radioButton_21.setObjectName("radioButton_21")
        self.verticalLayout_3.addWidget(self.radioButton_21)
        self.radioButton_22 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_22.setFont(font)
        self.radioButton_22.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.radioButton_22.setObjectName("radioButton_22")
        self.verticalLayout_3.addWidget(self.radioButton_22)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Построить график"))
        self.radioButton.setText(_translate("MainWindow", "Белый"))
        self.radioButton_2.setText(_translate("MainWindow", "Синий"))
        self.radioButton_3.setText(_translate("MainWindow", "Красный"))
        self.radioButton_4.setText(_translate("MainWindow", "Зеленый"))
        self.pushButton_2.setText(_translate("MainWindow", "Проявить области"))
        self.radioButton_13.setText(_translate("MainWindow", "120°"))
        self.radioButton_15.setText(_translate("MainWindow", "180°"))
        self.radioButton_6.setText(_translate("MainWindow", "60°"))
        self.radioButton_9.setText(_translate("MainWindow", "300°"))
        self.radioButton_12.setText(_translate("MainWindow", "90°"))
        self.radioButton_10.setText(_translate("MainWindow", "210°"))
        self.radioButton_7.setText(_translate("MainWindow", "240°"))
        self.radioButton_16.setText(_translate("MainWindow", "330°"))
        self.radioButton_11.setText(_translate("MainWindow", "150°"))
        self.radioButton_14.setText(_translate("MainWindow", "270°"))
        self.radioButton_5.setText(_translate("MainWindow", "30°"))
        self.radioButton_8.setText(_translate("MainWindow", "0°"))
        self.radioButton_17.setText(_translate("MainWindow", "Белый"))
        self.radioButton_18.setText(_translate("MainWindow", "Синий"))
        self.radioButton_19.setText(_translate("MainWindow", "Красный"))
        self.radioButton_20.setText(_translate("MainWindow", "Зеленый"))
        self.radioButton_21.setText(_translate("MainWindow", "Левый глаз"))
        self.radioButton_22.setText(_translate("MainWindow", "Правый глаз"))
