import sys
from itertools import product
input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

for i in list(product(lst, repeat=m)):
	print(*i)