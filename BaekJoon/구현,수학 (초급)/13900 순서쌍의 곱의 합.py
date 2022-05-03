import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
s = sum(lst)
result = 0
for i in lst:
	s -= i
	result += s * i
print(result)