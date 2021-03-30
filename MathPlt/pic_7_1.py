# Пример 7.1 Методы создания мультиокон
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

import utils as utl


fig = plt.figure()

tri = 211
ax1 = fig.add_subplot(tri)
ax1.set_title(u'Область 1')
ax2 = fig.add_subplot(2, 1, 2)
ax2.set_title(u'Область 2')

# Узнаём координаты областей, которые занимают subplots
print(u'Область 1', ax1)
print(type(ax1))
print(u'Область 2', ax2)

# Нарисуем в каждом subplot линию сетки
for ax in fig.axes:
    ax.grid(True)
utl.save(name='pic_7_1_a', fmt='png')


fig = plt.figure()

# В примере для задания границ областей была использована информация
# о границах subplots из предыдущего примера

ax1 = fig.add_axes([0.125, 0.547727, 0.775, 0.352273]) 
ax1.set_title(u'Область 1')
ax2 = fig.add_axes([0.125, 0.125, 0.775, 0.352273]) 
ax2.set_title(u'Область 2')

# Узнаём координаты областей, которые занимают subplots
print(u'Область 1', ax1)
print(type(ax1))
print(u'Область 2', ax2)

# Нарисуем в каждом subplot линию сетки
for ax in fig.axes:
    ax.grid(True)
utl.save(name='pic_7_1_a', fmt='png')

plt.show()
