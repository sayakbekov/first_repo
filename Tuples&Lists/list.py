'''
a = (123, 4545, 54654)
b = ('dfdf' , 'wewewew')

ls = []
ls.extend(a)
ls.extend(b)
print(ls)




print(a[0])
print(a[1])

print(a[::1])
'''
'''
ls = []
ls.append( 12345 )
ls.append(123456.56)
ls.append('12345')
ls.append(1,)
ls.append([23456])
print(ls)
'''
'''
a = ''
ls = []
ls.append('beknazar')
ls.append('azat')
ls.append('dosy')
ls.append('samat')
ls.append('bakula')
print(a.join(ls))
'''

'''
a = [424, 4556,  646,]
b = ['dgfer', 'etggg',]
a.extend(b)
print(a)
'''

#names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
#print(names.count('Jack'))

#names.remove('Jimmy')
#print(names)

'''
ls=[]
ls.append('amankeldi')
ls.append('2007')
ls.append('python')
print(ls)
'''
'''
pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
print(pythonList.index('loop'))
print(pythonList.pop(6))
print(pythonList)
'''
'''
numbers = [123, 321, 2, 543, 64, 463, 234, 867, 6234, 63246, 3, 43]
a = 0
for i in numbers:
	a+=i
print(a)
'''
'''
string = "14 июня"

letters = []
numbers = []
if string[0].isdigit():
	numbers.append(string[0])
if string[1].isdigit():
        numbers.append(string[1])
if string[3].isalpha():
	letters.append(string[3])
if string[4].isalpha():
        letters.append(string[4])
if string[5].isalpha():
        letters.append(string[5])
if string[6].isalpha():
        letters.append(string[6])
print(numbers ,letters)
'''

#pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
#print(pythonList[1:4])
