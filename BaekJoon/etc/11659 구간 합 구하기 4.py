import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

for i in range(1, len(lst)):
	lst[i] = lst[i]+ lst[i-1]
# print(lst)
for i in range(m):
	x, y = map(int, input().split())
	first = lst[y-1]
	if x-2 < 0:
		second = 0
	else:
		second = lst[x-2]
	print(first - second)

