lst = list(input())
answer = []
for i, v in enumerate(lst):
	answer.append(lst[i:])
answer.sort()
for i in answer:
	print(''.join(i))