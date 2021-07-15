def add(a, b):
	return a + b

a = 3
b = 4
c = add(a, b)
print(c)

def add(a, b):
	return a + b
print(add(3, 4))

def say():
	return 'Hi'

a = say()
print(a)

def add(a, b):
	print("%d %d 의 합은 %d 입니다" %(a, b, a+b))

a = add(3, 4)

def say():
	print('Hi')
say()

def add(a, b):
	return a + b
result = add(a = 3, b = 7)
print(result)

result = add(b = 5, a = 3)
print(result)

def add_many(*args):
	result = 0
	for i in args:
		result = result + i
	return result
result = add_many(1, 2, 3)
print(result)
result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

def add_mul(choice, *args):
	if choice == "add":
		result = 0
		for i in args:
			result = result + i
	elif choice =="mul":
		result = 1
		for i in args:
			result = result * i
	return result

result = add_mul('add', 1, 2, 3, 4, 5)
print(result)

result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)

## 키워드 파라미터 kwargs
# 매개변수를 출력하는 함수 이다 .
def print_kawrgs(**kwargs):
	print(kwargs)

print_kawrgs(a = 1)
print_kawrgs(name='foo', age = 3)

def add_and_mul(a, b):
	return a+b, a*b
result = add_and_mul(3, 4)
print(result)

def say_nick(nick):
	if nick =="바보":
		return
	print("나의 별명은 %s 입니다." %nick)
say_nick('야호')
say_nick('바보')

def say_myself(name, old, man=True):
	print("나의 이름은 %s 입니다." %name)
	print("나이는 %d 살 입니다." % old)
	if man:
		print('남자입니다.')
	else:
		print('여자입니다.')
say_myself("이진", 24)
say_myself("이진", 24, False)

#효력이 없음
a = 1
def vartest(a):
	a = a+1
vartest(a)
print(a)

def vartest(hello):
	hello = hello + 1

def vartest(a):
	 a= a + 1
	 return a
a = vartest(3)
print(a)

a = 1
def vartest():
	global a
	a = a+ 1
vartest()
print(a)

add = lambda a, b: a+b
result = add(3, 4)
print(result)

