import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import csv

data_names = ['Киев', 'Харьков', 'Львов', 'Одесса',
              'Днепр', 'Ивано-Франковск', 'Николаев', 'Запорожье',
              'Черновцы', 'Суммы']
data_values = [1076, 979, 222, 189, 137, 134, 124, 124, 91, 79]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 9})

plt.title('Распределение кафе по городам Украины (%)')

xs = range(len(data_names))

plt.pie(
    data_values, autopct='%.1f', radius = 1.1,
    explode = [0.15] + [0 for _ in range(len(data_names) - 1)] )
plt.legend(
    bbox_to_anchor = (-0.16, 0.45, 0.25, 0.25),
    loc = 'lower left', labels = data_names )
fig.savefig('MathPlt/img/pie.png')