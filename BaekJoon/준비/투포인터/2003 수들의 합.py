import sys
input= sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
end = 0
interval = 0
cnt = 0
for start in range(len(lst)):
	while end < n and interval < m:
		interval += lst[end]
		end += 1
	if interval == m:
		cnt += 1
	interval -= lst[start]
print(cnt)
