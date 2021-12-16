n, k = map(int, input().split())
lst = []
for i in range(n):
	lst.append(int(input()))
lst.sort()
d = [10001] * (k+1)
d[0] = 1
for i in lst:
	for j in range(i, k+1):
		if j >= i:
			if j % i == 0:
				d[j] = min((j // i), d[j])
			else:
				d[j] = min(d[j], d[j-i]+1)

if d[k] == 10001:
	print(-1)
	exit()
print(d[k])