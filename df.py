# Цикл While
# Задан некоторый список Aсодержащий целые числа. Используя инструкцию whileразработать программу,
# которая вычисляет сумму элементов списка.
a = range(0, 10)
i = 0
sum_ = 0
while i < len(list(a)):
    sum_ = sum_ + a[i]
    i = i + 1
print(sum_)

# Задано целое число k(1<k<365). Написать фрагмент кода, который определяет:
# каким будет k-й день года: выходной (суббота, воскресенье); какая будет дата (месяц и число).
# В программе использовать цикл while.
# по условиям задачи первй день начинается не с 1, а с 2 (k>1, не >=)и заканчивается 364 (так как 365 не включительно)

from random import randrange
k = randrange(2, 365)
print(k)
# входные данные
first_day = 5  # первый день года, 5 - пятница
print("Первый день недели в году: ", first_day)

# вспомогательный список - количество дней в месяцах года
MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# начальная инициализация перед вычислением
tk = 1  # текущее значение дня
tday = first_day  # текущий день недели
tmonth = 1  # текущий номер месяца
tday2 = 1  # текущий номер дня в месяце tmonth

# цикл while - вычисление
while tk < k:
    # перейти на следующий день
    tday = tday + 1
    tday2 = tday2 + 1
    tk = tk + 1

    # скорректировать день недели
    if tday > 7:
        tday = 1

    # скорректировать день месяца и номер месяца
    if tday2 > MONTHS[tmonth - 1]:
        tday2 = 1
        tmonth = tmonth + 1  # перейти на следующий месяц
print("--------------------")
print("Результат: ")
print("День недели: ", tday)
print("Номер месяца: ", tmonth)
print("Число: ", tday2)
print(
    'Вторую задачу сам решить не смог, воспользовался подскзкой интернета. Даже читая решения, по шагам разбираю, но сложно заходит')

# Задан список строк. В каждой строке подсчитать количество вхождений заданного символа
a = ['qwe', 'wsx', 'dsa', 'qsc']
b = str(input('введите символ: '))

i = 0
qty = 0
while i < len(a):
    print('В строке', a[i], 'вхождений символа', b, a[i].count(b), 'раз')
    i = i + 1

# Пользователь вводит число. Определение наличия заданного элемента в списке list_=[2,8,3,4,3,5,2,1,0,3,4,4,5,8,7,7,5].
# Если элемент не найден, то выводится соответствующее сообщение.
a = int(input('Ведите целое число:'))
list_ = [2, 8, 3, 4, 3, 5, 2, 1, 0, 3, 4, 4, 5, 8, 7, 7, 5]
i = 0
while i < len(list_):
    if a == list_[i]:
        print('Список содержит число:', a)
        break
    i += 1
else:
    print('Список НЕ содержит число:', a)

# ===============================
# Python Списки
# Заполнить список ста нулями, кроме первого и последнего элементов, которые должны быть равны единице;
a = [0]*100
a.append(1)
a.insert(0, 1)
print(a, type(a))

# Сформировать возрастающий список из чётных чисел (количество элементов 45);
b = list(range(2, 1000, 2))
b = b[0:45]
print(b)

# Но наверное это не тот способ, о котором просили. Решение через while
i = 0
res = [2]
while i < 44:
    res.append(res[i]+2)
    i += 1
print(res)

# Пользователь вводит число. Определить, содержит ли список данное число x.
# Вивести информационное сообщение содержит или не содержит ;
a = int(input('Ведите целое число:'))
i = 0
while i < len(res):
    if a == res[i]:
        print('Список содержит число:', a)
        break
    i += 1
else:
    print('Список НЕ содержит число:', a)


# # Найдите сумму и произведение элементов списка. Результаты вывести на экран;
# print(res)
# print(len(res))
i = 0
sum_ = 0
p = 1
while i < len(res):
    sum_ = sum_ + res[i]
    p = p * res[i]
    i += 1
print('Сумма элементов списка:', sum_, 'произведение элементов списка', p)

# # Найти наибольший элемент списка и вывести его на экран;
print('max =', max(res))

# Определите, есть ли в списке повторяющиеся элементы, если да, то вывести на экран это значение;
i = 0
while i < len(res):
    if res[i] in res[(i+1):]:
        print('повторяющийся элемент', res[i])
        break
    i += 1
else:
    print('повторяющиеся элементы отсутствуют')

# # Поменять местами самый большой и самый маленький элементы списка;
print('before', res)
min_res = min(res)
max_res = max(res)
res_min_i = res.index(min(res))
res_max_i = res.index(max(res))
res.remove(min(res))
res.remove(max(res))
res.insert(res_min_i, max_res)
res.insert(res_max_i, min_res)
print('after', res)


# Дан произвольный список. Представьте его в обратном порядке.
print('before reverse', res)
res.reverse()
print('after reverse', res)