from itertools import permutations
n, m = map(int, input().split())
lst = [i for i in range(1, n+1)]
for i in list(permutations(lst, m)):
	print(*i)