# def main(number):
#     # print(number)
#     if number == 0:
#         print(number) 
#     if number > 0:
#         if number == 0:
#             print(number) 
#         else:
#             main(number-1)
#     if number < 0:
#         if number == 0:
#             print(number) 
#         else:
#             main(number+1)

# # main(20)





# def aza(a, b):
#     return a*b

# print(aza(4, 8))



# a = (lambda a, b: a*b)(4, 5)
# print(a)


# print((lambda a, b, n: f'{a} умноженная на {b} и деленая на {n} = {a*b//n}')(4333, 335, 5))



# def  dosmart(func):
#     def inner():
#         print('I am Dosmart')
#         print(func())

#     return inner

# @dosmart
# def amankeldi():
#     print('I am Amankeldi')


# print(amankeldi())




# def plus(func):
#     def inner(a, b):
#         print(f'{a+b} я сложил и сделал свою работу!')
        
#         func(a, b)
#     return inner



# @plus
# def minus(c, v):
#     print(f'{c - v} я отнял и сделал свою работу!' )



# minus(6, 5)




# print((lambda a, b, c: f'Объём бассейна = {a*b*c}')(5, 6, 4))

# print((lambda a, b: f' {a} прошло с нового года, {b} осталось до нового года  ') (303, 62))


# def check(n):
#     if n % 2 == 1:
#         print(n)
#     check(n+1)

# print(check(1))

# sss={'dfgh',"dfghjkk",44.7,66}

# def rec(s):
#     print(s)  
#     if len(s) == 0:
#         return s   
#     for value in s:  
#         a = []  
#         a.append(value)  
#         break   
#     s.discard(a[0])       
#     return rec(s)
# print(rec(sss))

import random  

def fuin(f):
    def inner_fun():
        fuin=f()
        b = []
        for i in fun:
            if i in b:
                continue
            elif not i in b:
                 b.append(i)
        return b
    return inner_fun

@fun
def random_list():
   return random.choices(range(10, 51), k = 100)

print(random_list())




# str = "%"
# result = ord(str)
# print(result)
 
# # Выполняем преобразование кода ASCII в символ
# str_2 = 977
# result_2 = chr(str_2)
# print(result_2)

# spisok= [1745345,98726,439872634,7312,64872,123687126,9312,4124,231,3123,34,3453] 


# new_spisok= []

# for value in spisok:
#     a = 1.185
#     s = (lambda x, y: x*y) (value, a)
#     new_spisok.append(s)
# print(new_spisok) 




# def auth(login, password):
#     encrypted_password = ''
#     encrypted_ls = [str(ord(i)) for i in login]
#     for i in login:
#         encrypted_login = ''.join(encrypted_ls)
#     print(encrypted_login)

    
#     encrypted_password = chr(int(password))
#     print(encrypted_password)


# auth('admin', '10356')



# import random as rd
