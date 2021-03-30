# Пример 4.4 Дискретная цветовая палитра¶

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import utils as utl


dat = np.random.random(200).reshape(20, 10) # создаём матрицу значений

N = 10
# Список цветов
cpool = [ '#bd2309', '#bbb12d', '#1480fa', '#14fa2f', '#000000',
          '#faf214', '#2edfea', '#ea2ec4', '#ea2e40', '#cdcdcd',
          '#577a4d', '#2e46c0', '#f59422', '#219774', '#8086d9' ]
# Создание дискретных colormap
cmap1 = mpl.colors.ListedColormap(['r','orange','y','g','c','b','violet'], 'indexed')
cmap2 = mpl.colors.ListedColormap(cpool[5:5+N], 'indexed')

#plt.register_cmap(cmap=cmap3)

fig, axes= plt.subplots(nrows=2, ncols=1, sharex=True)

cmaps = [cmap1, cmap2]

for i, ax in enumerate(fig.axes):
    cf = ax.pcolor(dat, cmap=cmaps[i])        
    fig.colorbar(cf, ax=ax)

fig.suptitle(u'Создание дискретных цветовых палитр')
utl.save(name='pic_4_5_a', fmt='png')


dat = np.random.random(200).reshape(20,10) # создаём матрицу значений

N = 10
# Список цветов в HEX формате
cpool = [ '#bd2309', '#bbb12d', '#1480fa', '#14fa2f', '#000000',
          '#faf214', '#2edfea', '#ea2ec4', '#ea2e40', '#cdcdcd',
          '#577a4d', '#2e46c0', '#f59422', '#219774', '#8086d9' ]

# Создание дискретных colormap
cmap1 = mpl.colors.ListedColormap(['r','orange','y','g','c','b','violet'], 'indexed')   # 7 цветов
cmap2 = mpl.colors.ListedColormap(cpool[5:5+N], 'indexed')   # 10 цветов

fig, axes= plt.subplots(nrows=2, ncols=1, sharex=True)

cmaps = [cmap1, cmap2]

for i, ax in enumerate(fig.axes):
    cf = ax.pcolor(dat, cmap=cmaps[i])        
    if(i == 0):
        fig.colorbar(cf, ax=ax, ticks=np.linspace(0, 1, 7+1))
    else:
        fig.colorbar(cf, ax=ax)
        
plt.suptitle(u'Создание дискретных цветовых палитр')

utl.save(name='pic_4_5_b', fmt='png')
plt.show()
