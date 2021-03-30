# Пример 2.3 Методы изолиний
import matplotlib.pyplot as plt
import utils as utl
import numpy as np


dat = np.random.random(200).reshape(20, 10) # создаём матрицу значений

fig = plt.figure()
pc = plt.pcolor(dat) # метод псевдографики pcolor
plt.colorbar(pc)
plt.title('Simple pcolor plot')
utl.save(name='pic_2_3_a', fmt='png')

fig = plt.figure()
me = plt.imshow(dat) 
plt.colorbar(me)
plt.title('Simple imshow plot')
utl.save(name='pic_2_3_b', fmt='png')

plt.show()