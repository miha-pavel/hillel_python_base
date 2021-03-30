# Пример 4.2 Цветовая палитра colormap

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import utils as utl


dat = np.random.random(200).reshape(20,10) # создаём матрицу значений

# Создаём список цветовых палитр из словаря
maps = [m for m in plt.cm.datad]
# или так
maps = []

for i, m in enumerate(plt.cm.datad):
    maps.append(m)
#    print('%d - %s' % (i, m))

print(u'Предустановленные цветовые палитры:', maps)

fig, axes= plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)

cmaplist = plt.cm.datad

for ax in fig.axes:
    random_cmap = np.random.choice(maps)
    cf = ax.contourf(dat, cmap=plt.get_cmap(random_cmap))
    ax.set_title('%s colormap' % random_cmap)
    fig.colorbar(cf, ax=ax)
    
plt.suptitle(u'Различные цветовые палитры')   # единый заголовок рисунка
utl.save(name='pic_4_3', fmt='png')

plt.show()
