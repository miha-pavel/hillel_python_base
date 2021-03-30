# Пример 1.4.2 Различные по форме области рисования
import matplotlib.pyplot as plt
import utils as utl 


fig = plt.figure()
# Добавление на рисунок прямоугольной (по умолчанию) области рисования
ax = fig.add_axes([0, 0, 1, 1])
print (type(ax))
plt.scatter(1.0, 1.0)
utl.save('pic_1_4_1_a', fmt='png')


fig = plt.figure()
# Добавление на рисунок круговой области рисования
ax = fig.add_axes([0, 0, 1, 1], polar=True)
plt.scatter(0.0, 0.5)
utl.save(name='pic_1_4_1_b', fmt='png')
plt.show()