# # Импорты
# import time
# import pygame as p
# import random
# from pygame.locals import *

# # Константы цветов RGB
# BLACK = (0 , 0 , 0)
# WHITE = (255 , 255 , 255)
# # Создаем окно
# root = p.display.set_mode((500 , 500))
# # 2х мерный список с помощью генераторных выражений
# cells = [[random.choice([0 , 1]) for j in range(root.get_width() // 20)] for i in range(root.get_height() // 20)]


# # Функция определения кол-ва соседей
# def near(pos: list , system=[[-1 , -1] , [-1 , 0] , [-1 , 1] , [0 , -1] , [0 , 1] , [1 , -1] , [1 , 0] , [1 , 1]]):
#     count = 0
#     for i in system:
#         if cells[(pos[0] + i[0]) % len(cells)][(pos[1] + i[1]) % len(cells[0])]:
#             count += 1
#     return count


# # Основной цикл
# while 1:
#     # Заполняем экран белым цветом
#     root.fill(WHITE)

#     # Рисуем сетку
#     for i in range(0 , root.get_height() // 20):
#         p.draw.line(root , BLACK , (0 , i * 20) , (root.get_width() , i * 20))
#     for j in range(0 , root.get_width() // 20):
#         p.draw.line(root , BLACK , (j * 20 , 0) , (j * 20 , root.get_height()))
#     # Нужно чтобы виндовс не думал что программа "не отвечает"
#     for i in p.event.get():
#         if i.type == QUIT:
#             quit()
#     # Проходимся по всем клеткам

#     for i in range(0 , len(cells)):
#         for j in range(0 , len(cells[i])):
#             # print(cells[i][j],i,j)
#             p.draw.rect(root , (255 * cells[i][j] % 256 , 0 , 0) , [i * 20 , j * 20 , 20 , 20])
#     # Обновляем экран
#     p.display.update()
#     cells2 = [[0 for j in range(len(cells[0]))] for i in range(len(cells))]
#     for i in range(len(cells)):
#         for j in range(len(cells[0])):
#             if cells[i][j]:
#                 if near([i , j]) not in (2 , 3):
#                     cells2[i][j] = 0
#                     continue
#                 cells2[i][j] = 1
#                 continue
#             if near([i , j]) == 3:
#                 cells2[i][j] = 1
#                 continue
#             cells2[i][j] = 0
#     cells = cells2
# https://github.com/StanislavPetrovV/Python-Game-of-life/blob/master/main.py
import pygame
from random import randint
from copy import deepcopy

# Размери поверхности
RES = WIDTH, HEIGHT = 1500, 1000
# Размер ячейки
TILE = 10
W, H = WIDTH // TILE, HEIGHT // TILE
# Скорость итерации
FPS = 3

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()



next_field = [[0 for i in range(W)] for j in range(H)]
current_field = [[0 for i in range(W)] for j in range(H)]
current_field = [[1 if i == W // 2 or j == H // 2 else 0 for i in range(W)] for j in range(H)]
# current_field = [[randint(0, 1) for i in range(W)] for j in range(H)]
# current_field = [[1 if not i % 9 else 0 for i in range(W)] for j in range(H)] # 2,5,8,9,10,11,13,18,21,22,26,30,33,65
# current_field = [[1 if not (2 * i + j) % 4 else 0 for i in range(W)] for j in range(H)] # (2,4),(4,4)
# current_field = [[1 if not (i * j) % 22 else 0 for i in range(W)] for j in range(H)] # 5,6,9,22,33
# current_field = [[1 if not i % 7 else randint(0, 1) for i in range(W)] for j in range(H)]

def check_cell(current_field, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j][i]:
                count += 1

    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0


while True:
    # Создание рабочей поверхности и проверка поверхности на закритие
    surface.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    [pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
    [pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]
    
    # draw life
    for x in range(1, W - 1):
        for y in range(1, H - 1):
            if current_field[y][x]:
                pygame.draw.rect(surface, pygame.Color('forestgreen'), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
            next_field[y][x] = check_cell(current_field, x, y)

    current_field = deepcopy(next_field)

    print(clock.get_fps())
    pygame.display.flip()
    clock.tick(FPS)