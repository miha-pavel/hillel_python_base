dict_={1:10, 2:20, 3:30, 4:40, 5:50}
print('dict_: ', dict_)
print('id(dict_): ', id(dict_))
first = list(dict_.items())[0]
print('first: ', first)
second = list(dict_.items())[1]
print('second: ', second)
last = list(dict_.items())[-1]
print('last: ', last)
dict_[first[0]], dict_[last[0]] = last[1], first[1]
print('dict_: ', dict_)
print('id(dict_): ', id(dict_))
dict_.pop(second[0])
print('dict_: ', dict_)
print('id(dict_): ', id(dict_))
dict_['new_key'] = 'new_value'
print('dict_: ', dict_)
print('id(dict_): ', id(dict_))