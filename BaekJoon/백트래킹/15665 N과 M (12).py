import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

result = list(combinations_with_replacement(lst, m))


answer = []
for i in result:
	if i not in answer:
		answer.append(i)
		print(*i)