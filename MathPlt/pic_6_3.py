# Пример 6.2 Создание областей рисования
import matplotlib.pyplot as plt
import numpy as np

import utils as utl


x = np.arange(20)
y = np.exp(-x)*np.sin(x)

fig = plt.figure()

# Обычный график в декартовых координатах
ax = fig.add_subplot(121, polar=False)
ax.plot(x, y, 'r')
rect = ax.patch 
rect.set_facecolor('green')
ax.grid(True)

# График в полярных координатах
ax2 = fig.add_subplot(122, polar=True)
ax2.plot(x, y, 'g')
rect = ax2.patch  # Круговой
rect.set_facecolor('red')
utl.save(name='pic_6_3', fmt='png')

plt.show()
