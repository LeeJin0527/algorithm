import sys
input = sys.stdin.readline
while True:
	lst = list(map(int, input().split()))

	if all(i for i in lst) == 0:
		break
	lst.sort()
	if lst[-1] >= lst[0] + lst[1]:
		print('Invalid')
	elif lst[0] == lst[1] == lst[2]:
		print('Equilateral')
	elif lst[0] != lst[1] != lst[2]:
		print('Scalene')
	else:
		print('Isosceles')
