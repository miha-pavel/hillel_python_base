# set_ = {1,2,3,4,5,6}
# dict_ = {}
# set_1 = set()
# print('set_1: ', set_1)
# print('type(set_1): ', type(set_1))



# Удаление дупликации
# fruits = ["apple", "banana", "cherry", "apple", "cherry", "apple"]
# print(fruits)
# set_fr = set(fruits)
# new_list = list(set_fr)
# print('new_list: ', new_list)


# print(dir(set()))


# Множество неповторяющяяся python коллекция
# fruits = {"apple", "banana", "cherry", "apple"}
# print(fruits)


# Єлементи множества должни бить не изменяеми
# type(set_1) = {"abc", 34, True, 40, "male"}
# print('set_1: ', set_1)

# set_1 = {"abc", 34, True, 40.5, set()}
# set_1 = {"abc", 34, True, 40.5, {}}
# set_1 = {"abc", 34, True, 40.5, []}
# print('set_1: ', set_1)


# # Генерирование множества
# df = {}
# print('df: ', df)
# print('type(df): ', type(df))
# set_1 = {'jack', 'sjoerd'}
# print('set_1: ', set_1)
# print('type(set_1): ', type(set_1))
# set_2 = {c for c in 'abracadabra' if c not in 'abc'}
# print('set_2: ', set_2)
# set_3 = set()
# print('set_3: ', set_3)
# set_4 = set('foobar')
# print('set_4: ', set_4)
# s_1 = {'a', 'b', 'foo'}
# set_5 = set(s_1)
# print('set_5: ', set_5)
# print('type(set_5): ', type(set_5))


# Получить єлемент множества
# fruits = {"apple", "banana", "cherry"}
# fruits[0]

# fruits = {"apple", "banana", "cherry"}
# for x in fruits:
#     print(x)

# fruits = {"apple", "banana", "cherry"}
# print("banana" in fruits)


# Добавление єлементов
# fruits = {"apple", "banana", "cherry"}
# fruits.add("orange")
# print(fruits)
# fruits = {"apple", "banana", "cherry"}
# fruits.add("cherry")
# print(fruits)


# # Удаление єлементов множества
# fruits = {"apple", "banana", "cherry"}
# fruits.remove("banana")
# print(fruits)
# # Если удаляемый элемент не существует, метод remove () вызовет ошибку.
# fruits.remove("banana")
# print(fruits)
# # Если удаляемый элемент не существует, метод discard () НЕ выдаст ошибку.
# print(fruits)
# fruits.discard("banana")
# print(fruits)


# Наборы неупорядочены, поэтому при использовании метода pop() вы не знаете, какой элемент будет удален.
# fruits = {"apple", "banana", "cherry"}
# x = fruits.pop()
# print('fruits: ', fruits)
# print(x)
# print(fruits)
# fruits = {"apple", "banana", "cherry"}
# fruits.clear()
# print(fruits)
# fruits = {"apple", "banana", "cherry"}
# del fruits
# print(fruits)


# # Копирование множества
# fruits = {"apple", "banana", "cherry"}
# x = fruits
# print('id(x): ', id(x))
# print('id(fruits): ', id(fruits))

# fruits = {"apple", "banana", "cherry"}
# x = fruits.copy()
# print(x)
# print('id(x): ', id(x))
# print('id(fruits): ', id(fruits))

# fruits = {"apple", "banana", "cherry"}
# x = set(**fruits)
# print(x)
# print('id(x): ', id(x))
# print('id(fruits): ', id(fruits))


# Обновление другим множеством
fruits = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
fruits.update(tropical)
print('fruits: ', fruits)
fruits = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
fruits|=tropical
print('fruits: ', fruits)
# # Объект в методе update() может бить не только множеством, это может быть любой повторяемый объект (кортежи, списки, словари и т. Д.).
fruits = {"apple", "banana", "cherry"}
tropical_list = ["kiwi", "orange"]
fruits.update(tropical_list)
print(fruits)

# Удаляет элементы в этом наборе, которых нет в другом, указанном наборе (х)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print('x: ', x)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x&=y
print(x)

# # Удаляет элементы из этого набора, которые также включены в другой указанный набор.
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# # Удалите элементы, которые есть в обоих наборах:
# x.difference_update(y)
# print(x)
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# # Удалите элементы, которые есть в обоих наборах:
# y.difference_update(x)
# print(y)
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# # Удалите элементы, которые есть в обоих наборах:
# x-=y
# print(x)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.symmetric_difference_update(y)
# print(x)
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x^=y
# print(x)
# x = {"apple", "banana", "cherry"}
# y = {"apple", "banana", "cherry"}
# x^=y
# print(x)



# Обеденение двух и более множеств
# Вернуть набор, содержащий объединение наборов
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, "b", 3}
# set3 = set1.union(set2)
# print(set3)
# set3_ = set1|set2
# print('set3_: ', set3_)


# Пересичение
# Возвращает набор, являющийся пересечением двух других наборов.
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.intersection(y)
# print(z)
# z_ = x & y
# print('z_: ', z_)


# # Отличие
# # Возвращает набор, содержащий разницу между двумя или более наборами.
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# # Вернуть набор, содержащий элементы, которые существуют только в наборе x, но не в наборе y:
# z = x.difference(y)
# print(z)
# z_ = x - y
# print('z_: ', z_)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# # Вернуть набор, содержащий элементы, которые существуют только в наборе y, а не в наборе x:
# z = y.difference(x)
# print(z)
# z_ = y - x
# print('z_: ', z_)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y)
# print(z)
# z_ = x ^ y
# print('z_: ', z_)


# # Проверка на отличие
# # Возвращает, есть ли у двух наборов пересечение или нет.
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "facebook"}
# # Вернуть True, если в наборе y нет элементов в наборе x:
# z = x.isdisjoint(y)
# print(z)
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.isdisjoint(y)
# print('z: ', z)

# # Возвращает, содержит ли другой набор этот набор или нет
# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}
# # Вернуть True, если все элементы набора x присутствуют в наборе y:
# z = x.issubset(y)
# print(z)
# z_ = x<=y
# print('z_: ', z_)

# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b"}
# z = x.issubset(y)
# print(z)
# z_ = x<=y
# print('z_: ', z_)

# # Возвращает, содержит ли этот набор другой набор или нет
# x = {"f", "e", "d", "c", "b", "a"}
# y = {"a", "b", "c"}
# # Вернуть True, если все элементы набора y присутствуют в наборе x:
# z = x.issuperset(y)
# print(z)
# z_ = x>=y
# print('z_: ', z_)
# x = {"f", "e", "d", "c", "b"}
# y = {"a", "b", "c"}
# z = x.issuperset(y)
# print(z)
# z_ = x>=y
# print('z_: ', z_)


# Встроенние методи множеств
# Длина множества
# fruits = {"apple", "banana", "cherry"}
# print(len(fruits))

# all() метод
# Возвращает True, если все элементы набора истинны (или если набор пуст).
# all values true
# l = {1, 3, 4, 5}
# print(all(l))
# # all values false
# l = {0, False}
# print(all(l))
# # one false value
# l_0 = {1, 3, 4, 0}
# print('l_0: ', all(l_0))
# # one true value
# l = {1, False, 5}
# print(all(l))
# # empty iterable
# l = set()
# print('type(l): ', type(l))
# print(all(l))

# any() метод
# Возвращает True, если какой-либо элемент набора истинен. Если набор пуст, возвращает False.
# True since 1,3 and 4 (at least one) is true
# l = {1, 3, 4, 0}
# print(any(l))
# # False since both are False
# l = {0, False}
# print(any(l))
# # True since 5 is true
# l = {0, False, 5}
# print(any(l))
# # False since iterable is empty
# l = set()
# print(any(l))