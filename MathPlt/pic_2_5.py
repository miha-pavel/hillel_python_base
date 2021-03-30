# Пример 2.5 Методы заливки
import matplotlib.pyplot as plt
import utils as utl
import numpy as np


x = np.arange(0, 4*np.pi+0.1, 0.1)
y = np.sin(x)
z = np.sin(2*x)

x2 = np.arange(20)
y2 = -1.5*x2 + 2.33
z2 = 0.7*x2 - 8.5 

# fill()
fig = plt.figure()
plt.fill(x, y, 'r') # метод псевдографики pcolor
plt.title('Simple fill')
plt.grid(True)
utl.save(name='pic_2_5_a', fmt='png')

# fill_between()
fig = plt.figure()
plt.plot(x2, z2, color='pink', linewidth=4.0)
plt.plot(x2, y2, color='g', linewidth=4.0)
plt.fill_between(x2, y2, z2) 
plt.title('Simple fill_between')
plt.grid(True)
utl.save(name='pic_2_5_b', fmt='png')

# fill_betweenx()
fig = plt.figure()
plt.plot(z, x, color='pink', linewidth=4.0)
plt.plot(z, x-1.0, color='g', linewidth=4.0)
plt.fill_betweenx(z, x, x-1.0, color='cyan')
plt.title('Simple fill_betweenx')
plt.grid(True)
utl.save(name='pic_2_5_c', fmt='png')

plt.show()