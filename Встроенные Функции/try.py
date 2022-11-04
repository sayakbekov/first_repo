
'''
try:
        print('ошибка типов данных')
        for i in range(-5, 5):
                if int(i) % 2 == 0:
                        print(i)
except:
        print('error')



try:
        a = 123
         b = '321'
        print(a+s)
except TypeError:
        print('ошибка типов данных')
'''
'''
try:
        values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
        true= {}
        false = {}
        true = set(true)
        false = set(false)
        for i in values:
                if i:
                        true.add(int(i))
                else:
                        false.add(i)


except:
        for i in values:
                if i:
                        true.add(str(i))
                else:
                        false.add(i)
print('true: ', true)
print('false: ', false)






while True: print(eval(input('vvedite vyrajenie: ')))
'''
'''
a = input('vedite chislo')
s = {}
s=set(s)
for i in a.split():
	s.add(int(i))
print(min(s))
'''
'''
a = input('ведите функцию ')
if 'abs'==a:
	print('Возвращает число в АБСОЛЮТНОМ значении: ')
elif 'eval'==a:
	print('Позволяет исполнить Python code из Строки.')
elif 'round'==a:
	print('Округляет значение числа до задонного места.')
else:
	print('такой функции у нас нет!')
'''
'''
a =int(input('сумма  не меньше 50000'))
b=a*(3.47/100)
print(round(b,2))
'''
'''
try:
	a = 123
	b = '321'
	print(a+b)
except TypeError:
        print('ошибка типов данных')
try:
	ls =[ 1, 2, 3, 6]
	ls[0]
	ls[3]
	ls[4]
except IndexError:
	print('не имеет такого индекса')
try:

        a = 123
        b = '321'
        print(s+b)
except NameError:
	print('вызывает обект которого не сушествует' )
'''
'''
try:
	at = 10
	n = 15
	wo = 20

	for e in range(-at, at):
		print(wo / e)
	if at > '5':
		print(at > 5)
except:
	print('Не закрыли скобку, не поставили равно и много много остального...')
'''
'''
lst = []
for i in range(10):
	lst.append(i)
a = list(reversed(lst))
sls_obj = slice(0,8)
print(a[sls_obj])
'''
'''
a = (0)
b = (1)
numbers = []
while b >= a:
	  b -= 1
print(b + 1)
'''
'''
try:
	dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
	for x in dict_.keys():
		x + 'abc'
except TypeError:
        print('ошибка типов данных')
'''
