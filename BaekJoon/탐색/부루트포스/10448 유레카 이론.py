from itertools import combinations_with_replacement
import sys
import math
input = sys.stdin.readline
t = int(input())
for _ in range(t):
	n = int(input())
	tmp = []

	for i in range(1, n+1):
		x = i*(i+1) // 2
		if x > n:
			break
		tmp.append(x)
	result = 0
	for i in list(combinations_with_replacement(tmp, 3)):
		if sum(i) == n:
			result = 1
			break
	print(result)
