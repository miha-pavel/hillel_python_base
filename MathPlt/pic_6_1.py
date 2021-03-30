# Пример 6.1.1 Контейнер Axes
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

import utils as utl


fig = plt.figure()

print(u'Список областей рисования после создания объекта fig %s \n' % fig.axes)

plt.scatter(0.,1.)

print(u'Список областей рисования после вызова комманды scatter %s \n' % fig.axes)

utl.save(name='pic_6_1_a', fmt='png')


x = [0,1,2,3,4,5,6,7,8,9,10]
y = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11]

fig = plt.figure()

# Первая область рисования (мультиокно 1)
ax = fig.add_subplot(211)
line = ax.plot(x, y, '-', color='blue', linewidth=2)
print('Lines on the axes:', type(line), line)

# Вторая область рисования (мультиокно 2)
ax2 = fig.add_subplot(212)
n, bins, rectangles = ax2.hist(np.random.randn(1000), 50, facecolor='yellow')
print('Patches on the axes:', len(ax2.patches), rectangles)

for ax in fig.axes:
    ax.grid(True)
utl.save(name='pic_6_1_b', fmt='png')

plt.show()
