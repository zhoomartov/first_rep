'''
def main(n):
    ls=[]
    for i in (1 len(n)+1):
            
'''




















'''
a =input('введите текст')
text_1 = a[:len (a)//2]
text_2 = a[len (a)//2:]
b =text_1.upper()
c =text_2.lower()
print(b)
print(c)
'''

#"Аналог шифра цезаря ". Программа должна запрашивать элементы списка через пробел. 
# После чего пользователь должен ввести значение для сдвига элементов списка. 
# Значение может быть как положительным, так и отрицательным. Если значение положительное, 
# элементы списка должны сдвигаться вправо, если отрицательное - влево. Результат необходимо вывести на экран:
# Введенные данные: [5,7,9,10,2] 2
# Результат:        [9,10,2,5,7]
# """

def sdvig(n):
    a =int(input())
    print(n)
    return n[a:]+ n[:a] or n[-a:]+ n[:-a]
#print(sdvig([5,7,9,10,2]))


# "Напишите функцию которая принимает в себя словарь где ключи это номера а значения страны. Попросите пользователя ввести страну или ключ и выдайте ему результат."
# d = {'1': 'kyrgyzstan', '2': 'kazahstan'}
# """
'''
def country(a):
    d = {'1': 'kyrgyzstan', '2': 'kazahstan'}
    a =input('выведите страну или ключ')
    for i in d:
        if i ==a:
            print(i)
            break 
    return i 
print(country())
'''

def country_1 (n):
    d ={'1': 'kyrgyzstan', '2': 'kazahstan'}
    if type (n) == int:
        for i in d.keys():
            if str(n)==i:
                return d.get(i)
print(country_1(1))