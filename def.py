# my_list = [1, 'dfkjfhd', True, 555]
# def length():
#     result = 0
#     for i in my_list:
#         result += 1
#     print('ваш список состоит из {0} элементов'.format(result))


# length()

# print(my_list)


# def name():
#     a = input('name: ')
#     print(a)





# list_1 = ['name', 'age', '1', '19']
# # list_1 = ['age', 'name', '19', '1']

# def listik():
#     l1 = list_1[: len(list_1)//2]
#     l2 = list_1[len(list_1)//2 :]
#     l1 = list(reversed(l1))
#     l2 = list(reversed(l2))
#     print(l1+l2)
# listik()

# def fibonacci(chislo):
#     list = []
#     f1 = 0 
#     f2 = 1
#     for i in range(chislo):
#         s = f1 + f2
#         list.append(s)
#         f1 = f2
#         f2 = s
#     print(list)

# fibonacci(199)   


# def num(x , y):
#     if operation == '+':
#         result = x + y
#         print(result)
#     else:
        
#         print('Entre right sym')
        
# result = None

# a = float(input('a = '))
# operation = input('symbol = ')
# d = float(input('b = '))

# num(a, d)

# def num(x , y):
#     if operation == '-':
#         result = x - y
#         print(result)
#     else:
#         print('Entre right sym')
        
# num(a,d)

def open_file():
    file = input('name file')
    with open(file, 'w')as s:
        s.write('your file')
a = open_file()
print(a)





# def gen_number():
#     a = ['1',' 4', '5','7','9','0']
#     b = ['0444']
#     for i in range(6):
#         d = random.choice(a) 
#         b.append(d) 
#         num = ''.join(b)
#     print(num)
# gen_number()