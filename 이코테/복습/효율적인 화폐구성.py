n, m = map(int, input().split())
lst = []
for i in range(n):
	lst.append(int(input()))
d = [10001] * (m+1)
d[0] = 0
for i in range(n):
	for j in range(lst[i], m+1):
		if d[j - lst[i]] != 10001:
			d[j] = min(d[j-lst[i]] +1 , d[j])
if d[m] == 10001:
	print('-1')
else:
	print(d[m])