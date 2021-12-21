n = int(input())
lst = list(map(int, input().split()))
print(lst)

d = [0] * (n+1)
d[0] = lst[0]
d[1] = max(lst[0],lst[1])

for i in range(2, n):
	d[i] = max(d[i-1], lst[i] + d[i-2])
print(d[n-1])

