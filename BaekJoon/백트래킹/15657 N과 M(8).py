import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
for i in list(combinations_with_replacement(lst, m)):
	print(*i)