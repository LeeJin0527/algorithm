x = int(input())
d = [300001] * 30001
d[1] = 0
d[2] = 1
for i in range(3, x+1):
	d[i] = min(d[i-1] + 1, d[i])
	if i % 2 == 0:
		d[i] = min(d[i// 2] + 1, d[i])
	if i % 3 == 0:
		d[i] = min(d[i// 3] + 1, d[i])
	if i % 5 == 0:
		d[i] = min(d[i// 5] + 1, d[i])
print(d[x])
