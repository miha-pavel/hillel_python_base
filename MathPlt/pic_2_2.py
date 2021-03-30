# Пример 2.2 Диаграммы
import matplotlib.pyplot as plt
import utils as utl
import numpy as np


s = ['one','two','three ','four' ,'five']
x = [1, 2, 3, 4, 5]
z = np.random.random(100)
z1 = [10, 17, 24, 16, 22]
z2 = [12, 14, 21, 13, 17]

# bar()
fig = plt.figure()
plt.bar(x, z1)
plt.title('Simple bar chart')
plt.grid(True)   # линии вспомогательной сетки
utl.save(name='pic_2_2_a', fmt='png')

# hist()
fig = plt.figure()
plt.hist(z)
plt.title('Simple histogramm')
plt.grid(True)
utl.save(name='pic_2_2_b', fmt='png')

# pie()
fig = plt.figure()
plt.pie(x, labels=s)
plt.title('Simple pie chart')
utl.save(name='pic_2_2_c', fmt='png')

# boxplot()
fig = plt.figure()
plt.boxplot([z1, z2])
plt.title('Simple box whisker chart')
plt.grid(True)
utl.save(name='pic_2_2_d', fmt='png')

# errorbar()
fig = plt.figure()
plt.errorbar(x, z1, xerr=1, yerr=0.5)
plt.title('Simple error bar chart')
plt.grid(True)
utl.save(name='pic_2_2_e', fmt='png')

plt.show()