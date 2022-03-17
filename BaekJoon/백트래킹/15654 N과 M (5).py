from itertools import permutations
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
for i in list(permutations(lst, m)):
	print(*i)
