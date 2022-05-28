'''
Первое Задание
1.Что больше: Количество троек в числе 17531 или число 5821?
2.Если остаток деления 4388 на 7 больше или равно 4 - умножьте остаток на 7.
3.Если остаток деления 4292 на 5 меньше или равно 3 - разделите остаток на 3.
4.Распишите по порядку шаги исполнения выражения: 7 + 5 * (3 * (27**3))
5.Сколько получится если:
  1. От 183 отнять 17
  2. Разделить 19
  3. Добавить 13.6
  4. Результат умножить на 2
  5. И всё это поделить по модулю 12
'''

def main(a, b):
    q = a.count('3')
    if q > b:
        print(q,'>',b)
    else:
        print(q,'<',b)
#main('17531', 5821)

def ocnatok(a=4388):
    b =a %7
    print(b)
    if b >=4:
        print(b*7)
#ocnatok()

def octatok2(a=4292):
    b =a%5
    print(b)
    if b <=3:
        print(b*3)
#octatok2()

a =27*3
b =3*a
c=5*b
d=7+c
#print(c)

def chislo(a=183):
    b =a-17
    c =b/19
    d =c+13.6
    e =d%12
    return e
#print(chislo())
"""
#a(+,-,/,*,**, //,%)
a =input("выражения: ")
b =int(input("1 число: "))
c =int(input("2 число: "))
if a =="+":
    print(b+c)
elif a=="-":
    print(b-c)
elif a =="/":
    print(b/c)
elif a =="*":
    print(b*c)
elif a =="**":
    print(b**c)
elif a =="//":
    print(b//c)
elif a =="%":
    print(b%c)
else:
    print("Попробуйте еще раз")
"""    

'''
Третье Задание
АВТОРИЗАЦИЯ
1. Зарегистрируйте пользователя запросив логин и пароль
2. Добавьте полученные данные в список users = [ ]
3. Попросите Пользователя Войти запросив пороль и логин 
4. если данные есть в списке users выведите ДОБРО ПОЖАЛОВАТЬ 
5. Если данные не окажутся или были введены неправильные данные выведите НЕПРАВИЛЬНЫЙ ЛОГИН ИЛИ ПАРОЛЬ
'''

def avtoreg():
    login_password =input("Логин и пароль для регистрации")
    users=[]
    a =users.append(login_password)
    print(users)
    loginpassword =input("Войти Логин :пароль")
    for i in users:
        if  i == loginpassword:
            print("Добро пожаловать")
        else:
            print("НЕПРАВИЛЬНЫЙ ЛОГИН ИЛИ ПАРОЛЬ!!!")
#avtoreg()
'''
Собеседование
Должен
знать либо python, либо java, либо javascript. Возраст от 18 до 65. Опыт
от 3х лет. Зарплата до 60000. Вывести результат, подходит кандидат или
нет.
'''

a =['python',"java","javascript"]
lan =input("Какой язык програмирования вы знаете?")
age =int(input("Ваш возраст?"))
zp =int(input("Какию зарплату вы хотите?"))
opyt =int(input("Ваш опыт?"))


if lan == 'python' or lan == 'java' or lan == 'javascript':
    if age >=18 and age <= 65: 
        if opyt >=3:
            if zp <=60000:
                print('podhodite')
else:
    print(' ne podhodite')
# for item in a:
#     if item ==b:
#         print("проверка 1")
#         if c >=18 and c<=65:
#             print("проверка 2") 
         
#             if d >=3:
#                 print("проверка 3")
            
#                 if s<=60000:
#                     print("Вы подходит")
#                 else:
#                     print("нет")
