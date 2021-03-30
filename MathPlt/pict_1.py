import matplotlib.pyplot as plt
import numpy as np
from random import randint


import numpy as np
test_data = np.genfromtxt('MathPlt/test_csv_data.csv', delimiter=',')
data = np.array(test_data)
# # print('data: ', data)
# plt.plot(data[:, 1], data[:, 0])
print('data[:, 0]: ', data[:, 0])
print('data[:, 1],: ', data[:, 1])
# fig = plt.figure()
# plt.plot(x, y, marker='v', color='red')
# plt.title('Наш график')
# plt.xlabel('Точки  абсцисы')
# plt.ylabel('Случайные точки ординаты')
# # plt.show()
# list_data = [70,  71,  72,  73,  74,  75,  76,  77,  78,  79,  80,  81,  82,  83,
#   84,  85,  86,  87,  88,  89,  90,  91,  92,  93,  94,  95,  96,  97,
#   98,  99, 100,]
# print('list_data: ', list_data[: 1])
