'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i>5:
        print(i)
'''
'''
digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
for i in digits:
    a = i/9
    print(a)
'''
fruits = ('banana','stawberry','apple','orange','limon','ananas')
#print(fruits [0])
#print(fruits[-1])


'''
spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)

for i in spisok_2:
    if i not in spisok_1:
        print(i)
'''


import random

'''
for i in range(300):
    if i %2==0:
        print(i)
    if i ==237:
        break
'''

def guess_number():
    tries = 1
    random_number = random.randint(0,10)
    print(random_number)
    number = int(input('Выберите число в диапазоне от 0 до 10: '))
    if number == random_number:
        print('Вы выиграли!')
    else:
        while random_number != number:
            number = int(input('Попробуйте еще раз! '))
            tries += 1
            if tries == 3:
                print('Вы воспользовались всеми тремя шансами! ВЫ проиграли')
                break
            if number == random_number:
                print('Вы выиграли!')

guess_number()

def text():
    l = []
    t = input('введите текст больше 6ти слов')
    b =t.count(' ')
    print(b)
    while b+1 <= 6:
        t = input('введите текст больше 6ти слов')
    for i in t.split():
        l.append(i)
    c =l[:len (l)//2]
    n =l[len(l)//2:]
    n.extend(c)
    return n
#print(text())

numbers = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]
for i in (numbers):
 #print(i)