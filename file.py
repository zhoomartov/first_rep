'''
file = open('directories.txt', 'w')
file.write('above-educational-free-web-templa')
file.close()

f = open('directories.txt', 'r')
a = f.read()
print(a)
f.close()
'''

'''
name =input('username: ')
password =input('password: ')
f = open('user.txt', 'w')
a =f.write(f'username: {name}\n password: {password}')
'''

'''
f = open('directories.txt', 'r')
a = f.read()
if 'w' in a:
	print('да ,в тексте есть w ')
else:
	print('нет, в тексте нет w')
f.close()
'''
'''
t_words = []
a = open('python.txt', 'w')
b = a.write(Python is a widely used high-level programming language for general-purpose
programming, created by Guido van Rossum and first released in 1991. An interpreted
language, Python has a design philosophy that emphasizes code readability (notably
using whitespace indentation to delimit code blocks rather than curly brackets or
keywords), and a syntax that allows programmers to express concepts in fewer lines of
code than might be used in languages such as C++ or Java.
)
a.close()

f = open('python.txt', 'r')
a = f.read()
for i in a.split():
	if 'T' and 't' in i:
		t_words.append(i)
print(t_words)
f.close()
'''

a =open('database.txt', 'a') 
login =input('логин')
password =input('пароль')
p2 = input()

b =open('database.txt', 'r')
q = b.read()
for i in q.split(':'):
	if login == i:
		print('login zanyat!')
	else: 
		a.write(f'{login}:{password}')
