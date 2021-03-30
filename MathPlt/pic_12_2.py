# Пример 12.1 Легенда
import matplotlib.pyplot as plt
from random import randint, choice
import numpy as np
from matplotlib import rcParams
import matplotlib.gridspec as gridspec

import utils as utl


x = np.arange(-2*np.pi, 2*np.pi, 0.2)

fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True)

# Обрати внимание!
rborder = 0.75
rcParams['figure.subplot.right'] = rborder
rcParams['figure.subplot.hspace'] = 0.15
rcParams['figure.subplot.wspace'] = 0.15

lns = []
for i, ax in enumerate(fig.axes):
    y = np.sin(x)*randint(1, 5)
    line = ax.plot(x, y, label = u'График %d' % i, color=choice(['r','b','k','g']))
    if i > 1:
        ax.set_xlabel(u'Аргумент')
    if i%2 == 0:
        ax.set_ylabel(u'Функция %d' % i)
    ax.grid(True, color='grey')
    ax.set_title(u'subplot %d' % i)
    lns = lns + line

ax2 = fig.add_axes([rborder, 0.6, 1.-rborder, 0.15], frameon=False)
labs = [l.get_label() for l in lns]
ax2.legend(lns, labs, loc=3, frameon=True)
# Скрываем координатные оси
ax2.set_axis_off()
utl.save(name='pic_12_2_a', fmt='png')


x = np.arange(-2*np.pi, 2*np.pi, 0.2)
fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True)
# Обрати внимание!
rborder = 0.75
rcParams['figure.subplot.right'] = rborder
rcParams['figure.subplot.hspace'] = 0.15
rcParams['figure.subplot.wspace'] = 0.15
lns = []
for i, ax in enumerate(fig.axes):
    y = np.sin(x)*randint(1, 5)
    z = np.cos(x)*randint(1, 5)
    bar1 = ax.bar(x, y, width=0.4, label = u'Диаграмма %d-1' % i, color=choice(['r','b','pink','violet']))
    print('%d Тип данных bar' % i, type(bar1), bar1)
    bar2 = ax.bar(x, z, width=0.4, label = u'Диаграмма %d-2' % i, color=choice(['k','g','w','cyan']))
    if i > 1:
        ax.set_xlabel(u'Аргумент')
    if i%2 == 0:
        ax.set_ylabel(u'Функция %d' % i)
    ax.grid(True, color='grey')
    ax.set_title(u'subplot %d' % i)
    # Сравни с предыдущим примером
    lns.append(bar1)
    lns.append(bar2)
    
ax2 = fig.add_axes([rborder, 0.35, 1.-rborder, 0.5], frameon=False)
#lns
#print type(lns), type(lns[0]), lns[0] 
labs = [l.get_label() for l in lns]
ax2.legend(lns, labs, loc=3, frameon=True)
# Скрываем координатные оси области рисования ax2
ax2.set_axis_off()
utl.save(name='pic_12_2_b', fmt='png')

plt.show()
