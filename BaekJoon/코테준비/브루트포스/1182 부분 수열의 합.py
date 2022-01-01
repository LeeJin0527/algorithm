import sys
from itertools import combinations
input = sys.stdin.readline
n, s = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
	for j in list(combinations(lst, i)):
		if sum(j) == s:
			cnt += 1
print(cnt)

