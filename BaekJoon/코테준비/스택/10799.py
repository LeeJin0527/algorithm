lst = list(input())
stk = []
answer = 0
for i, v in enumerate(lst):
	if v == '(':
		stk.append(v)
	else:
		if lst[i-1] == '(':
			stk.pop()
			answer += len(stk)
		else:
			stk.pop()
			answer += 1
print(answer)
