from collections import defaultdict
n = int(input())
lst = defaultdict(list)
for i in range(n):
	tmp = input()
	lst[tmp].append(tmp)
answer = {}
for i in lst:
	answer[i] = len(lst[i])
answer = max(sorted(answer.items()), key=lambda x:x[1])
print(answer[0])

'''
from collections import defaultdict
n = int(input())
lst = defaultdict(list)
for i in range(n):
	tmp = input()
	lst[tmp].append(tmp)
answer = []
for i in lst:
	answer.append([i, len(lst[i])])
answer.sort(key=lambda x: (x[1], x[0]), reverse= True)
block = 0
result = []
for i, v in enumerate(answer):
	if i == 0:
		block = v[1]
	if v[1] < block:
		break
	result.append(v[0])
print(result[-1])

'''