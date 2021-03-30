# Пример 2.1 Самые простые графические команды
import matplotlib.pyplot as plt
import utils as utl


fig = plt.figure()
# Добавление на рисунок прямоугольной (по умолчанию) области рисования
scatter1 = plt.scatter(0.0, 1.0)
print('Scatter: ', type(scatter1))

graph1 = plt.plot([-1.0, 1.0], [0.0, 1.0])
print('Plot: ', len(graph1), graph1)

text1 = plt.text(0.5, 0.5, 'Text on figure')
print('Text: ', type(text1))

grid1 = plt.grid(True)   # линии вспомогательной сетки

utl.save(name='pic_2_1', fmt='png')

plt.show()