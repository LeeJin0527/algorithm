from itertools import combinations
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
for i in list(combinations(lst, m)):
	print(*i)
