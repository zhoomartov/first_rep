def chislo (a,b):
    n =a*b
    return n
#print(chislo(3,3))


def main(number):
    if number == 0:
        print(number)
    elif number > 0:
        main(number-1)
    else:
        main(number+1)

#main(994)



#print((lambda a,b: f'результат умножения: {a*b}' )(100, 50))


def jibek(function):
    def wrapper():
        print('hello! my name is Jibek')
        function()
    return wrapper

@jibek
def dos():
    print('hello! my name is Dosmart')

# dos()


#print((lambda a, b, c: f'Обьем бассейна: {a*b*c}')(55, 80, 40))

#print((lambda a: f'до нового года осталось {365-a]},прошло с нового года {}')(135))

def chislo (number):
    if number %2!=0:
        print(number)
    chislo(number+1)
    
#chislo(1)

'''
ls ={'asdf','qwerty',2354}
def function(kaas):
    print(kaas)
    if len(kaas) == 0:
        return kaas
    else:
        kaas.pop()
        function(ls)
function(ls)
'''

import random
'''
ls =[]
def chislo(f):
    for i in range(100):
        random_number =random.randint(10,50)
        ls.append(random_number)
    print(ls)
    def wrapper(arg):
        f(arg)
    return wrapper

@chislo
def delete (arg):
    arg =set(arg)
    print(list(arg))
delete(ls)

'''

def registration(f):
    def wrapper(n, p):
        f(n, p)
    return wrapper


@registration
def cache(n, p):
    users = {}
    ls_for_use = []
    ls = []
    for i in n:
        ls.append(ord(i))
    print(ls)
    while len(ls)!=0:
        for i in ls:
            ls.remove(i)
            ls_for_use.append(str(i))
    print(ls_for_use)
    name = ''.join(ls_for_use)
    print(name)


cache('dosmart_', '12345')