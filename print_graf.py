import numpy as np
import pylab
import pyqtgraph


def onMouseClick(event):
    axes = event.inaxes

    # Если кликнули вне какого-либо графика, то не будем ничего делать
    if axes is None:
        return

    # В качестве текущих выберем оси, внутри которых кликнули мышью
    pylab.sca(axes)

    # Координаты клика в системе координат осей
    a = event.xdata
    b = event.ydata

    x.append(a)
    y.append(b)
    # Выведем точку, куда кликнули
    pylab.plot(a, b, 'bo')

    # Выведем график из точек
    pylab.plot(x, y, color='blue', linewidth=2)

    # Сделаем заливку графика
    pylab.fill(x, y, color='blue')

    # Обновим рисунок
    ax.set_thetagrids(np.arange(0.0, 360.0, 30.0))
    ax.set_rgrids(np.arange(0, 100, 10))
    pylab.draw()


if __name__ == '__main__':
    fig = pylab.figure()
    # Добавление на рисунок круговой области рисования
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
    ax.set_thetagrids(np.arange(0.0, 360.0, 30.0))
    ax.set_rgrids(np.arange(10, 100, 10))
    x = []
    y = []

    # Подписка на событие
    fig.canvas.mpl_connect('button_press_event', onMouseClick)

    pylab.show()
