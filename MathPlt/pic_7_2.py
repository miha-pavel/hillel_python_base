# Пример 7.2 Близкое расположение областей рисования
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

import utils as utl


fig = plt.figure()

ax1 = fig.add_subplot(211)
ax1.set_title(u'Две области слиплись')
ax2 = fig.add_subplot(212)

# Чтобы подписи осей координатных сеток не сливались разнесём их
# в разные стороны - одну оставим слева, а другую вынесем направо
ax1.tick_params(axis='x', labelbottom='off', labeltop='off') 
ax2.tick_params(axis='y', labelleft='off', labelright='on', left=False, right=True)
# Узнаём координаты областей, которые занимают subplots
print(u'Область 1', ax1)
print(type(ax1))
print(u'Область 2', ax2)

# Нарисуем в каждом subplot линию сетки

for ax in fig.axes:
    ax.grid(True)

# Параметр подобран эмпирически, на глаз. Это скверно

plt.tight_layout(h_pad = -0.88)
utl.save(name='pic_7_2_a', fmt='png')


fig = plt.figure()

N = 100
x = np.arange(N)
y = np.random.random(N)*30.

# Область ax1 нарисуется первой
ax1 = fig.add_axes([0., 0., 1.0, 1.0]) 
# Область ax2 перекроет область ax1 и закроет её часть
ax2 = fig.add_axes([0.5, 0.5, 0.5, 0.5])

rect0 = [0.0, 0.0]

ax1.plot(rect0, 'r')
ax1.plot(x, y, 'green')

ax2.plot(rect0, 'c')
ax2.hist(y, 20, edgecolor='k', facecolor='r')
ax2.tick_params(axis='y', which='major', direction='inout',
                left=True, right=True, labelleft=False, labelright=True)
ax2.tick_params(axis='x', which='major', direction='inout',
                bottom=True, top=True, labelbottom=False, labeltop=True)

print(u'Область 1', ax1)
print(type(ax1))
print(u'Область 2', ax2)

for ax in fig.axes:
    ax.grid(True)
utl.save(name='pic_7_2_a', fmt='png')

plt.show()
