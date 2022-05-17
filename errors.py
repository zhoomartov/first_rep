'''
n = [1, 2]
try:
	for i in range(-5, 5):
		if int(i) % 2 == 0:
			print(n[2]/i)
except IndexError:
	print('bro у тебя проблемы с индексом')
'''

'''
values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)

true = []
false = []
try:
	for i in values:
		true.append(set(i))
except:
	for i in values:
		false.append(i)
print('spisok true:', true)
print('spisok false:', false)
'''

'''
a =input('5 чисел с пробелами')
b ={133}
for i in a.split():
	b.add(int(i))
print(min(b))
'''
'''
n =[]
a = input('python функция')
if a == 'print':
	print('')
elif a == 'len':
	l = len(a)
	print(f'len {l}')
elif a == 'append':
	n.append(a)
	print(n,'вот ваш лист')
elif a == 'index':
	print('находит индекс')
elif a == 'add':
	print('добавляет элемент в множество ')
else:
	print('вы непровильно ввели финкцию')
'''
'''
s = int(input('сумма займа (не больше 49 999)'))
b =s*(3.47/100)
print(round(b, 2))
'''

'''
a =input('')
b =a + 100
print('pr')
'''

'''
a =['asdfg']
print(a.pop(5))
'''

'''
a = 234
c =34
print(a+b)
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
a = 0
b = 1
numbers = []
try:
	while b > a:
		numbers += b
		b += 1
except TypeError:
	print('что-то с типами данных!')
'''


'''
dict ={'name': 'john', 'lastname': 'Show', 12: 'age'}
try:
	for x in dict.keys():
		x + 'abc'
except TypeError:
	print('ind and str')
'''





