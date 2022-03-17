import sys
from itertools import product
input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))

result = list(product(lst, repeat=m))
result = set(result)

result = list(result)
result.sort()
for i in result:
	print(*i)