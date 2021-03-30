# Пример 4.4 Плавная цветовая палитра

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import utils as utl


dat = np.random.random(200).reshape(20,10) # создаём матрицу значений

# Создаём список цветовых палитр из словаря
maps = [m for m in plt.cm.datad]
# или так
maps = []
for m in plt.cm.datad:
    maps.append(m)

fig, axes= plt.subplots(nrows=2, ncols=1, sharex=True)   # смотри главу "Рисунки с несколькими областями рисования"

cmaplist = plt.cm.datad

for i, ax in enumerate(fig.axes):
    random_cmap = np.random.choice(maps)
    if(i == 0):
        cf = ax.pcolor(dat, cmap=plt.get_cmap(random_cmap))
    else:
        cf = ax.imshow(dat, cmap=plt.get_cmap(random_cmap))        

    ax.set_title('%s colormap' % random_cmap)
    
    fig.colorbar(cf, ax=ax)

plt.suptitle(u'Различные цветовые палитры')
utl.save(name='pic_4_4_a', fmt='png')


dat = np.random.random(200).reshape(20,10) # создаём матрицу значений

xx = np.array([0.5, 0.0, 0.1])*255
print(xx)
# Создаём список цветовых палитр из словаря

# ---------------------------------------------------------
# Вариант 1 Ромашка (бело-жёлтый)

cdict1 = {'red':   ((0.0, 1.0, 1.0),
                   (1.0, 1.0, 1.0)),

         'green': ((0.0, 1.0, 1.0),
                   (1.0, 1.0, 1.0)),

         'blue':  ((0.0, 1.0, 1.0),
                   (1.0, 0.0, 0.0))
        }

cmap1 = mpl.colors.LinearSegmentedColormap('cmap1', cdict1)

# Вариант 2 Светофор(красный-жёлтый-зелёный)
cdict2 = {'red':   ((0.0, 0.0, 0.0),
                   (0.5, 1.0, 1.0),
                   (1.0, 1.0, 1.0)),

         'green': ((0.0, 1.0, 1.0),
                   (0.5, 1.0, 1.0),
                   (1.0, 0.0, 0.0)),

         'blue':  ((0.0, 0.0, 0.0),
                   (0.5, 0.0, 0.0),
                   (1.0, 0.0, 0.0))
        }
cmap2 = mpl.colors.LinearSegmentedColormap('cmap2', cdict2)
# ---------------------------------------------------------

fig, axes= plt.subplots(nrows=2, ncols=1, sharex=True)

cmaplist = plt.cm.datad

cmaps = [cmap1, cmap2]

for i, ax in enumerate(fig.axes):
    cf = ax.imshow(dat, cmap=cmaps[i])        
    fig.colorbar(cf, ax=ax)

plt.suptitle(u'Создание цветовых палитр')

utl.save(name='pic_4_4_b', fmt='png')


# розовый [255, 204, 255] -> [1., 0.8, 1.]
# фиолетовый [153, 0, 255] -> [0.6, 0., 1.]
# синий [0, 0, 255] -> [0., 0., 1.]
# красный [255, 0, 0] -> [1., 0., 0.]

cdict1 = {'red':   ((0.0, 1.0, 1.0), # red in RGB of pink, розовый
                   (0.2, 0.6, 0.6), # red in RGB of blue синий 
                   (0.8, 0.0, 0.0),  # red in RGB of violet фиолетовый 
                   (1.0, 1.0, 1.0)),  # red in RGB of red красный  

         'green':  ((0.0, 0.8, 0.8), # green in RGB of pink, розовый
                   (0.2, 0.0, 0.0), # green in RGB of blue синий 
                   (0.8, 0.0, 0.0), # green in RGB of violet фиолетовый 
                   (1.0, 0.0, 0.0)), # green in RGB of red красный  

         'blue':  ((0.0, 1.0, 1.0), # blue in RGB of pink, розовый
                   (0.2, 1.0, 1.0), # blue in RGB of blue синий 
                   (0.8, 1.0, 1.0), # blue in RGB of violet фиолетовый
                   (1.0, 0.0, 0.0)) # blue in RGB of red красный  
          }

cmap1 = mpl.colors.LinearSegmentedColormap('cmap1', cdict1)
plt.register_cmap(cmap=cmap1)
# ---------------------------------------------------------

fig = plt.figure()

ax = fig.add_subplot(111)

cmaplist = plt.cm.datad

cf = ax.pcolor(dat, cmap=cmap1)        
cbar = fig.colorbar(cf, ax=ax)
plt.suptitle(u'Розово-сине-фиолетово-красная палитра')

utl.save(name='pic_4_4_c', fmt='png')


# Пример 4.4.4 - взят с http://schubert.atmos.colostate.edu/~cslocum/custom_cmap.html

'''
NAME
    Custom Colormaps for Matplotlib
PURPOSE
    This program shows how to implement make_cmap which is a function that
    generates a colorbar.  If you want to look at different color schemes,
    check out https://kuler.adobe.com/create.
PROGRAMMER(S)
    Chris Slocum
REVISION HISTORY
    20130411 -- Initial version created
    20140313 -- Small changes made and code posted online
    20140320 -- Added the ability to set the position of each color
    20150503 -- Shabanov P.A.: added debug parameter
'''

def make_cmap(colors, position=None, bit=False, debug=False):
    '''
    make_cmap takes a list of tuples which contain RGB values. The RGB
    values may either be in 8-bit [0 to 255] (in which bit must be set to
    True when called) or arithmetic [0 to 1] (default). make_cmap returns
    a cmap with equally spaced colors.
    Arrange your tuples so that the first color is the lowest value for the
    colorbar and the last is the highest.
    position contains values from 0 to 1 to dictate the location of each color.
    '''
    import matplotlib as mpl
    import numpy as np
    bit_rgb = np.linspace(0,1,256)
    if position == None:
        position = np.linspace(0,1,len(colors))
    else:
        if len(position) != len(colors):
            sys.exit("position length must be the same as colors")
        elif position[0] != 0 or position[-1] != 1:
            sys.exit("position must start with 0 and end with 1")
    if(debug):
        print('position:', position)
        print('len colors', len(colors))
        
    if bit:
        for i in range(len(colors)):
            colors[i] = (bit_rgb[colors[i][0]],
                         bit_rgb[colors[i][1]],
                         bit_rgb[colors[i][2]])
    if(debug):
        print('colors', colors)
    cdict = {'red':[], 'green':[], 'blue':[]}
    for pos, color in zip(position, colors):
        cdict['red'].append((pos, color[0], color[0]))
        cdict['green'].append((pos, color[1], color[1]))
        cdict['blue'].append((pos, color[2], color[2]))

    if (debug): 
        print('red', cdict['red'])
        print('green', cdict['green'])
        print('blue', cdict['blue'])

        
    cmap = mpl.colors.LinearSegmentedColormap('my_colormap',cdict,256)
    return cmap

### An example of how to use make_cmap
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(311)
### Create a list of RGB tuples
# 'r', 'y', 'w', 'g', 'b'
colors = [(255, 0, 0), (255, 255, 0), (255, 255, 255), (0, 157, 0), (0, 0, 255)] # This example uses the 8-bit RGB
### Call the function make_cmap which returns your colormap
my_cmap = make_cmap(colors, bit=True)
### Use your colormap
plt.pcolor(np.random.rand(25,50), cmap=my_cmap)
plt.colorbar()

ax = fig.add_subplot(312)
colors = [(1,1,1), (0.5,0,0)] # This example uses the arithmetic RGB
### If you are only going to use your colormap once you can
### take out a step.
plt.pcolor(np.random.rand(25,50), cmap=make_cmap(colors))
plt.colorbar()

ax = fig.add_subplot(313)
colors = [(0.4,0.2,0.0), (1,1,1), (0,0.3,0.4)]
### Create an array or list of positions from 0 to 1.
position = [0, 0.3, 1]
plt.pcolor(np.random.rand(25,50), cmap=make_cmap(colors, position=position))
plt.colorbar()
utl.save(name='pic_4_4_d', fmt='png')

plt.show()
