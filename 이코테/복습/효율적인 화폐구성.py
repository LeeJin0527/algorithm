n, m = map(int, input().split())
d = [10001] * (m+1)
d[0] = 0
lst = []
for i in range(n):
	lst.append(int(input()))
for i in range(n):
	for j in range(lst[i], m+1):
		if d[j - lst[i]] != 10001:
			d[j] = min(d[j], d[j - lst[i]] + 1)
if d[m] != 10001:
	print(d[m])
else:
	print(-1)
