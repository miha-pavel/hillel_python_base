import random as rnd


# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.
rand_list = [rnd.randint(1, 100) for _ in range(20)]
print('rand_list: ', rand_list)

# 2) Создать словарь triangle в который записать точки A B C (ключи), и их координаты - кортежи (значения),
# созданные случайным образом с помощью модуля random в диапазоне от -10 до 10 по каждой оси.
list_before = [rnd.randint(-10, 10) for _ in range(2)]
print('list_before: ', list_before)
vertex  = ["A", "B", "C", "D"]
triangle = {key: tuple(rnd.randint(-10, 10) for _ in range(2)) for key in vertex}
print("triangle", triangle)

# 3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
my_str = "I'm the string"
# Печатает ***I'm the string***

def my_print(my_str: str):
    """Print changed string:

    Args:
        my_str (str): The string before changing.
    """
    print(f"***{my_str}***")

my_str = "I'm the string"
my_print(my_str=my_str)

my_print = lambda my_str : print(f'***{my_str}***')
my_print(my_str)
my_str = "dsfdstry"
my_print(my_str)

# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
persons = [
    {"name": "John", "age": 35},
    {"name": "Bob", "age": 19},
    {"name": "Jack", "age": 15},
    {"name": "Thomas", "age": 45},
    {"name": "Richard", "age": 25},
    {"name": "Richird", "age": 15}
    ]

# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
min_age = min(person["age"] for person in persons)
[print(person["name"]) for person in persons if person["age"]==min_age]
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
longest_name = max(len(person["name"]) for person in persons)
[print(person["name"]) for person in persons if len(person["name"])==longest_name]
# в) Посчитать среднее количество лет всех людей из списка.
avr = sum(person["age"] for person in persons)/len(persons)
print('avr: ', avr)

my_print = lambda condition : [print(person["name"]) for person in persons if condition]
my_print(person["age"] == min_age)
my_print(len(person["name"]) == longest_name)

my_print = lambda condition : [print(person["name"]) for person in persons if eval(condnition)]
my_print('person["age"]==min_age')
my_print('len(person["name"])==longest_name')

# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

my_dict_1 = {"a": 1, "b":87, "c":3, "d":4}
print('my_dict_1.items(): ', my_dict_1.items())
my_dict_2 = {"t1": 1, "b":2, "e":5, "c":89}
print('my_dict_2.items(): ', my_dict_2.items())
# а) Создать список из ключей, которые есть в обоих словарях.
intersection_keys = list(set(my_dict_1.keys()).intersection(my_dict_2.keys()))
print('intersection_keys: ', intersection_keys)
intersection_keys = list(my_dict_2.keys() & my_dict_1.keys())
print('intersection_keys &: ', intersection_keys)
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
difference_keys = list(set(my_dict_1.keys()).difference(my_dict_2.keys()))
print('difference_keys: ', difference_keys)
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
new_dict = {key: my_dict_1[key] for key in difference_keys}
print('new_dict: ', new_dict)

unique_keys_in_dicts = list(set(my_dict_1.keys()).difference(my_dict_2.keys())) + list(set(my_dict_2.keys()).difference(my_dict_1.keys()))
print('unique_keys_in_dicts: ', unique_keys_in_dicts)
unique_keys_in_dicts = list(my_dict_1.keys() ^ my_dict_2.keys())
print('unique_keys_in_dicts ^: ', unique_keys_in_dicts)

unique_dict1 = {key: value for key, value in my_dict_1.items() if key in unique_keys_in_dicts}
print('unique_dict1: ', unique_dict1)
unique_dict2 = {key: value for key, value in my_dict_2.items() if key in unique_keys_in_dicts}
print('unique_dict2: ', unique_dict2)
common_keys_dict = {key: [my_dict_1[key], my_dict_1[key]] for key in intersection_keys}
print('common_keys_dict: ', common_keys_dict)
merge_dict = {**unique_dict1, **unique_dict2, **common_keys_dict}
print('merge_dict: ', merge_dict)
intersection = dict(my_dict_1.items() & my_dict_2.items())
print('intersection: ', intersection)
union = dict(my_dict_1.items() | my_dict_2.items())
print('union: ', union)
difference = dict(my_dict_1.items() ^ my_dict_2.items())
print('difference: ', difference)

rand_list_1 = [rnd.randint(1, 100) for _ in range(20000000)]
# print('rand_list_1: ', rand_list_1)
rand_list_2 = [rnd.randint(1, 100) for _ in range(20000000)]
# print('rand_list_1: ', rand_list_1)
import time
now = time.time()
intersection = list(set(rand_list_1) & set(rand_list_2))
print('intersection: ', time.time()-now)

now = time.time()
intersection = list(set([x for x in rand_list_1 if x in rand_list_2]))
print('intersection: ', time.time()-now)
now = time.time()
intersection = list(set(filter(lambda x:x in rand_list_1, rand_list_2)))
print('intersection: ', time.time()-now)

now = time.time()
intersection = list(set(rand_list_1).intersection(set(rand_list_2)))
print('intersection: ', time.time()-now)