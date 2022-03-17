import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
delete = int(input())
def dfs(delete):
	lst[delete] = -2
	for i in range(len(lst)):
		if delete == lst[i]:
			dfs(i)

dfs(delete)
cnt = 0
for i in range(len(lst)):
	if lst[i] != -2 and i not in lst:
		cnt += 1
print(cnt)