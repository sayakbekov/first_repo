# def main(*args, **kwargs):
#     print(args)
#     print(type(kwargs))

# main(7, 3)


# def  name(name='dosmart', age=15):
#     return f'привет {name} оо круто мне тоже {age} лет'


# print(name('azat', 18))


# def add(n1, n2):
#     return n1+n2

# def substract(n1, n2):
#     return n1-n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# print(divide( 23, 456))
# print(multiply(334, 2342))
# print(add(5, 9))
# print(substract(100, 98))

# def main(**kwargs):
#     return kwargs


# names = {'name':'amankeldi',
#         'n': 'azat'
#     }
# print(main(**names))





# def  wer(text):
#     text1 = 0
#     for i in text:
#         if i == ' ':
#             pass
#         else:
#             text1 += 1
#     return text1
# print(wer("aman 13"))

# def dic(a, b):
#     new_dict = {}
#     new_dict.update(a)
#     new_dict.update(b)

#     return new_dict

# print(dic({'name': 'amankeldi'}, {'age': 15}))



# def menu(a, b):
#     file = open('/home/mainuser/menu.txt', 'w')
#     file.write(a)
#     file.write(b)

#     return 'успешно завершено '
# print(menu('плов', 'кола'))

# def f():
#     file = input('слово')
#     with open(file, 'w')as s:
#         s.write('успешно')

# print(f())

# def f():
#     print('я основная функция ')
#     def f1():
#         print('я вложеная функция')
#     f1()
# f()

