import sys
from itertools import permutations
input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
lst = list(permutations(lst, m))

lst = set(lst)

lst = list(lst)
lst.sort()
for i in lst:
	print(*i)