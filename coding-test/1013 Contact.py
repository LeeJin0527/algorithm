import re
n = int(input())
for _ in range(n):
	compare = input()
	regular = re.compile('(100+1+|01)+')
	if regular.fullmatch(compare):
		print('YES')
	else:
		print('NO')
