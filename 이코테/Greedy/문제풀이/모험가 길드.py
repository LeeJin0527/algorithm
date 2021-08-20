n = int(input())
data = list(map(int, input().split()))

data.sort()

group = 0
cnt = 0
# 1 2 2 2 3
for i in range(n):
	cnt += 1

	if data[i] == cnt:
		group += 1
		cnt = 0
print(group)