n = int(input())
k = list(map(int, input().split()))

d = [0] * (n+1)
d[1] = k[0]
d[2] = max(k[0], k[1])

for i in range(3, n+1):
	d[i] = max(d[i-1], d[i-2] + k[i-1])

print(d[n])
