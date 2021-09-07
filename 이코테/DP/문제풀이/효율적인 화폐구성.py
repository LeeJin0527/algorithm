n, m = map(int, input().split())
store = []
# [2, 3]
for i in range(n):
	store.append(int(input()))
d = [987654321] * (m+1)
d[0] = 0

for i in store:
	if i > m:
		continue
	d[i] = 1

for i in range(store[-1] + 1, m+1):
	for j, v in enumerate(store):
		if d[i - v] != 987654321:
			d[i] = min(d[i], d[i-v] + 1)
if d[m] == 987654321:
	print(-1)
else:
	print(d[m])