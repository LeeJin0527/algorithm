n = int(input())
lst = list(map(int, input().split()))
d = [0] * 101
d[0] = lst[0]
d[1] = max(lst[0], lst[1])
for i in range(2, n):
	d[i] = max(lst[i] + d[i-2], d[i-1])
print(d[n-1])