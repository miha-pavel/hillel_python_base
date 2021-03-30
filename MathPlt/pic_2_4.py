# Пример 2.4 Методы отображений
import matplotlib.pyplot as plt
import utils as utl
import numpy as np


dat = np.random.random(200).reshape(20, 10) # создаём матрицу значений

fig = plt.figure()
cr = plt.contour(dat) 
plt.colorbar(cr)
plt.title('Simple contour plot')
utl.save(name='pic_2_4_a', fmt='png')

fig = plt.figure()
cf = plt.contourf(dat) 
plt.colorbar(cf)
plt.title('Simple contourf plot')
utl.save(name='pic_2_4_b', fmt='png')

fig = plt.figure()
cf = plt.matshow(dat) 
plt.colorbar(cf, shrink=0.7)
plt.title('Simple matshow plot')
utl.save(name='pic_2_4_c', fmt='png')

plt.show()