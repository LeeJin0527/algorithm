lst = list(input())

stk = []
answer = 0
tmp = 1
for i, v in enumerate(lst):
	if v == '(':
		tmp *= 2
		stk.append(v)
	elif v == '[':
		tmp *= 3
		stk.append(v)
	elif v ==')':
		if len(stk) == 0:
			answer = 0
			break
		elif lst[i-1] == '(':
			answer += tmp
		elif stk[-1] == '[':
			answer = 0
			break
		stk.pop()
		tmp //= 2

	else:
		if len(stk) == 0:
			answer = 0
			break
		elif lst[i-1] == '[':
			answer += tmp
		elif stk[-1] == '(':
			answer = 0
			break
		stk.pop()
		tmp //= 3


if stk:
	print('0')
else:
	print(answer) 
