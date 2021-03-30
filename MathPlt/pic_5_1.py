# Пример 5.1 Дискретная цветовая палитра¶

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import utils as utl


fig = plt.figure()

print(type(fig))
# Создание экземпляра Axes c помощью Figure-метода add_subplot()
ax = fig.add_subplot(111)
# или так
box = [0.25, 0.5, 0.25, 0.25]
# Создание экземпляра Axes c помощью Figure-метода add_axes()
ax2 = fig.add_axes(box)

x = np.arange(0.0, 1.0, 0.1)
y = np.sin(x)*np.exp(x)
z = np.cos(x)*np.sin(x)

# Методы plot() вызываются через экземпляры ax, а не plt (интерфейс pyplot)
ax.plot(y)
ax.plot(z)

for ax in fig.axes:
    ax.grid(True)

utl.save(name='pic_5_1', fmt='png')
plt.show()
