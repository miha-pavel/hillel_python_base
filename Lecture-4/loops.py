# txt = 'Hello Word'
# print('dir(txt): ', dir(txt))
# for leter in txt:
#     print(leter)

# txt = 'jhfdkjsaflhdshfkjzlxnsakjldhskf'
# for leter in txt:
#     if leter == 'f':
#         print(leter)

# txt = 'j5hf2143dkj5sa465flh5dshfkj7zlx6nsak9jldhs45kf'
# for leter in txt:
#     if leter.isnumeric():
#         print(leter)

# res = ''
# txt = 'j5hf2143dkj5sa465flh5dshfkj7zlx6nsak9jldhs45kf'
# for leter in txt:
#     if leter.isalpha():
#         res = res + leter
# print('res: ', res)
# dsaf = ''
# txt = 'j5hf2143dkj5sa465flh5dshfkj7zlx6nsak9jldhs45kf'
# for leter in txt:
#     if leter.isalpha():
#         dsaf += leter
# print('dsaf: ', dsaf)

# txt = 'jhfdkjsaflhdshfkjzlxnsakjldhskf'
# txt.upper()
# print('txt: ', txt)
# for leter in txt:
#     print('leter: ', leter)
# txt = 'jhfdkjsaflhdshfkjzlxnsakjldhskf'
# txt = txt.upper()
# print('txt: ', txt)
# for leter in txt:
#     print('leter: ', leter)

# # Oператор continue начинает следующий проход цикла, минуя оставшееся тело цикла
# txt = 'j5hf2143dkj5sa465flh5dshfkj7zlx6nsak9jldhs45kf'
# for leter in txt:
#     if leter.isalpha():
#         continue
#     print(int(leter) * 2, end='')


# # Oператор break досрочно прерывает цикл.
# txt = '23124dkj5sa465flh5dshfkj7zlx6nsak9jldhs45kf'
# for leter in txt:
#     if leter.isalpha():
#         break
#     print(leter * 2)

# Oператор else выполнится только в том случае, если выход из цикла произошел без помощи break
# leter = 'a'
# str_  = 'hello world'
# for item in str_:
#     print('before-item: ', item)
#     if item == leter:
#         print('after-item: ', item)
#         break
# else:
#     print(f'Буквы {leter} в строке {str_} нет')

# leter = 'o'
# for i in 'hello world':
#     if i == leter:
#         print('leter: ', leter)
#         break
# else:
#     print(f'Буквы {leter} в строке нет')
