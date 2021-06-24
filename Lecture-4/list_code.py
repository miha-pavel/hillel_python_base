# fruits = []
# print('fruits: ', fruits)
# fruits = list()
# print('fruits: ', fruits)
fruits = ['apple', 'banana', 'melon', 'pineapple']
# print('fruits: ', fruits)
# fruits = [1, 'banana', 10.0, [1, 2, 3], {1:'w', 2:'r'}, None]
# fruits = [1, 'banana', 10.0, 1, [1, 2, 3], [1,2,3], {1:'w', 2:'r'}, None]
# print('fruits: ', fruits[0])
# print('fruits: ', fruits[1])
# print('fruits: ', fruits[2])
# print('fruits: ', fruits)


# print('='*50)
# print('DIR - какие методы существуют для класс (инструкции) list')
print('dir(list): ', dir(list()))

# some_list = list()
# print('some_list: ', some_list)
# print('type(some_list): ', type(some_list))
# some_list = []
# print('some_list: ', some_list)
# print('type(some_list): ', type(some_list))

# print('='*50)
# print('INDEX - полоучить индекс элемента')
# index_melon = fruits.index('melon')
# print('index_melon: ', index_melon)
# fruits = [4, 55, 64, 32, 16, 32]
# x_index = fruits.index(32)
# print('x_index: ', x_index)

# print('='*50)
# print('ПОЛОЖИТЕЛЬНЫЕ ИНДЕКСЫ')
fruits = ['apple', 'banana', 'melon', 'pineapple']
# print('fruits[3]: ', fruits[0])
# print('fruits[3]: ', fruits[3])
# print('fruits[0:3]: ', fruits[0:3])
# print('fruits[:3]: ', fruits[:3])
# print('fruits[1:3]: ', fruits[1:3])
# print('fruits[1:]: ', fruits[1:])
# i = 1
# print('fruits[0]: ', fruits[i*2])

# print('='*50)
# print('ОТРИЦАТЕЛЬНИЙ ИНДЕКСЫ')
# fruits = ['apple', 'banana', 'melon', 'pineapple']
# print('fruits[-1]: ', fruits[-1])
# print('fruits[-3]: ', fruits[-3])
# print('fruits[:-3]: ', fruits[:-3])
# print('fruits[-4:-1]: ', fruits[-4:-1])
# print('fruits[-4:]: ', fruits[-4:])

# print('='*50)
# print('ЦИКЛ СКВОЗЬ СПИСОК')
# for fruit in fruits:
#     print(fruit)

# print('='*50)
# print('IN - ПРОВЕРКА О СУЩЕСТВОВАНИИ ЭЛЕМЕНТА В СПИСКЕ')
# fruits = ['apple', 'banana', 'melon', 'pineapple']
# fruit = "watermelon"
# print('fruit in fruits: ', fruit in fruits)
# if fruit in fruits:
#     print(f"Yes, {fruit} is in the fruits list")
# else:
#     print(f"No, {fruit} is not in the fruits list")

# print('='*50)
# print('LEN - ДЛИНА СПИСКА')
# print('Длина списка:', len(fruits))

# print('='*50)
# print('APPEND - ДОБАВЛЕНИЕ ЭЛЕМЕНТА В СПИСОК (в конец)')
# print('Список до обновления:', fruits)
# print('Длина списка до:', len(fruits))
# fruits.append("orange")
# print('Новый список:', fruits)
# print('Длина списка после:', len(fruits))

# updated_list = []
# fruits = [1, 'banana', '10.0', [1, 2, 3], None]
# for fruit in fruits:
#     if isinstance(fruit, str):
#         updated_list.append(fruit)
# print('updated_list: ', updated_list)

# Добовление в начало
# updated_list = ['er', 'sd', 'fg']
# fruits = [1, 'banana', '10.0', [1, 2, 3], None]
# for fruit in fruits:
#     if isinstance(fruit, str):
#         updated_list.reverse()
#         updated_list.append(fruit)
#         updated_list.reverse()
# print('updated_list: ', updated_list)
# Добовление в начало
# updated_list = ['er', 'sd', 'fg']
# fruits = [1, 'banana', '10.0', [1, 2, 3], None]
# for fruit in fruits:
#     if isinstance(fruit, str):
#         updated_list.insert(0, fruit)
# print('updated_list: ', updated_list)


# print('='*50)
# print('INSERT - ДОБАВЛЕНИЕ ЭЛЕМЕНТА В СПИСОК')
# print('Список до обновления:', fruits)
# print('Длина списка до:', len(fruits))
# fruits.insert(1, "watermelon")
# print('Новый список:', fruits)
# print('Длина списка после:', len(fruits))

# print('='*50)
# print('REMOVE - УДАЛЕНИЕ ЭЛЕМЕНТА В СПИСОК')
# print('Список до обновления:', fruits)
# print('Длина списка до:', len(fruits))
# fruits.remove("banana")
# print('Новый список:', fruits)
# print('Длина списка после:', len(fruits))

# print('='*50)
# print('POP - УДАЛЕНИЕ ЭЛЕМЕНТА ИЗ КОНЦА СПИСКА')
# print('Список до обновления:', fruits)
# print('Длина списка до:', len(fruits))
# pop_2 = fruits.pop(2)
# print('pop_2: ', pop_2)
# # print('Удаленный элемент:', fruits.pop(2))
# print('Новый список:', fruits)
# print('Длина списка после:', len(fruits))

# print('='*50)
# print('DEL - УДАЛЕНИЕ ЭЛЕМЕНТА ПО ИНДЕКСУ')
# print('Список до обновления:', fruits)
# print('Длина списка до:', len(fruits))
# del fruits[2]
# print('Новый список:', fruits)
# print('Длина списка после:', len(fruits))
# print('='*50)
# print('DEL - УДАЛЕНИЕ СПИСКА')
# print('Список до обновления:', fruits)
# print('Длина списка до:', len(fruits))
# del fruits
# print('Новый список:', fruits)
# print('Длина списка после:', len(fruits))

# print('='*50)
# print('CLEAR - ОЧИСТКА СПИСКА')
# fruits = ['apple', 'banana', 'melon', 'pineapple']
# print('Список до обновления:', fruits)
# print('Длина списка до:', len(fruits))
# fruits.clear()
# print('Новый список:', fruits)
# print('Длина списка после:', len(fruits))

# print('='*50)
# print('COUNT - как много элементов в списке')
# fruits = ['apple', 'pineapple', 'banana', 'melon', 'pineapple']
# pineapple_count = fruits.count('pineapple')
# print('pineapple_count:', pineapple_count)

# print('='*50)
# print('MIN MAX списка')
# list1 = [1, 3, 4, 56, 7, 8, 6]
# print('min of list: ', min(list1))
# print('max of list: ', max(list1))

# list1 = ['1', '3', '4', '56', '7', '8']
# print('min of list: ', min(list1))
# print('max of list: ', max(list1))


# print('='*50)
# print('КОПИРОВАНИЕ СПИСКА')
# print('='*50)
# print('ПРИСВАИВАНИЕ НОВОМУ СПИСКУ')
# fruits = ['apple', 'banana', 'melon', 'pineapple']
# print('Список до обновления:', fruits)
# print('Длина списка до:', len(fruits))
# new_fruits = fruits
# print('new_fruits: ', new_fruits)
# fruits.append('watermelon')
# print('fruits: ', fruits)
# print('new_fruits: ', new_fruits)
# print('id_fruits: ', id(fruits))
# print('id_new_fruits: ', id(new_fruits))
# print('is id new_fruits and id fruits True: ', id(new_fruits) == id(fruits))
# print('fruits: ', id(fruits[0]))
# print('id_new_fruits: ', id(new_fruits[0]))
# print('is id new_fruits[0] and id fruits[0] True: ', id(new_fruits[0]) == id(fruits[0]))
# fruits.append('sd')
# print('fruits: ', fruits)
# print('new_fruits: ', new_fruits)

# print('='*50)
# print('КОПИРОВАНИЕ СПИСКА')
# print('='*50)
# print('ПРИСВАИВАНИЕ НОВОМУ СПИСКУ')
# fruits = ['apple', 'banana', 'melon', 'pineapple']
# print('Список до обновления:', fruits)
# print('Длина списка до:', len(fruits))
# new_fruits = fruits[:]
# print('new_fruits: ', new_fruits)
# fruits.append('watermelon')
# print('fruits: ', fruits)
# print('new_fruits: ', new_fruits)
# print('id_new_fruits: ', id(new_fruits))
# print('id_fruits: ', id(fruits))
# print('is id new_fruits and id fruits True: ', id(new_fruits) == id(fruits))
# print('fruits: ', id(fruits[0]))
# print('id_new_fruits: ', id(new_fruits[0]))
# print('is id new_fruits[0] and id fruits[0] True: ', id(new_fruits[0]) == id(fruits[0]))

# print('='*50)
# print('COPY')
# fruits = ['apple', 'banana', 'melon', 'pineapple']
# print('Список до обновления:', fruits)
# print('Длина списка до:', len(fruits))
# new_fruits = fruits.copy()
# print('Новый список:', new_fruits)
# print('Длина списка после:', len(new_fruits))
# print('id fruits: ', id(fruits))
# print('id new_fruits: ', id(new_fruits))
# print('is id new_fruits and id fruits True: ', id(new_fruits) == id(fruits))
# print('id fruits[0]: ', id(fruits[0]))
# print('id new_fruits[0]: ', id(new_fruits[0]))
# print('is id new_fruits[0] and id fruits[0] True: ', id(new_fruits[0]) == id(fruits[0]))
# fruits.append('watermelon')
# print('fruits after append : ', fruits)
# print('new_fruits after append : ', new_fruits)

# print('='*50)
# print('LIST')
# fruits = ['apple', 'banana', 'melon', 'pineapple']
# print('Список до обновления:', fruits)
# print('Длина списка до:', len(fruits))
# new_fruits = list(fruits)
# print('Новый список:', new_fruits)
# print('Длина списка после:', len(new_fruits))
# print('id fruits: ', id(fruits))
# print('id new_fruits: ', id(new_fruits))
# print('is id new_fruits and id fruits True: ', id(new_fruits) == id(fruits))
# print('id fruits[0]: ', id(fruits[0]))
# print('id new_fruits[0]: ', id(new_fruits[0]))
# print('is id new_fruits[0] and id fruits[0] True: ', id(new_fruits[0]) == id(fruits[0]))
# fruits.append('watermelon')
# print('fruits after append : ', fruits)
# print('new_fruits after append : ', new_fruits)

# print('='*50)
# print('SPRED generator')
# fruits = ['apple', 'banana', 'melon', 'pineapple']
# print('Список до обновления:', fruits)
# print('Длина списка до:', len(fruits))
# new_fruits = [*fruits]
# print('Новый список:', new_fruits)
# print('Длина списка после:', len(new_fruits))
# print('id fruits: ', id(fruits))
# print('id new_fruits: ', id(new_fruits))
# print('is id new_fruits and id fruits True: ', id(new_fruits) == id(fruits))
# print('id fruits[0]: ', id(fruits[0]))
# print('id new_fruits[0]: ', id(new_fruits[0]))
# print('is id new_fruits[0] and id fruits[0] True: ', id(new_fruits[0]) == id(fruits[0]))
# fruits.append('watermelon')
# print('fruits after append : ', fruits)
# print('new_fruits after append : ', new_fruits)

# print('='*50)
# print('COPY.COPY')
# fruits = ['apple', 'banana', 'melon', 'pineapple']
# print('Список до обновления:', fruits)
# print('Длина списка до:', len(fruits))
# import copy
# new_fruits = copy.copy(fruits)
# print('Новый список:', new_fruits)
# print('Длина списка после:', len(new_fruits))
# print('id fruits: ', id(fruits))
# print('id new_fruits: ', id(new_fruits))
# print('id new_fruits is id fruits: ', id(new_fruits) == id(fruits))
# print('id fruits[0]: ', id(fruits[0]))
# print('id new_fruits[0]: ', id(new_fruits[0]))
# print('id new_fruits[0] is id fruits[0]: ', id(new_fruits[0]) == id(fruits[0]))
# fruits.append('watermelon')
# print('fruits after append : ', fruits)
# print('new_fruits after append : ', new_fruits)
# fruits[0] = 'watermelon'
# print('fruits after append : ', fruits)


# print('='*50)
# print('COPY.DEEPCOPY')
# fruits = ['apple', 'banana', 'melon', ['pineapple', 'pear']]
# print('Список до обновления:', fruits)
# import copy
# new_fruits = copy.deepcopy(fruits)
# print('Новый список:', new_fruits)
# print('id fruits: ', id(fruits))
# print('id new_fruits: ', id(new_fruits))
# print('id new_fruits is  id fruits: ', id(new_fruits) == id(fruits))
# print('id fruits[0]: ', id(fruits[0]))
# print('id new_fruits[0]: ', id(new_fruits[0]))
# print('id new_fruits[0] is  id fruits[0]: ', id(new_fruits[0]) == id(fruits[0]))
# print('id fruits[3]: ', id(fruits[3]))
# print('id new_fruits[3]: ', id(new_fruits[3]))
# print('id new_fruits[3] is  id fruits[3]: ', id(new_fruits[3]) == id(fruits[3]))
# print('id fruits[3][0]: ', id(fruits[3][0]))
# print('id new_fruits[3][0]: ', id(new_fruits[3][0]))
# print('id new_fruits[3][0] is  id fruits[3][0]: ', id(new_fruits[3][0]) == id(fruits[3][0]))
# fruits.append('watermelon')
# print('fruits after append : ', fruits)
# print('new_fruits after append : ', new_fruits)
# fruits[0] = 'watermelon'
# print('fruits after append : ', fruits)
# print('new_fruits after append : ', new_fruits)

# [] - # list
# () - # tuple
# {} - # dict, set


# print('='*50)
# print('ОБЕДЕНЕНИЕ ДВУХ СПИСКОВ')
# print('='*50)
# print('КАНКАТЕНАЦИЯ')
# list1 = ["a", "b", "c"]
# list2 = [8, 2, 3]
# list3 = list1 + list2
# print('Новый список:', list3)
# print('list3:', id(list3))
# print('list1:', id(list1))
# print('list2:', id(list2))
# print('id(list1[0]): ', id(list1[0]))
# print('id(list3[0]): ', id(list3[0]))
# print('id(list1[0]) is id(list3[0]): ', id(list1[0]) == id(list3[0]))
# print('id(list2[0]): ', id(list2[0]))
# print('id(list3[3]): ', id(list3[3]))
# print('id(list2[0]) is id(list3[3]): ', id(list2[0]) == id(list3[3]))

# print('='*50)
# print('EXTEND')
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# print('id(list1): ', id(list1))
# # list1.extend(list2)

# list1.extend(list2)
# list3 = list1
# print('list3: ', list3)
# print('list1: ', list1)
# print('list3: ', list3)
# print('Новый список list1:', list1)
# print('id(list1): ', id(list1))
# print('id(list3): ', id(list3))
# print('id(list1[3]): ', id(list1[3]))
# print('id(list2[0]): ', id(list2[0]))
# print('id(list1[3]) is id(list2[0]): ', id(list1[3]) == id(list2[0]))

# print('='*50)
# print('FOR loop')
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# for x in list2:
#     list1.append(x)
# print('Новый список list1:', list1)
# print('id(list1[3]): ', id(list1[3]))
# print('id(list2[0]): ', id(list2[0]))
# print('id(list1[3]) is id(list2[0]): ', id(list1[3]) == id(list2[0]))
# list2.pop()
# print('list2: ', list2)
# print('Новый список list1:', list1)

# new_fruits = []
# fruits = ['abra', 'apple', 'banana', 'melon', 'pineapple']
# for fruit in fruits:
#     new_fruits.append(fruit.startswith('ap'))
# print('Новый список new_fruits:', new_fruits)


# print('='*50)
# print('РЕВЕРСИРОВАНИЕ списка')
# print('='*50)
# print('REVERSE')
# fruits = ['apple', 'banana', 'cherry']
# fruits.reverse()
# print('reversed_fruits:', fruits)

# print('='*50)
# print('Срезы')
# fruits = ['apple', 'banana', 'cherry']
# reversed_fruits = fruits[::-1]
# print('reversed_fruits:', reversed_fruits)

# print('='*50)
# print('CОРТИРОВКА СПИСКА')
# print('='*50)
# # list.sort(reverse=True|False, key=myFunc)
# print('SORT')
# cars = ['Ford', 'BMW', 'Volvo']
# cars.sort()
# print('cars: ', cars)

# print('='*50)
# print('Cортировка списка c реверссом')
# cars = ['Ford', 'BMW', 'Volvo']
# cars.sort(reverse=True)
# print('cars: ', cars)

# print('='*50)
# print('Cортировка списка по ключу - длина элемента')
# def myFunc(e):
#     return len(e)
# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
# cars.sort(key=myFunc)
# print('cars: ', cars)

# print('='*50)
# print('Cортировка списка по ключу - длина элемента и реверсом')
# def myFunc(e):
#     return len(e)
# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
# cars.sort(reverse=True, key=myFunc)
# print('cars: ', cars)

# print('='*50)
# print('Cортировка списка словорей по ключу')
# def myFunc(e):
#     return e['year']
# cars = [
#     {'car': 'Ford', 'year': 2005},
#     {'car': 'Mitsubishi', 'year': 2000},
#     {'car': 'BMW', 'year': 2019},
#     {'car': 'VW', 'year': 2011}
# ]
# cars.sort(key=myFunc)
# print('cars: ', cars)


fruits = [1,'abra', 2, None, {1,2,3,4}, 10.45, 3, 'pineapple']
new_fruits = []
for fruit in fruits:
    if isinstance(fruit, int):
        new_fruits.append(fruit**3)
print('Новый список new_fruits:', new_fruits)

new_fruits = [fruit**3 for fruit in fruits if isinstance(fruit, int)]
print('Новый список new_fruits:', new_fruits)

# print('='*50)
# print('LIST COMPREHENSION')
list1 = [1, 3, 4, 56, 7, 8, 25]
new_list = [i**2 for i in list1]
print('new_list: ', type(new_list))
print('new_list: ', new_list)

even_list = [i for i in list1 if i % 2 == 0]
print('even_list: ', even_list)

squer_even_list = [i**2 for i in list1 if i % 2 == 0]
print('squer_even_list: ', squer_even_list)

bad_lists = ['Adobe', 'Audience', 'Manager', 'Ds', 'This', 'There', 'These']
filter_list = ['This', 'Ds', 'There', 'These']
result_list = [i for i in bad_lists if i not in filter_list]
print('result_list: ', result_list)


a=3
b=4
c=5
print(f'''В элементе dsTGgNDXZrI ------===> {a} символов
В элементе dGJhYUrpJOCLfRnh ------===> {b} символов
В элементе gtyMw ------===> {c} символов''')


print('В элементе dsTGgNDXZrI ------===> 0 символов a В элементе dGJhYUrpJOCLfRnh ------===> 0 символов a В элементе snjUSrs ------===> 0 символов a В элементе gtyMw ------===> 0 символов a ')