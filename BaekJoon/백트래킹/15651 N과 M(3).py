from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = [i for i in range(1, n+1)]
flag = 0
for i in combinations_with_replacement(lst, m):
	print(*i)


