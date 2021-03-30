# a = 2.9
# b = 3
# try:
#     print(a/b)
# except:
#     if b == 0:
#         print('ZeroDivisionError: ', ZeroDivisionError)
#     else:
#         print('TypeError: ', TypeError)
conteiners = [[1, None, 2, 3, 4+5j, 6], [1.0, 2.5, None, 3,9, 4.0+5.2j, 6.1], ['1', '2', '3.6', None, '4+5.7j', '6']]

for conteiner in conteiners:
    print('conteiner: ', conteiner)
    for box in conteiner:
        print('box: ', box)
        print('type(box): ', type(box))