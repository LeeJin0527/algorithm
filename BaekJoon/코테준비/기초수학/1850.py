import math
a, b = map(int, input().split())
k = math.gcd(a, b)
print(k)
for i in range(k):
	print(1, end ='')