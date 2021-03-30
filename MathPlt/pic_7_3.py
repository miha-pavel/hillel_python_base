# Пример 7.3 Автоматизированное создание мультиокон
import matplotlib.pyplot as plt
import numpy as np

import utils as utl


fig, subplots = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)

x = np.arange(20)

i = -1
for ax in fig.axes:
    i += 1
    y = np.random.rand(np.size(x))
    ax.grid(True)
    ax.text(0.5, 0.9, str(i+1), color='red')
    ax.plot(x, y)
    if((i+1)%2 == 0):
        ax.tick_params(axis='y', labelleft='off', labelright='on', left=False, right=True)
    if((i==0) or (i==1)):
        ax.tick_params(axis='x', labelbottom='off', labeltop='off', left=False, right=True)     
    if((i==1) or (i==2)):
        ax.tick_params(axis='y', labelleft='off', labelright='off', left=False, right=False)
    if(i==3):
        ax.tick_params(axis='x', labelbottom='off', labeltop='off')        
    if(i==1):
        ax.tick_params(axis='x', labelbottom='off', labeltop='on')
    if(i==0):
        ax.tick_params(axis='y', left=True, right=False)

# Параметры подобраны эмпирически, на глаз
plt.tight_layout(h_pad = -0.15, w_pad = -0.2)
utl.save(name='pic_7_3', fmt='png')

plt.show()
