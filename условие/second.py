'''
a = input('какую вы машину хотите?') 
b = input('какого года?')
c = input('с каким пробегом?')
d = input('какого цвета?')
e = input('со сколькими хозяинами?')
r = input('цена?')
car = ['Toyota ', 'Lexus']
color = ['white', 'grey']
for i in car:
	if i==a:
		print(i)
if int(b) >= 2004:
	print(b)
if int(c) == 150000:
	print(c)
for i in color:
	if i == d:
		print(i)
if int(e) <= 2:
	print(e)
if int(r) <= 10000:
	print(r)

else:
	print('извините такой машины нету')

c = input('с каким пробегом?')
r = input('цена?')
if int(c) ==200000:
	print(c)
if int(r) <= 8000:
	print(r)
else :
	print("извините такой машины нету")

'''

a = input('какой компьютер желаете?')
b = int(input('оперативная память?'))
c = int(input('размер жесткого диска?'))
d = input('SSD или  HDD')
e = int(input('терабайт'))
comp = ['hp', 'acer','lg']
memory = ['4', '8']
k = ['SSD', 'HDD']
for i in comp:
	if i == a:
		print(i)
for i in memory:
	if i == b:
		print(i)
if int(c) <= 256:
	print(c)
for i in k:
	if i==k:
		print(i)
if e <= 1:
	print(e)

