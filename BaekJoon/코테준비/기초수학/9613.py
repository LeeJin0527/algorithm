from itertools import combinations
import math
import sys
sys = sys.stdin.readline
n = int(input())
for i in range(n):
	result = 0
	lst = list(map(int, input().split()))
	for j in list(combinations(lst[1:], 2)):
		result += math.gcd(*j)
	print(result)