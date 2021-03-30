# Пример 6.2 Создание областей рисования
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

import utils as utl


x = np.arange(10)
y = np.arange(-1, -11, -1)

fig = plt.figure()

ax = fig.add_subplot(211)
line = ax.plot(x, y, '-', color='blue', linewidth=2)
print('Lines:', type(line), line)

# Изменяем цвет подписей делений оси OX с помощью "set-get" технологии
for label in ax.get_xticklabels():
    label.set_color('orange')

ax2 = fig.add_subplot(212)
n, bins, rectangles = ax2.hist(np.random.randn(1000), bins=50, facecolor='yellow')
print('Patches:', len(ax2.patches), rectangles)

for ax in fig.axes:
    ax.grid(True)
utl.save(name='pic_6_4_a', fmt='png')


x = np.arange(10)
y = np.arange(-1, -11, -1)

fig = plt.figure()

ax = fig.add_subplot(211)
line = ax.plot(x, y, '-', color='blue', linewidth=2)
print('Lines:', type(line), line)

# Изменяем цвет подписей делений оси OX с помощью работы с контейнером XAxis
for label in ax.xaxis.get_ticklabels():
    label.set_color('red')
    label.set_rotation(-45)
    label.set_fontsize(12)

ax2 = fig.add_subplot(212)
n, bins, rectangles = ax2.hist(np.random.randn(1000), bins=50, facecolor='yellow')
print('Patches:', len(ax2.patches), rectangles)

for axes in fig.axes:
    axes.grid(True)
utl.save(name='pic_6_4_b', fmt='png')


rcParams['axes.grid'] = True
rcParams['axes.facecolor'] = 'orange'
rcParams['axes.labelcolor'] = 'red'
rcParams['axes.labelsize'] = 'large'
rcParams['axes.labelweight'] = 'bold'
k = 0.1
b = -0.7
x = np.arange(10)
y = k*x + b
fig = plt.figure()
ax = fig.add_subplot(111)
ax.barh(x, y)
ax.set_xlabel(u'Ось абсцисс')
ax.set_ylabel(u'Ось ординат')
ax.grid(True)
utl.save(name='pic_6_4_c', fmt='png')

plt.show()
