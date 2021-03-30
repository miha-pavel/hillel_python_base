# Генерирование tuple
# t = ()
# print('t: ', t)
# print('type(t): ', type(t))

# another_t = tuple()
# print('another_t: ', another_t)
# print('type(another_t): ', type(another_t))
# st = tuple('hello, world!')
# print('st: ', st)
# print('type(st): ', type(st))
# st = ('hello, world!')
# print('st: ', st)
# print('type(st): ', type(st))

# sd = st,
# print('sd: ', sd)
# print('type(sd): ', type(sd))

# t = (1, 2, 3, 4, 5)
# print('t: ', t)
# print('type(t): ', type(t))

# t = 1, 2, 3, 4, 5
# print('t: ', t)
# print('type(t): ', type(t))

# def some_function(a, b):
#     return a, b

# a = 1
# b = 2
# function_t = some_function(a, b)
# print('function_t: ', function_t)
# print('type(function_t): ', type(function_t))


# Кортеж неизменяемий обект
# t = (1, 2, 3, 4, 5)
# t[2] = 56
# Как можно изменить кортеж
# t = (1, 2, 3, 4, 5)
# print('t: ', id(t))
# l = list(t)
# print('l: ', l)
# print('type(l): ', type(l))
# l[2] = 56
# print('l: ', l)
# t = tuple(l)
# print('t: ', t)
# print('t: ', id(t))

# # Возможность дупликации
# fruits = ("banana", "cherry", "apple", "banana", "cherry")
# print('fruits: ', fruits)

# # Тип данних может бить любой
# tuple1 = ("abc", 34, True, 40.9, "male", None, [1, 3, 4])
# print('tuple1: ', tuple1)

# # Проблема одного єлемента
# t = (2)
# print('t: ', t)
# print('type(t): ', type(t))

# t = (2,)
# print('t: ', t)
# print('type(t): ', type(t))

# t = 2,
# print('t: ', t)
# print('type(t): ', type(t))

# def some_function(a):
#     b = 2
#     c = 3
#     return a, b, c
# a = 1
# # function_t = some_function(a)
# # print('function_t: ', function_t)
# # print('type(function_t): ', type(function_t))
# function_a, _, _ = some_function(a)
# print('_: ', _)
# print('type(_): ', type(_))
# print('function_a: ', function_a)
# print('type(function_a): ', type(function_a))

# # Лучшее представление кортежей
# t = (1,)
# print('t: ', t)
# print('type(t): ', type(t))
# l = [1, 2, 3, 4, 5, ]
# print('l: ', l)
# d = {'s': 1, 'w': 2, }
# print('d: ', d)


# # Упаковка єлементов кортежа
# t = ('foo', 'bar', 'baz', 'qux')
# (s1, s2, s3, s4) = t
# print('s1: ', s1)
# print('type(s1): ', type(s1))
# print('s2: ', s2)
# print('s3: ', s3)
# print('s4: ', s4)

# a = 'foo'
# b = 'bar'
# a, b = b, a
# print('a: ', a)
# print('b: ', b)

# Но может возникнуть проблеми нужно внимательно отслеживать количество обектов в кортеже
# t = ('foo', 'bar', 'baz')
# (s1, s2, s3, s4) = t

# _ = ''
# t = ('foo', 'bar', 'baz')
# (s1, s2, _) = t
# print('_: ', _)
# print('s2: ', s2)
# print('s1: ', s1)

# f_l = [1,2,3,45,6,]
# for f in f_l:
#     print(f)


# Использование спред оператора
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print('green: ', green)
# print('yellow: ', yellow)
# print('red: ', red)
# # или
# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# (green, *tropic, red) = fruits
# print('green: ', green)
# print('tropic: ', tropic)
# print('red: ', red)


# Действия с кортежами
print(dir(tuple()))
# Длина кортежа
fruits = ("apple", "banana", "cherry")
print(len(fruits))


# # Работа с индексами
# fruits = ("apple", "banana", "cherry")
# print(fruits[1])
# fruits = ("apple", "banana", "cherry")
# print(fruits[-1])
# fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon")
# print(fruits[2:5])
# fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon")
# print(fruits[:4])
# fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon")
# print(fruits[2:])
# fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon")
# print(fruits[-4:-1])
# fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon")
# print(fruits[1::2])
# # Реверс кортежа
# fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon")
# print(fruits[::-1])


# # Наличие єлемента в кортеже
fruits = ("apple", "banana", "cherry")
element = "apple"
if element in fruits:
    print(f'Yes, {element} is in the fruits tuple')
else:
    print(f'No, {element} is not in the fruits tuple')

# append
# fruits = ("apple", "banana", "cherry")
# fruits.append("orange") # This will raise an error
# print(fruits)

# fruits = ("apple", "banana", "cherry")
# y = list(fruits)
# y.append("orange")
# fruits = tuple(y)
# print('fruits: ', fruits)

# Удаление єлемента
# fruits = ("apple", "banana", "cherry")
# y = list(fruits)
# y.remove("apple")
# fruits = tuple(y)
# print('fruits: ', fruits)

# fruits = ("apple", "banana", "cherry")
# del fruits
# print(fruits) #this will raise an error because the tuple no longer exists


# Применение цикла
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)

# fruits = ("apple", "banana", "cherry")
# for i in range(len(fruits)):
#     print(fruits[i])

# fruits = ("apple", "banana", "cherry")
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i = i + 1

# Обеденение(канкатенация) кортежей
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print('tuple3: ', tuple3)
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = (*tuple1, *tuple2)


# fruits = ("apple", "banana", "cherry")
# double_fruits = fruits * 2
# print('double_fruits: ', double_fruits)

# # Встроенние методи кортежей
# _tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# tuple_count = _tuple.count(5)
# print('tuple_count: ', tuple_count)

# _tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# element = _tuple.index(8)
# print('element: ', element)

# tuple comprehension
# tc = tuple(i*2 for i in (1, 2, 3))
# print('tc: ', tc)
# print('type(tc): ', type(tc))
