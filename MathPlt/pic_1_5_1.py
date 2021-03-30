# Пример 1.5.1 # Элементы простого рисунка 
import matplotlib.pyplot as plt
import utils as utl
import numpy as np


lag = 0.1
x = np.arange(0.0, 2*np.pi+lag, lag)
y = np.cos(x)

fig = plt.figure()
plt.plot(x, y)

plt.text(np.pi-0.5, 0,  '1 Axes', fontsize=26, bbox=dict(color='w'))
plt.text(0.1, 0, '3 Yaxis', fontsize=18, bbox=dict(color='w'), rotation=90)
plt.text(5, -0.9, '2 Xaxis', fontsize=18, bbox=dict(color='w'))

plt.title('1a TITLE')
plt.ylabel('3a Ylabel')
plt.xlabel('2a Xlabel ')

plt.text(5, 0.85, '6 Xticks', fontsize=12, bbox=dict(color='w'), rotation=90)
plt.text(0.95, -0.55, '6 Xticks', fontsize=12, bbox=dict(color='w'), rotation=90)

plt.text(5.75, -0.5, '7 Yticks', fontsize=12, bbox=dict(color='w'))
plt.text(0.15, 0.475, '7 Yticks', fontsize=12, bbox=dict(color='w'))

plt.grid(True)

utl.save(name='pic_1_5_1', fmt='png')

plt.show()