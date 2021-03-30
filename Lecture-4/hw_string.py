# str_ = "MusTAng Gt500"
# elements = str_.split(' ')
# print('elements: ', elements)
# formated_name = elements[0].title()
# print('formated_name: ', formated_name)
# formated_compl = elements[1].upper()
# print('formated_compl: ', formated_compl)
# df = f'{formated_name} {formated_compl}'
# print('df: ', df)


# str_ = "MusTAng Gt500"
# elements = str_.split(' ')
# print('elements: ', elements)
# print('type(elements): ', type(elements))
# print('dir(elements): ', dir(elements))
# df = f'{elements[0].title()} {elements[1].upper()}'
# print('df: ', df)


str_ = "MusTAng Gt500"
elements = str_.split(' ')
print('elements: ', elements)
formated_name = elements[0].title()
print('formated_name: ', formated_name)
print('type(formated_name): ', type(formated_name))
formated_compl = elements[1].upper()
print('formated_compl: ', formated_compl)
print('type(formated_compl): ', type(formated_compl))
str_cancat = formated_name + " " + formated_compl
print('str_cancat: ', str_cancat)
str_cancat1 = f'{formated_name} {formated_compl}'
str_cancat1 = f'{formated_name} {None}'
print('None: ', None)
print('type(None): ', type(None))
print('str_cancat1: ', str_cancat1)
