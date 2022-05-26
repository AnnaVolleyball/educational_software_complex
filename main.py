# -*- coding: UTF-8 -*-
import sys

from PyQt5.QtCore import QRectF
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QButtonGroup
from PyQt5 import QtGui, QtWidgets

from MainWindow import Ui_MainWindow
from Laboratornaya import Ui_LabMainWindow
from Lectsia import Ui_LecMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np


class WorkWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle("Технические средства для офтальмологии")
        self.pushButton.clicked.connect(self.show_lec)
        self.pushButton_2.clicked.connect(self.show_lab)

    def show_lab(self):
        self.LabWin = LabWindow()
        self.LabWin.show()
        # self.close()

    def show_lec(self):
        self.LecWin = LecWindow()
        self.LecWin.show()
        # self.close()


class LecWindow(QMainWindow, Ui_LecMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle("Методический материал")


class LabWindow(QMainWindow, Ui_LabMainWindow, QButtonGroup):
    def __init__(self):
        try:
            self.fig = Figure()
            super().__init__()
            self.setupUi(self)
            self.setWindowIcon(QtGui.QIcon('icon.png'))
            self.setWindowTitle("Лабораторная работа")
            self.button_group_eye = QButtonGroup()
            self.button_group_color_left = QButtonGroup()
            self.button_group_color = QButtonGroup()
            self.button_group_gradus = QButtonGroup()

            self.button_group_eye.addButton(self.radioButton_21)
            self.button_group_eye.addButton(self.radioButton_22)
            self.radioButton_22.setChecked(True)

            self.button_group_color_left.addButton(self.radioButton_17)
            self.button_group_color_left.addButton(self.radioButton_18)
            self.button_group_color_left.addButton(self.radioButton_19)
            self.button_group_color_left.addButton(self.radioButton_20)
            self.radioButton_17.setChecked(True)

            self.button_group_gradus.addButton(self.radioButton_5)
            self.button_group_gradus.addButton(self.radioButton_6)
            self.button_group_gradus.addButton(self.radioButton_7)
            self.button_group_gradus.addButton(self.radioButton_8)
            self.button_group_gradus.addButton(self.radioButton_9)
            self.button_group_gradus.addButton(self.radioButton_10)
            self.button_group_gradus.addButton(self.radioButton_11)
            self.button_group_gradus.addButton(self.radioButton_12)
            self.button_group_gradus.addButton(self.radioButton_13)
            self.button_group_gradus.addButton(self.radioButton_14)
            self.button_group_gradus.addButton(self.radioButton_15)
            self.button_group_gradus.addButton(self.radioButton_16)

            self.button_group_color.addButton(self.radioButton)
            self.button_group_color.addButton(self.radioButton_2)
            self.button_group_color.addButton(self.radioButton_3)
            self.button_group_color.addButton(self.radioButton_4)

            self.button_group_gradus.buttonToggled[QtWidgets.QAbstractButton, bool].connect(self.change_picture)
            self.button_group_color_left.buttonToggled[QtWidgets.QAbstractButton, bool].connect(self.change_picture)
            self.button_group_eye.buttonToggled[QtWidgets.QAbstractButton, bool].connect(self.change_picture)

            self.canvas = MyMplCanvas(self)
            self.toolbar = NavigationToolbar(self.canvas, self)

            self.layout = QVBoxLayout(self.widget)
            self.layout.addWidget(self.canvas)
            self.layout.addWidget(self.toolbar)

            self.pushButton.clicked.connect(self.canvas.print_graf)
            self.pushButton_2.clicked.connect(self.canvas.make_fill)

            self.change_picture()

        except Exception as e:
            print(e)

    def ret_color(self):
        if self.radioButton.isChecked():
            return "yellow"
        elif self.radioButton_2.isChecked():
            return "blue"
        elif self.radioButton_3.isChecked():
            return "red"
        elif self.radioButton_4.isChecked():
            return "green"

    def change_picture(self):
        try:
            title = self.button_group_eye.checkedButton().text()
            title1 = self.button_group_color_left.checkedButton().text()
            title2 = self.button_group_gradus.checkedButton().text()
            stroka = ''

            if title == "Правый глаз":
                stroka += "R"
            else:
                stroka += "L"

            if title1 == 'Синий':
                stroka += 'b'
            elif title1 == 'Красный':
                stroka += 'r'
            elif title1 == 'Зеленый':
                stroka += 'g'
            else:
                stroka += 'w'

            stroka += title2[:-1]
            print(stroka)
            self.scene = QtWidgets.QGraphicsScene(self)
            self.graphicsView.setScene(self.scene)
            self.pixmapItem = self.scene.addPixmap(QtGui.QPixmap(f"{stroka}.tiff").scaled(834, 1194))
            # self.label.setPixmap(QtGui.QPixmap(f"{stroka}.tiff").scaled(556, 796))
        except Exception as e:
            print(e)


class MyMplCanvas(FigureCanvas, Ui_LabMainWindow):
    def __init__(self, win):
        self.fig = Figure()
        self.win = win
        super(MyMplCanvas, self).__init__(self.fig)

    def onMouseClick(self, event):
        axes = event.inaxes

        # Если кликнули вне какого-либо графика, то не будем ничего делать
        if axes is None:
            return

        # В качестве текущих выберем оси, внутри которых кликнули мышью
        self.fig.sca(axes)

        # Координаты клика в системе координат осей
        a = event.xdata
        b = event.ydata

        color = self.win.ret_color()

        x, y = self.pins[color]
        x.append(a)
        y.append(b)


        # Выведем точку, куда кликнули
        self.ax.plot(a, b, f'{color[0]}o')

        # Выведем график из точек
        self.ax.plot(x, y, color=color, linewidth=2)


        # Обновим рисунок
        self.ax.set_thetagrids(np.arange(0.0, 360.0, 30.0))
        self.ax.set_rgrids(np.arange(0, 100, 10))
        self.draw()

    def print_graf(self):
            try:
                self.fig.clear()  # !!!

                self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
                self.ax.set_thetagrids(np.arange(0.0, 360.0, 30.0))
                self.ax.set_rgrids(np.arange(10, 100, 10))

                self.fig.canvas.mpl_connect('button_press_event', self.onMouseClick)
                self.draw()  # !!!
                self.pins = {"yellow": [[], []],
                             "blue": [[], []],
                             "red": [[], []],
                             "green": [[], []]}
            except Exception as e:
                print(e)

    def make_fill(self):
        color = self.win.ret_color()

        x, y = self.pins[color]
        # Сделаем заливку графика
        self.ax.fill(x, y, color=color, alpha=0.1)

        # Обновим рисунок
        self.ax.set_thetagrids(np.arange(0.0, 360.0, 30.0))
        self.ax.set_rgrids(np.arange(0, 100, 10))
        self.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WorkWindow()
    ex.show()
    sys.exit(app.exec())

