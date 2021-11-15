n = int(input())
result = 0
for i in range(n):
	answer = list(input())
	stk = []
	for j, v in enumerate(answer):
		if v == '(':
			stk.append(v)
		elif v == ')':
			if len(stk) == 0:
				result = 0
				break
			else:
				stk.pop()
		if stk:
			result = 0
		else:
			result = 1
	if result == 0:
		print('NO')
	else:
		print('YES')
