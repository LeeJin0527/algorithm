import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
lst =  list(map(int, input().split()))
stack = [-1000000001]
d = [0] * n
maxVal = 0
for i in range(len(lst)):
	if stack[-1] < lst[i]:
		stack.append(lst[i])
		d[i] = len(stack)-1
		maxVal = d[i]
	else:
		d[i] = bisect_left(stack, lst[i])
		stack[d[i]] = lst[i]

print(d)
res = []
for i in range(len(d)-1, -1, -1):
	if maxVal == d[i]:
		res.append(lst[i])
		maxVal -= 1

res.reverse()
print(*res)
