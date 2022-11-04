'''
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']

lang = input('язык программирования: ')
for i in languages:
        if i == lang:
                print('этот язык программирования есть в списке! ')
'''
'''
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
	print(i)
	if i == 'php':
		break
'''

'''
a = 1
for i in range(5):
        a = a*7
print(a)
'''


'''
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
a = 0
for  i in languages:
	print(a, i)
	a += 1
'''
'''
for i in range(11):
        print(i)
for i in range(9, 0, -1):
        print(i)
'''

#names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
#for i in range(12)
'''
ls=[1,2,3,4,5,6,7,8,9,10]
q = 0
print(type(q))
print(names[q])
for i in range(len(names)):
	if names[q] % 2== 0:
		print (names[q])
	q += 1
'''

#for index, item in enumerate(names):
#	if index % 2 == 0:
#		print(item)
'''
names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
for index, item in enumerate(names):
       if index % 2 == 0:
               print(item)
'''
'''
a  = int(input('число'))
string1  = str(a)
if len(string1)==3:
	print('Это число трёхзначное?')
if a>0 and a % 2==0:
	print(' Это число положительное и чётное')
if a>100 and a % 17 and a>150 and a==13**2:
	print('это число больше 100 и оно делится на 17 без остатка или это число больше 150 и равно 13**2 тогда показать что это за число')
'''
'''
ls=[]
for i in range(-100, 101):
	ls.append(i)
print(ls)
for item in (ls):
	if item%13==0 and item%2==0:
		print(item)
'''
'''
ls = ["3:1", "2:2", "0:1", "3:0", "0:0", "0:1", "4:2", "2:1", "1:1", "0:2"]
points = 0
for i in ls:
	if int(i[0]) > int(i[2]):
		points += 3
	if int(i[0]) < int(i[2]):
		points += 0
	if int(i[0]) == int(i[2]):
		points += 2
print(points)
'''
'''
n = int(input('сколько стоит телефон'))
k = int(input('сколько вы можете откладывать'))
money = 0
days = 0
sunday = 0
while money < n:
	if days == 7:
		sunday += 1
	money += k
	days += 1

print(days + sunday)
'''

