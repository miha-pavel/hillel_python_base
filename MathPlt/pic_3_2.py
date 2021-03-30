# Пример 3.2 Текст на рисунке
import matplotlib.pyplot as plt
import numpy as np

import utils as utl


a = 1.
x = np.arange(-2*np.pi, 2*np.pi, 0.05)
# Уравнение кардиоиды
xz = a*(2*np.cos(x) - np.cos(2*x))
yz = a*(2*np.sin(x) - np.sin(2*x))

fig = plt.figure()
plt.plot(xz, yz)

# Текст в координатах данных
str1 = plt.text(-np.pi/2., np.pi/2., 'Text in absolute coords', fontsize=14)   # выравнивание по левому краю
print('Text class: %s' % str1.__class__)

# Текст в рамке
plt.text(0.5, 0.5, 'Text with borders', fontsize=14,
         # выравнивание по вертикали и по горизонтали по центру
         horizontalalignment='center', verticalalignment='center',
         bbox=dict(facecolor='pink', alpha=0.5))

# Текст в относительных координатах области рисования ax
ax = fig.add_subplot(111)   # создаём область рисования ax
plt.text(0.5, 0.5, 'Text in relative coords', fontsize=14,
         horizontalalignment='right', verticalalignment='center',
         transform=ax.transAxes)
plt.grid()
utl.save(name='pic_3_2', fmt='png')

plt.show()