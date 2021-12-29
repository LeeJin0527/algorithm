import sys
from collections import deque, defaultdict
input = sys.stdin.readline
n, s, m = map(int, input().split())
songs = list(map(int, input().split()))
lst = [False] * (m+1)

# 맨 처음 트루값
lst[s] = True

for i in songs:
	tmp = []
	for j, v in enumerate(lst):
		if v == True:
			tmp.append(j)
	for j in tmp:
		lst[j] = False
	for j in tmp:
		if j-i >= 0:
			lst[j-i] = True
		if j+i <= m:
			lst[j+i] = True

for i in range(len(lst)-1, -1, -1):
	if lst[i] == True:
		print(i)
		exit()
print(-1)

