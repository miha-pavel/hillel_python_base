# Пример 5.2 Конфигурация Figure
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

import utils as utl


figsize = (8,6)

fig = plt.figure(figsize=figsize, facecolor='pink', frameon=True)
plt.plot([[0.0, 0.0],[1., 1.]], 'k')
plt.grid(True)
rcParams['figure.edgecolor'] = 'blue'
utl.save(name='pic_5_2_a', fmt='png')


rcParams['font.family'] = 'Times New Roman', 'Arial', 'Tahoma'
rcParams['font.fantasy'] = 'Times New Roman'
# Изменение параметров рисования (смена чёрного по белому на белое по чёрному)
facecolor = 'k'
rcParams['figure.edgecolor'] = facecolor
rcParams['figure.facecolor'] = facecolor
rcParams['axes.facecolor'] = facecolor
#rcParams['axes.edgecolor'] = 'k'
rcParams['grid.color'] = 'w'
rcParams['xtick.color'] = 'w'
rcParams['ytick.color'] = 'w'
rcParams['axes.labelcolor'] = 'w'

x = np.arange(0, 4*np.pi, 0.12)
y = np.tan(x)

fig = plt.figure()
plt.plot(x, y,'w')

plt.xlim(x[0], x[-1])
plt.ylim(np.min(y), np.max(y))

plt.xlabel(u'Время [c]', fontsize=12)
plt.ylabel(u'Амплитуда [м]', fontsize=12)
plt.grid(True, color='w')
utl.save(name='pic_5_2_b', fmt='png')


def sm2inch(a):
    '''
    Converts inches to santimeters
    '''
    b = []
    for i in a:
        b.append(i/2.54)
    return b

# Возвращаем обычные значения цветов для дальнейшей интерактивной работы

rcParams['figure.edgecolor'] = 'w'
rcParams['figure.facecolor'] = 'w'
rcParams['axes.facecolor'] = 'w'
rcParams['axes.edgecolor'] = 'k'
rcParams['grid.color'] = 'k'
rcParams['xtick.color'] = 'k'
rcParams['ytick.color'] = 'k'
rcParams['axes.labelcolor'] = 'k'

figsize = (3.5, 2.5) # см
figsize = sm2inch(figsize)
print(figsize)
fig2 = plt.figure(figsize=figsize, facecolor='w')
rcParams['figure.edgecolor'] = 'w'
plt.text(0.45, 0.45,'Hello, world!', color='red', fontsize=16)
plt.grid(True)

utl.save(name='pic_5_2_c', fmt='png')

plt.show()
