# import os, sys, random, platform
# import secrets, string
# import datetime

# print(os.name)
# os.mkdir('hello')
# os.rmdir('hello')

# print(os.listdir())
# print(os.path)

#


# ls = [1, 2,3,4,5,6,7,8,9,10]
# print(random.choice(ls))


# print(sys.argv)

# print(sys.executable)


# print(platform.architecture())
# print(platform.processor())



# print(random.randrange(1, 10, 3))
# print(random.randint(1, 10))

# names = ['azat', 'amankeldi', 'dosmart']
# ls = []
# for i in names:
#    print(i)
#     for alpha in i:
#         print(alpha)
#         ls.append(alpha)
# random.shuffle(ls)
# print(ls)


# letters = string.ascii_letters + string.digits
# password = ''.join(secrets.choice(letters) for i in range(8))
# print(password)




# start = datetime.datetime.now()
# for i in range(1, 100):
#     print(i)

# import sys
# print(sys.platform)

# import os
# os.mkdir('aman')
# file = open('/home/mainuser/aman/file.txt', 'w')
# file2 = open('/home/mainuser/aman/santa.txt', 'w')
# file3 = open('/home/mainuser/aman/amir.txt', 'w')
# file4 = open('/home/mainuser/aman/azat.txt', 'w')
# file5 = open('/home/mainuser/aman/beknazar.txt', 'w')

# import random

# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# print(random.choice(names))

# i = random.randrange(0, len(names), 2)
# print(names[i])

# ls = []
# for i in names:
#     for alpha in i:
#             ls.append(alpha)
# random.shuffle(ls)
# print(ls)
import random

a = input('камень, ножницы или бумага: ')
b = ['камень', 'ножницы', 'бумага']
comp =random.choice(b)


while True:
    if a == 'бумага' and comp == 'камень':
        print('win')
        a = input('камень, ножницы или бумага: если хотите выйти введите выйти')
    elif a == 'выйти':
        break
    elif a =='бумага' and comp == 'ножницы':
        print('lost')
        a = input('камень, ножницы или бумага: если хотите выйти введите выйти')
    elif a == 'выйти':
        break
    elif a == 'бумага' and comp == 'бумага':
        print('draw')
        a = input('камень, ножницы или бумага: если хотите выйти введите выйти')
    elif a == 'выйти':
        break

    elif a == 'ножницы' and comp == 'камень':
        print('lost')
        a = input('камень, ножницы или бумага: если хотите выйти введите выйти')
    elif a == 'выйти':
        break
    elif a =='ножницы' and comp == 'бумага' :
        print('win')
        a = input('камень, ножницы или бумага: если хотите выйти введите выйти')
    elif a == 'выйти':
        break
    elif a == 'ножницы' and comp == 'ножницы':
        print('draw')
        a = input('камень, ножницы или бумага: если хотите выйти введите выйти')
    elif a == 'выйти':
        break

    elif a == 'камень' and comp == 'камень':
        print('draw')
        a = input('камень, ножницы или бумага: если хотите выйти введите выйти')
    elif a == 'выйти':
        break
    elif a =='камень'and comp == 'бумага' :
        print('lost')
        a = input('камень, ножницы или бумага: если хотите выйти введите выйти')
    elif a == 'выйти':
        break
    elif a == 'камень' and comp == 'ножницы':
        print('win')
        a = input('камень, ножницы или бумага: если хотите выйти введите выйти')
    elif a == 'выйти':
        break
    