# Пример 4.2 Способы задания цветов. RGB и HEX

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import utils as utl


fig = plt.figure()
ax = fig.add_subplot(111)   # добавление области рисования ax

N = 10
x = np.arange(1, N+1, 1)
y = 20.*np.random.rand(N)

rgb = np.array([204, 255, 51])/255.
myhex = '#660099'

ax.plot(x, y, color=myhex)
ax.bar(x, y, color=rgb, alpha=0.75, align='center')

ax.set_xticks(x)   # установка делений на оси OX
ax.set_xlim(np.min(x)-1, np.max(x)+1)   # ограничение области изменения по оси OX
ax.grid(True)
utl.save(name='pic_4_2', fmt='png')

plt.show()
