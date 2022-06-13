# -*- coding: UTF-8 -*-
import sys
import sqlite3
import random
import matplotlib.pyplot as plt
import numpy as np
import datetime

from PyQt5.QtCore import QRectF, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QButtonGroup
from PyQt5 import QtGui, QtWidgets

from MainWindow import Ui_MainWindow
from Laboratornaya import Ui_LabMainWindow
from Lectsia import Ui_LecMainWindow
from TestStud import Ui_TestMainWindow
from Info import Ui_InfoMainWindow
from Out_Time import Ui_TimeMainWindow
from Registration import Ui_RegMainWindow
from Results import Ui_ResMainWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class WorkWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, FIO, group, id, connection):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle("Технические средства для офтальмологии")
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.pushButton.clicked.connect(self.show_lec)
        self.pushButton_2.clicked.connect(self.show_lab)
        self.pushButton_3.clicked.connect(self.show_test)
        self.pushButton_7.clicked.connect(self.show_info)

        self.FIO = FIO
        self.group = group
        self.id = id

        self.pushButton_10.setText(self.FIO)
        self.pushButton_11.setText(self.group)

        self.update_statistics()

    def update_statistics(self):
        try:
            self.best = self.cursor.execute(
                f"select popytka, a_true, a_false, a_none, result from Results_Students where id_student = {self.id} ORDER BY a_true DESC, result DESC").fetchone()
            print(self.best)
            self.kolvo_popytk = self.cursor.execute(
                f"SELECT Popytky FROM Students WHERE FIO='{self.FIO}' AND gruppa='{self.group}'").fetchone()
            # self.id_stud = self.cursor.execute(  УЖЕ ПЕРЕДАЛИ В ФУНКЦИЮ
            #     f"SELECT id FROM Students WHERE FIO='{self.FIO}' AND gruppa='{self.group}'").fetchone()
            self.pushButton_14.setText(f"{self.kolvo_popytk[0]}")
            self.pushButton_15.setText(f"{self.best[4]}/10")

        except Exception as e:
            print(e)

        self.figure = plt.figure(figsize=(341, 341))
        self.canvas = FigureCanvas(self.figure)

        self.layout = QVBoxLayout(self.widget)
        self.layout.addWidget(self.canvas)

        ax = self.figure.add_subplot(111)
        plt.rcParams['axes.facecolor'] = 'white'

        labels = 'Правильно', 'Неправильно', 'Пропущено'
        sizes = [self.best[1], self.best[2], self.best[3]]
        colors = ['yellowgreen', 'lightcoral', 'lightskyblue']
        pie = ax.pie(sizes, colors=colors, shadow=True, autopct='%1.1f%%', startangle=90)
        ax.legend(pie[0], labels, loc="lower right")
        self.figure.patch.set_facecolor('blue')
        self.figure.patch.set_alpha(0.0)

    def show_lab(self):
        self.LabWin = LabWindow()
        self.LabWin.show()
        # self.close()

    def show_lec(self):
        self.LecWin = LecWindow()
        self.LecWin.show()
        # self.close()

    def show_test(self):
        self.TestWin = TestWindow(self.FIO, self.id, self.group, self.connection, self)
        self.TestWin.show()
        # self.close()

    def show_info(self):
        self.InfoWin = InfoWindow()
        self.InfoWin.show()
        # self.close()


class InfoWindow(QMainWindow, Ui_InfoMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle("О программе")


class ResWindow(QMainWindow, Ui_ResMainWindow):
    def __init__(self, FIO, id, group, pop, quest_number, true_answer, false_answer, none_answer):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle("Результаты теста")
        self.pushButton.clicked.connect(self.ret_on_MainWind)

        self.FIO = FIO
        self.id = id
        self.group = group
        self.pop = pop
        self.quest_number = quest_number
        self.true_answer = true_answer
        self.false_answer = false_answer
        self.none_answer = none_answer

        self.label_5.setText(f"{self.FIO}")
        self.label_6.setText(f"{self.group}")
        self.label_7.setText(f"{self.pop}")
        self.label_8.setText(f"{self.quest_number}/10")
        self.label_10.setText(f"{self.true_answer}")
        self.label_12.setText(f"{self.true_answer - self.false_answer}")

        self.figure = plt.figure(figsize=(341, 341))
        self.canvas = FigureCanvas(self.figure)

        self.layout = QVBoxLayout(self.widget)
        self.layout.addWidget(self.canvas)

        ax = self.figure.add_subplot(111)
        plt.rcParams['axes.facecolor'] = 'white'

        labels = 'Правильно', 'Неправильно', 'Пропущено'
        sizes = [self.true_answer, self.false_answer, self.none_answer]
        colors = ['yellowgreen', 'lightcoral', 'lightskyblue']
        pie = ax.pie(sizes, colors=colors, shadow=True, autopct='%1.1f%%', startangle=90)
        ax.legend(pie[0], labels, loc="lower right")
        self.figure.patch.set_facecolor('blue')
        self.figure.patch.set_alpha(0.0)

    def ret_on_MainWind(self):
        # self.update_statistics()
        self.close()


class TimeWindow(QMainWindow, Ui_TimeMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle("Завершение теста")
        self.pushButton.clicked.connect(self.close_and_saveBD)

    def close_and_saveBD(self):
        self.close()


class LecWindow(QMainWindow, Ui_LecMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle("Методический материал")


class TestWindow(QMainWindow, Ui_TestMainWindow):
    def __init__(self, FIO, id, group, connection, workWin):
        super().__init__()
        self.workWin = workWin
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle("Тестирование по лекции")
        # self.connection = sqlite3.connect("BD_TSDO.db")
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.quest_number = 0
        self.slovar = {}
        self.FIO = FIO
        self.id = id
        self.group = group
        self.true_answer = 0
        self.false_answer = 0
        self.none_answer = 0
        self.pop = self.cursor.execute(f"SELECT Popytky FROM Students WHERE id={self.id}").fetchone()
        self.pop = self.pop[0]

        self.pushButton_2.clicked.connect(self.check_and_next)
        self.pushButton.clicked.connect(self.close_lec_and_time)

        self.button_group_ans = QButtonGroup()
        self.button_group_ans.addButton(self.radioButton)
        self.button_group_ans.addButton(self.radioButton_2)
        self.button_group_ans.addButton(self.radioButton_3)
        self.button_group_ans.addButton(self.radioButton_4)

        self.questions = [i for i in range(1, 11)]
        random.shuffle(self.questions)
        self.questions = self.questions[:10]

        self.timer = QTimer(self)
        self.startTimer()
        self.timer.timeout.connect(self.timerTick)
        self.closeEvent = self.close_lec_and_time

        self.update_window()

    def startTimer(self):
        # 420
        self.inicio = 10
        self.updateTimerDisplay()
        self.timer.start(1000)

    def updateTimerDisplay(self):
        text = "%d:%02d" % (self.inicio / 60, self.inicio % 60)
        self.lcdNumber.display(text)

    def close_lec_and_time(self, ev):
        # self.TimeWin.close()
        #ЗДЕСЬ ЗАПИСЫВАЕМ РЕЗУЛЬТАТЫ ТЕСТА В БД
        print(self.pop)
        self.pop += 1
        print(self.pop)
        print(self.id)
        try:
            if self.true_answer == 0 and self.false_answer == 0 and self.none_answer == 0:
                self.none_answer = 10
            self.cursor.execute(f"""INSERT INTO Results_Students (a_true, a_false, a_none, popytka, id_student, result)
                                 VALUES ({self.true_answer}, {self.false_answer}, {self.none_answer}, {self.pop}, {self.id}, {self.quest_number})""")
            self.connection.commit()
            self.cursor.execute(f"""UPDATE Students SET Popytky = {self.pop}
                                    WHERE id={self.id}""")
            self.connection.commit()
        except Exception as e:
            print(e)
        self.end_test()
        self.close()

    def show_out_time(self):
        self.TimeWin = TimeWindow()
        self.TimeWin.show()
        self.setEnabled(False)
        self.TimeWin.closeEvent = self.close_lec_and_time

    def timerTick(self):
        self.inicio -= 1
        self.updateTimerDisplay()
        if self.inicio <= 0:
            self.timer.stop()
            self.show_out_time()

    def update_window(self):
        self.label.setText(f"{self.quest_number}/10")
        self.pushButton_2.setText("Проверить ответ")
        text = self.cursor.execute(f"SELECT Question FROM Questions WHERE id={self.questions[self.quest_number - 1]}").fetchone()
        set_text = f"Вопрос №{self.quest_number + 1}. {text[0]}"
        self.textBrowser.setText(set_text)
        answers = self.cursor.execute(f"SELECT id, Answer FROM Answers WHERE Numer={self.questions[self.quest_number - 1]}").fetchall()
        random.shuffle(answers)
        self.radioButton.setText(answers[0][1])
        self.radioButton_2.setText(answers[1][1])
        self.radioButton_3.setText(answers[2][1])
        self.radioButton_4.setText(answers[3][1])
        self.slovar[self.radioButton.text()] = answers[0][0]
        self.slovar[self.radioButton_2.text()] = answers[1][0]
        self.slovar[self.radioButton_3.text()] = answers[2][0]
        self.slovar[self.radioButton_4.text()] = answers[3][0]

    def check_and_next(self):
        if self.quest_number < 10:
            text = self.pushButton_2.text()
            if text == "Проверить ответ":
                self.quest_number += 1
                true_answ_id = self.cursor.execute(f"SELECT True_Answer FROM Questions WHERE id={self.questions[self.quest_number - 1]}").fetchone()
                if not self.button_group_ans.checkedButton():
                    self.statusbar.showMessage("Вопрос пропущен")
                    self.statusBar().setStyleSheet("background-color: pink")
                    self.none_answer += 1
                elif true_answ_id[0] == self.slovar[self.button_group_ans.checkedButton().text()]:
                    self.statusbar.showMessage("Верно")
                    self.statusBar().setStyleSheet("background-color: white")
                    self.true_answer += 1
                else:
                    self.statusbar.showMessage("Неверно")
                    self.statusBar().setStyleSheet("background-color: pink")
                    self.false_answer += 1
                self.pushButton_2.setText("Следующий вопрос")
            elif text == "Следующий вопрос":
                self.statusbar.clearMessage()
                self.statusBar().setStyleSheet("background-color: transparent")
                self.button_group_ans.setExclusive(False)
                self.radioButton.setChecked(False)
                self.radioButton_2.setChecked(False)
                self.radioButton_3.setChecked(False)
                self.radioButton_4.setChecked(False)
                self.update_window()
        else:
            try:
                self.close_lec_and_time(3)
            except Exception as e:
                print(e)

    def end_test(self):
        try:
            self.setEnabled(False)
            self.timer.stop()
            # передаем все необходимые штуки из бд
            print(self.pop)
            self.ResWin = ResWindow(self.FIO, self.id, self.group, self.pop, self.quest_number, self.true_answer, self.false_answer, self.none_answer)
            self.workWin.update_statistics()
            self.ResWin.show()
            # self.close()
        except Exception as e:
            print(e)


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
            self.check = 0

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
            self.radioButton_8.setChecked(True)

            self.button_group_color.addButton(self.radioButton)
            self.button_group_color.addButton(self.radioButton_2)
            self.button_group_color.addButton(self.radioButton_3)
            self.button_group_color.addButton(self.radioButton_4)
            self.radioButton.setChecked(True)

            self.button_group_gradus.buttonToggled[QtWidgets.QAbstractButton, bool].connect(self.change_picture)
            self.button_group_color_left.buttonToggled[QtWidgets.QAbstractButton, bool].connect(self.change_picture)
            self.button_group_eye.buttonToggled[QtWidgets.QAbstractButton, bool].connect(self.change_picture)

            self.canvas = MyMplCanvas(self, self.check)
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
    def __init__(self, win, check):
        self.fig = Figure()
        self.win = win
        self.check = check
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
            self.check += 1
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
        try:
            if self.check == 0:
                pass
            else:
                color = self.win.ret_color()

                x, y = self.pins[color]
                # Сделаем заливку графика
                self.ax.fill(x, y, color=color, alpha=0.1)

                # Обновим рисунок
                self.ax.set_thetagrids(np.arange(0.0, 360.0, 30.0))
                self.ax.set_rgrids(np.arange(0, 100, 10))
                self.draw()
        except Exception as e:
            print(e)


class RegistrationWindow(QMainWindow, Ui_RegMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect("BD_TSDO.db")
        self.cur = self.connection.cursor()
        self.pushButton.clicked.connect(self.push)

    def push(self):
        self.FIO = self.lineEdit.text()
        self.group = self.lineEdit_2.text()

        if not self.FIO or not self.group:
            self.statusbar.showMessage("Заполните оба поля!")
        else:
            try:
                check_id = self.cur.execute(f"""SELECT id FROM Students WHERE FIO='{self.FIO}' AND gruppa='{self.group}'""").fetchone()
                check_ids = self.cur.execute(f"""SELECT id FROM Students""").fetchall()
                if check_id in check_ids:
                    print(2222222)
                else:
                    self.cur.execute(f"""INSERT INTO Students (FIO, gruppa)
                                     VALUES ('{self.FIO}', '{self.group}')""")
            except Exception as e:
                print(e)
            self.connection.commit()
            self.id = self.cur.execute(f"""SELECT id FROM Students
                                           WHERE FIO='{self.FIO}'
                                           AND gruppa='{self.group}'""").fetchone()
            self.id = self.id[0]
            self.secondWin = WorkWindow(self.FIO, self.group, self.id, self.connection)
            self.secondWin.show()
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegistrationWindow()
    ex.show()
    sys.exit(app.exec())

