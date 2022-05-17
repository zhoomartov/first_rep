from re import S
from unittest import result


list_1 =['name', 'age', '1','19']
def main(a):
    f =a[:len(a)//2]
    f =list(reversed(f))
    w =a[len(a)//2:]
    w =list(reversed(w))
    print(f+w)    


def fibonacce(n):
    list =[]
    a = 0
    b = 1
    for i in range(n):
        c = a+b
        list.append(c)
        a = b
        b = c
    print(list)

#fibonacce(15)

def addition ():
    nomber1 = int(input('chislo'))
    nomber2 = int(input('chislo'))
    summa = nomber1 + nomber2
    print(summa)
# addition()

def calc ():
    nomber1 = int(input('chislo'))
    nomber2 = int(input('chislo'))
    summa1 = nomber1 - nomber2
    print(summa1)
# calc()

def calcaddintion ():
    calc()
    addition()

#calcaddintion()

'''
def fail (a):
    # a =input()
    with open(a ,'w') as b:
        b.write('qwerty')
fail('pythim.py')
'''
import random
def gen_number():
    list =['1','4','5','7','9','0']
    a = ['0444']
    for i in range(6):
        d =random.choice(list)
        a.append(d)
        number = ''.join(a)
    print(number)


# a = '348597'

# def digitize(n):
#     list =[]
#     for i in reversed(n):
#         list.append(i)
#     print(list)

# digitize(a)

# def main(n):
#     result = n+10
#     return result


# print(main(20))



# def my_func(*args, **kwargs):

#     print(kwargs) 


# my_func(fdfdf=374634)


def index(name, year, job, current_year=2022):
    age=current_year-year
    return f'Hello {name}! YA znau chto tebe {age} let. ty doljen pomenyat svou profeesion {job}'

#print(index('Bruno', 2000, 'doctor'))

def add(n,b):
    return n+b 
#print(add(10,20))
 
def substract(n,b):
    return n-b
#print(substract(20,30))

def multiply(m,k):
    return m*k
#print(multiply(20,30))

def divide(l,d):
    return l/d
#print(divide(20,30))

def collichestvo(b):
    a =0
    for i in b:
        if i == ' ':
            pass
        else:
            a+=1
    return a 
#print(collichestvo('werty qwert'))    

def direc (**kwargs):
    return kwargs

#print(direc(name='dosmart'))    

def menu(food, drink):
    with open ('menu.txt', 'w')as s:
        s.write(f'{food}, {drink}')
menu('lagman', 'cola')

def file (n):
    with open (n, 'w')as d:
        d.write(' ')
        return d
(file('fhfjhjhjh'))

'''
def function():
    print( 'я главная функция')

    def function_1():
         print('я вложенная функция')
    
    function_1()
function()
'''
'''
def dictionary(**kwargs):
    keys = kwargs.keys()
    values = kwargs.values()
    
    keys = tuple(keys)
    values = tuple(values)
    print(keys)
    print(values)
print(dictionary(name='dos', age=14))
'''
def simpe(d):
    a =2
    while d%a!=0:
        a+=1
    return d==a
(simpe(3))

def txt(a,b):
    ls =[]
    ls.append(a)
    ls.append(b)
    return ls
#print(txt('qwerty',4456))
'''
def chislo(n):
    if n==1:
        for i in range(n):
            print('1')
chislo(1)
elif n==10:
    for i in range(n):
        print('10')
chislo(10)
'''
def work (n, zp=5000):
    return f'{n}: {zp}'
#print(work('dos', zp=9000))

import random 
def chislo (n):
    ls =[]
    for i in range (n):
        ls.append(random.randint(1 ,9))
    return ls
#print(chislo(10))


def guess_number():
    tries = 1
    random_number = random.randint(0,10)
    number = int(input('Выберите число в диапазоне от 0 до 10: '))
    if number == random_number:
        print('Вы выиграли!')
    else:
        while random_number != number:
            number = int(input('Попробуйте еще раз! '))
            tries += 1
            if tries == 5:
                print('Вы воспользовались всеми тремя шансами! ВЫ проиграли')
                break
            if random_number > number:
                print('бери выше')
            elif random_number < number:
                print('бери ниже')
            if number == random_number:
                print('Вы выиграли!')

guess_number()