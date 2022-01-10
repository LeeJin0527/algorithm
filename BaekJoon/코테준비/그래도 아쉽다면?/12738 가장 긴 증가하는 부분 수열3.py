import sys
from bisect import bisect_left
n = int(input())
lst = list(map(int, input().split()))
stack = [-1000000001]
for i in range(len(lst)):
	if stack[-1] < lst[i]:
		stack.append(lst[i])
	else:
		k = bisect_left(stack, lst[i])
		stack[k] = lst[i]
print(len(stack[1:]))