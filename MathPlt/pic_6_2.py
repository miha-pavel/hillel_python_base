# Пример 6.2 Создание областей рисования
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

import utils as utl


fig = plt.figure()

x = np.arange(20)
y = np.exp(-np.sin(x))

x0 = 0.05
y0 = 0.05
dx = 0.9
dy = 0.9

rect = [x0, y0, dx, dy]
ax = fig.add_axes(rect)
ax.plot(x, y, 'g')
ax.text(7.5, 0.25, u'Зелёный график', color='g')
ax.grid(True)
# В отличие от интерфейса pyplot, команды для назначения подписей 
# нужно употреблять с приставкой set_
ax.set_title(u'Метод add_axes')
ax.set_xlabel(u'Ось абсцисс')
ax.set_ylabel(u'Ось ординат')
print('Тип ax: %s' % type(ax))
utl.save(name='pic_6_2_a', fmt='png')


fig = plt.figure()

x = np.arange(20)
y = np.exp(-np.sin(x))

ax = fig.add_subplot(111)
ax.plot(x, y, 'g')
ax.text(7.5, 0.25, u'Зелёный график', color='g')
ax.grid(True)

# В отличие от интерфейса pyplot, команды для назначения подписей 
# нужно употреблять с приставкой set_

ax.set_title(u'Метод add_subplot')
ax.set_xlabel(u'Ось абсцисс')
ax.set_ylabel(u'Ось ординат')

print('Тип ax: %s' % type(ax))
utl.save(name='pic_6_2_a', fmt='png')

plt.show()
