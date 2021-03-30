import re

# 4.ОДНОСИМВОЛЬНЫЕ ШАБЛОНЫ
# Один любой символ, кроме новой строки \n.
# mach = re.findall(pattern, string)
# print(re.findall(r"м.л.ко", "молоко, малако, Им0л0коИхлеб"))

# # Cимволы * или +
# print(re.findall(r'([a-z]*)(\d*)', 'foo3, im12, go, 24buz42')) 
# print(re.findall(r'([a-z]+)(\d+)', 'foo3, im12, go, 24buz42')) 
# print(re.findall(r'([a-z]+)(\d*)', 'foo3, im12, go, 24buz42')) 
# print(re.findall(r'([a-z]*)(\d+)', 'foo3, im12, go, 24buz42'))

# # Любая цифра \d
# print(re.findall(r"СУ\d\d", "СУ35, СУ111, АЛСУ14"))

# # Любой символ, кроме цифры \D
# print(re.findall(r"926\D123", "926)123, 1926-1234, 192641234"))

# # Любой пробельный символ (пробел)
# print(re.findall(r"бор\sода", "бор ода, борода, бор\toда, борtoда"))

# # Любой непробельный символ \S
# print(re.findall(r"\S123", "X123, я123, !123456, 1 + 123456"))

# # Любая буква (то, что может быть частью слова), а также цифры и _. Эквивалентно r'[a-zA-Z0–9_]' \w
# print(re.findall(r"\w\w\w", "Год, f_3, qwert"))

# # Любая не-буква, не-цифра и не подчёркивание \W
# print(re.findall(r"сом\W", "сом!, сом?, сомaн"))

# # Один из символов в скобках, а также любой символ из диапазона a-b
# print(re.findall(r"[0-9][0-9A-Fa-f]", "12, 1F, 1f, 4B, 1s"))

# # Любой символ, кроме перечисленных
# print(re.findall(r"<[^>]>", "<1>, <a>, <>>"))

# string = "перевал, вал, Перевалка"
# # Начало или конец слова \b
# pattern = r"\bвал"
# result = re.findall(pattern, string)
# print(result)
# # Не граница слова: либо и слева, и справа буквы, либо и слева, и справа НЕ буквы
# pattern = r"\Bвал"
# result = re.findall(pattern, string)
# print(result)
# pattern = r"\Bвал\B"
# result = re.findall(pattern, string)
# print(result)


# 5. КВАНТИФИКАТОРЫ (УКАЗАНИЕ КОЛИЧЕСТВА ПОВТОРЕНИЙ)
# # Жадность в регулярках и границы найденного шаблона
# print(re.findall(r"СУ\d*", "ПАСУ13 СУ12, ЧТОБЫ СУЖЕНИЕ УДАЛОСЬ."))
# print(re.findall(r"СУ\d+", "ПАСУ13 СУ12, ЧТОБЫ СУЖЕНИЕ УДАЛОСЬ."))

# string = "foo@boo@goo@moo@roo@zoo"
# # pattern = r"[\w'._+-]+@[\w'._+-]+"
# pattern = r"\w+@\w+"
# result = re.findall(pattern, string)
# print(result)


# 6.ФУНКЦИИ ДЛЯ РАБОТЫ С РЕГУЛЯРКАМИ ЖИВУТ В МОДУЛЕ RE.
# string = 'Телефон 123-12-12 Телефон 233-52-82'
# pattern = r'\d\d\D\d\d'
# result = re.search(pattern, string)
# print(result)
# print(dir(result))
# pattern = r'\d{2}\D\d{2}'
# result = re.search(pattern, string)
# print(result)

# print(re.search(r'\d\d\D\d\d', 'Телефон 123-1212'))
# print(re.fullmatch(r'\d{2}\D\d{2}', '12-12'))
# print(re.fullmatch(r'\d{2}\D\d{2}', 'Т. 12-12'))
# print(re.fullmatch(r'\d{2}\D\d{2}', ' 12-12'))
pattern = r'[a-zA-Z \-\']*'
print(re.fullmatch(pattern, "O'Pavlo Fg Miha-Oslo"))


# print(re.findall(r'\d{2}\.\d{2}\.\d{4}', 'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'))

# iter_res = re.finditer(r'\d\d\.\d\d\.\d{4}', 'Эта строка написана 19.01.2018, а могла бы и 01.09.2017')
# print(iter_res)
# for m in iter_res: 
#     print('Дата', m[0], 'начинается с позиции', m.start())

# print(re.split(r'\W+', 'Где, скажите мне, мои очки??!'))

# string = 'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'
# pattern = r'\d{2}\.\d{2}\.\d{4}'
# repl = 'DD.MM.YYYY'
# result = re.sub(pattern, repl, string)
# print(result)

# 7.ИСПОЛЬЗОВАНИЕ ДОПОЛНИТЕЛЬНЫХ ФЛАГОВ В ПИТОНЕ
# print(re.findall(r'\d+', '12 + ٦٧'))
# print(re.findall(r'\d+', '12 + ٦٧', flags=re.ASCII))
# print(re.findall(r'\w+', 'Hello, мир!'))
# print(re.findall(r'\w+', 'Hello, мир!', flags=re.ASCII))
# print(re.findall(r'[уеыаоэяию]+', 'ОООО ааааа ррррр ЫЫЫЫ яяяя'))
# print(re.findall(r'[уеыаоэяию]+', 'ОООО ааааа ррррр ЫЫЫЫ яяяя', flags=re.IGNORECASE))
# text = '\nТорт\nс вишней1\nвишней2'
# print('text: ', text)
# text = """
# Торт
# с вишней1
# вишней2
# """
# print('text: ', text)
# # text = "Торт\nс вишней1\nвишней2"
# print(re.findall(r'Торт.с', text))
# print(re.findall(r'Торт.с', text, flags=re.DOTALL))
# print(re.findall(r'виш\w+', text, flags=re.MULTILINE))
# print(re.findall(r'^виш\w+', text, flags=re.MULTILINE))#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# 8. ТОНКОСТИ ЭКРАНИРОВАНИЯ В ПИТОНЕ
# string = '\\paritet'
# pattern = '\\par'
# # result = re.findall(pattern, string)
# # print(result)
# pattern = '\\\\par'
# result = re.findall(pattern, string)
# print(result)
# pattern = r'\\par'
# result = re.findall(pattern, string)
# print(result)


# # 9. ПЕРЕЧИСЛЕНИЯ (ОПЕРАЦИЯ «ИЛИ»)
# string = "морковк, свекл, картошк, редиск"
# pattern = r"морковк|св[её]кл|картошк|редиск"
# result = re.findall(pattern, string)
# print(result)


# 10. СКОБКИ ПЛЮС ПЕРЕЧИСЛЕНИЯ
# string = "+38-(097)-123-12-12, +38-(197)-123-12-12"
# pattern = "(?:\+38)(?:-\(0\d{2}\))(?:-\d{2,3}){3}"
# result = re.findall(pattern, string)
# print(result)

# # Скобочные группы (группировка плюс квантификаторы)
# string = "xdmvbdfjhfv s 01:23:45:67:89:ab nbsdcbvdf"
# pattern = r"[0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}"
# result = re.findall(pattern, string)
# print(result)
# pattern = r"[0-9a-fA-F]{2}(?:[:-][0-9a-fA-F]{2}){5}"
# result = re.findall(pattern, string)
# print(result)


# # 11. MATCH-ОБЪЕКТЫ
# string = "bkvdfgdk +38-(097)-123-12-12, +38-(067)-123-12-12"
# pattern = "(?:\+38)(?:-\(0\d{2}\))(?:-\d{2,3}){3}"
# match = re.search(pattern, string)
# print(match)
# print(match[0])
# print(match.group())
# print(match.start())
# print(match.end())

# string = '---   Опять45   ---' 
# pattern = '\s*([А-Яа-яЁё]+)(\d+)\s*' 
# match = re.search(pattern, string) 
# print('match: ', match)
# print(f'Найдена подстрока >{match[0]}< с позиции {match.start(0)} до {match.end(0)}') 
# print(f'Группа букв >{match[1]}< с позиции {match.start(1)} до {match.end(1)}') 
# print(f'Группа цифр >{match[2]}< с позиции {match.start(2)} до {match.end(2)}')


# # 13.СЛОЖНЫЕ ШАБЛОНЫ, СООТВЕТСТВУЮЩИЕ ПОЗИЦИИ
# string = """КарлIV, КарлIX, КарлV, КарлVI, КарлVII, КарлVIII,
# ЛюдовикIX, ЛюдовикVI, ЛюдовикVII, ЛюдовикVIII, ЛюдовикX, ..., ЛюдовикXVIII,
# ФилиппI, ФилиппII, ФилиппIII, ФилиппIV, ФилиппV, ФилиппVI"""

# # Людовик, за которым идёт VI
# pattern = r"Людовик(?=VI)"
# result = re.findall(pattern, string, flags=re.MULTILINE)
# print(result)

# # Людовик, за которым идёт не VI
# pattern = r"Людовик(?!VI)"
# result = re.findall(pattern, string, flags=re.MULTILINE)
# print(result)

# # «шестой», но только если Людовик
# pattern = r"(?<=Людовик)VI"
# result = re.findall(pattern, string, flags=re.MULTILINE)
# print(result)

# # «шестой», но только если не Людовик
# pattern = r"(?<!Людовик)VI"
# result = re.findall(pattern, string, flags=re.MULTILINE)
# print(result)

# # Цифра, окружённая не-цифрами
# print(re.findall(r'(?<!\d)\d(?!\d)', "Text ABC 123 A1B2C3!"))

# # Текст от #START# до #END#
# print(re.findall(r'(?<=#START#).*?(?=#END#)', "text from #START# till #END#"))

# # Цифра, после которой идёт ровно одно подчёркивание
# print(re.findall(r'\d+(?=_(?!_))', "12_34__56"))

# string = """a foo and
# boo and zoo
# and others"""
# # Строка, в которой нет boo
# print(re.findall(r'^(?:(?!boo).)*?$', string, flags=re.MULTILINE))
# # Строка, в которой нет ни boo, ни foo
# print(re.findall(r'^(?:(?!boo)(?!foo).)*?$', string, flags=re.MULTILINE))


# # ТОНКОСТИ СО СКОБКАМИ И НУМЕРАЦИЕЙ ГРУПП.
# string = '123456789'
# pattern = r'((\d)(\d))((\d)(\d))'
# result = re.findall(pattern, string)
# print(result)

# # ГРУППЫ И RE.SPLIT
# string = '12  +  13*15   - 6'
# print(re.split(r'(\s*)([+*/-])(\s*)', string))
# print(re.split(r'([+*/-])', string))
# print(re.split(r'\s*([+*/-])\s*', string))