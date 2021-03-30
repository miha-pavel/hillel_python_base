# Пример 12.1 Легенда
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
import matplotlib.gridspec as gridspec

import utils as utl


a = 1
x = np.arange(-2*np.pi, 2*np.pi, 0.2)
y = np.sin(x) * np.cos(x)
f = np.sin(x) + np.cos(x)
xz = a*(2*np.cos(x) - np.cos(2*x))
yz = a*(2*np.sin(x) - np.sin(2*x))
# Способ 1 с помощью label
plt.plot(x, f, label = u'Сумма cos и sin')
plt.scatter(x, y, label = u'Произведение cos и sin', color='r')
plt.plot(xz, yz, label = u'Кардиоида')
plt.grid(True)
plt.xlabel(u'Аргумент')
plt.ylabel(u'Функция')
plt.title(u'Несколько графиков')
plt.legend()   # легенда для всего рисунка fig
utl.save(name='pic_12_1_a', fmt='png')


a = 1
x = np.arange(-2*np.pi, 2*np.pi, 0.2)
y = np.sin(x) * np.cos(x)
f = np.sin(x) + np.cos(x)
xz = a*(2*np.cos(x) - np.cos(2*x))
yz = a*(2*np.sin(x) - np.sin(2*x))
fig = plt.figure()
fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True)
for i, ax in enumerate(fig.axes):
    ax.plot(x, f, label = u'Линия1 ax%d' % i)
    ax.scatter(x, y, label = u'Маркеры ax%d' % i, color='r')
    ax.plot(xz, yz, label = u'Линия2 ax%d' % i)
    ax.grid(True)
    ax.set_xlabel(u'Аргумент')
    ax.set_ylabel(u'Функция')
    ax.set_title(u'Несколько графиков')
    ax.legend(loc='best', frameon=False)   # легенда для области рисования ax
plt.tight_layout()
utl.save(name='pic_12_1_b', fmt='png')


rcParams['font.family'] = 'Times New Roman', 'Arial', 'Tahoma'
rcParams['font.fantasy'] = 'Times New Roman'
a = 1
x = np.arange(-2*np.pi, 2*np.pi, 0.2)
y = np.sin(x) * np.cos(x)
f = np.sin(x) + np.cos(x)
xz = a*(2*np.cos(x) - np.cos(2*x))
yz = a*(2*np.sin(x) - np.sin(2*x))
# Способ 2 с помощью label
plt.plot(x, f, 'b')
plt.scatter(x, y, color='b')
plt.bar(x, y, color='g', alpha=0.25)
plt.plot(xz, yz, 'r')
plt.scatter([-5., 6], [-2., -1], color='r')
plt.grid(True)
plt.xlabel(u'Аргумент')
plt.ylabel(u'Функция')
plt.title(u'Несколько графиков')
lab1 = u'cos + sin'
lab2 = u'cos * sin'
lab2_5 = u'диаграмма'
lab3 = u'Кардиоида'
lab4 = u'две точки'
plt.legend((lab1, lab3, lab2, lab4, lab2_5), frameon=False)

utl.save(name='pic_12_1_c', fmt='png')

plt.show()
