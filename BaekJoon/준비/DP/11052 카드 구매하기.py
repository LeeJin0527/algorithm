import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
print(lst)

maxDp = [1] * (n+1)
minDp = [1] * (n+1)
for i in range(n):
	for j in range(i):
		if lst[i] > lst[j]:
			maxDp[i] = max(maxDp[j]+1, maxDp[i])
print(maxDp)

for i in range(n):
	for j in range(i):
		if lst[i] < lst[j]:
			print(i, j )
			minDp[i] = max(minDp[j]+1, minDp[i])

print(minDp)

