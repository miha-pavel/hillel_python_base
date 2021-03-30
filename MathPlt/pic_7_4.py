# Пример 7.4 Мультиокна разных размеров. Gridspec
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

import utils as utl


import matplotlib.gridspec as gridspec

# 3,3 - три столбца и три ячейки

ax = plt.subplot2grid((3, 1), (0, 0))

print(type(ax))

# это запись эквивалентна более детальной записи

gs = gridspec.GridSpec(3, 1)

ax = plt.subplot(gs[0, 0])
ax.grid(True)
# Положение текста задано в относительных координатах
ax.text(0.3, 0.5, u'Метод Gridspec', fontsize=14, transform=ax.transAxes)
utl.save(name='pic_7_4_a', fmt='png')


fig = plt.figure()

ax1 = plt.subplot2grid((2,2), (0, 0))
ax2 = plt.subplot2grid((2,2), (0, 1))
ax3 = plt.subplot2grid((2,2), (1, 0))
ax4 = plt.subplot2grid((2,2), (1, 1))

i = -1
jj = [0, 0, 1, 1]
kk = [0, 1, 0, 1]
for ax in fig.axes:
    i += 1
    stext = 'ax%d - %d, %d' % (i+1, jj[i], kk[i])
    ax.text(0.4, 0.5, stext, color='b')
    ax.grid(True)
utl.save(name='pic_7_4_b', fmt='png')


fig = plt.figure()

# Сетка состоит из 4 строк и 3 столбцов. Первая ячейка имеет номер (0,0),
# а последняя - (3,2)
egrid = (4,3)
ax1 = plt.subplot2grid(egrid, (0, 0), colspan=3)
ax2 = plt.subplot2grid(egrid, (1, 0), rowspan=2)
ax3 = plt.subplot2grid(egrid, (1, 1), rowspan=2, colspan=2)
ax4 = plt.subplot2grid(egrid, (3, 0), colspan=2)
ax5 = plt.subplot2grid(egrid, (3, 2))

for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center", 
                color='red', transform=ax.transAxes)
        ax.grid(True)

# Настройка расстояний между границами созданных subplots
plt.tight_layout()
utl.save(name='pic_7_4_c', fmt='png')


# Левая граница subplots на рисунке
rcParams['figure.subplot.left'] = 0.1
# Правая граница subplots на рисунке
rcParams['figure.subplot.right'] = 0.95
# Нижняя граница subplots на рисунке
rcParams['figure.subplot.bottom'] = 0.05
# Верхняя граница subplots на рисунке
rcParams['figure.subplot.top'] = 0.95

# Изменение параметров wspace и hspace методом rcParams

# Общая высота (вертикаль), выделенная для свободного пространства между subplots
rcParams['figure.subplot.hspace'] = 0.2
# Общая ширина (горизонталь), выделенная для свободного пространства между subplots
rcParams['figure.subplot.wspace'] = 0.2

N = 50
x = np.arange(N)
y = np.random.rand(np.size(x))

fig = plt.figure()

# Сетка состоит из 4 строк и 3 столбцов. Первая ячейка имеет номер (0,0),
# а последняя - (3,2)
egrid = (4,3)
ax1 = plt.subplot2grid(egrid, (0, 0), colspan=3)
ax2 = plt.subplot2grid(egrid, (1, 0), rowspan=2)
ax3 = plt.subplot2grid(egrid, (1, 1), rowspan=2, colspan=2)
ax4 = plt.subplot2grid(egrid, (3, 0), colspan=2)
ax5 = plt.subplot2grid(egrid, (3, 2))

for i, ax in enumerate(fig.axes):
        ax.plot(x, y, 'k')
        ax.text(0.2, 0.75, "ax%d" % (i+1), va="center", ha="center", 
                color='blue', transform=ax.transAxes, fontsize='large')
        ax.grid(True)

# Изменение параметров wspace и hspace методом fig.subplots_adjust()
fig.subplots_adjust(wspace=0.4, hspace=0.4)
utl.save(name='pic_7_4_d', fmt='png')

plt.show()
