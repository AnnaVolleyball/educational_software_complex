import random
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pylab


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 584)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("Графік")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


class MyMplCanvas(FigureCanvas):
    def __init__(self, *args, **kwargs):
        self.fig = Figure()
        super(MyMplCanvas, self).__init__(self.fig, *args, **kwargs)

    def onMouseClick(self, event):
        axes = event.inaxes

        # Если кликнули вне какого-либо графика, то не будем ничего делать
        if axes is None:
            return

        # В качестве текущих выберем оси, внутри которых кликнули мышью
        self.fig.sca(axes)
        #q = self.fig.add_subplot(111)

        # Координаты клика в системе координат осей
        a = event.xdata
        b = event.ydata

        x.append(a)
        y.append(b)
        # Выведем точку, куда кликнули
        self.ax.plot(a, b, 'bo')

        # Выведем график из точек
        self.ax.plot(x, y, color='blue', linewidth=2)

        # Сделаем заливку графика
        self.ax.fill(x, y, color='blue')

        # Обновим рисунок
        self.ax.set_thetagrids(np.arange(0.0, 360.0, 30.0))
        self.ax.set_rgrids(np.arange(0, 100, 10))
        self.draw()

    def plot(self, labels, men_means, women_means, x, width):  # !!!
        self.fig.clear()  # !!!

        self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
        self.ax.set_thetagrids(np.arange(0.0, 360.0, 30.0))
        self.ax.set_rgrids(np.arange(10, 100, 10))

        self.fig.canvas.mpl_connect('button_press_event', self.onMouseClick)
        self.draw()  # !!!

x = []
y = []


class Sheet(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self._plot)

        self.canavas = MyMplCanvas()
        self.toolbar = NavigationToolbar(self.canavas, self)

        self.layout = QVBoxLayout(self.widget)
        self.layout.addWidget(self.canavas)
        self.layout.addWidget(self.toolbar)

    def _plot(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        men_means = [random.randrange(1, 100) for _ in range(5)]
        women_means = [random.randrange(1, 100) for _ in range(5)]
        x = np.arange(len(labels))  # расположение столбиков
        width = 0.35  # толщина столбика

        self.canavas.plot(labels, men_means, women_means, x, width)  # !!!


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = Sheet()
    win.show()
    sys.exit(app.exec_())