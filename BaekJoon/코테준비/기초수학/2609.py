n, m = map(int, input().split())
start = min(n, m)
gcd = 0
lcm = 0
for i in range(start, 0, -1):
	if ((n % i) == 0) and ((m % i) == 0):
		gcd = i
		break
a, b = n // gcd, m // gcd
lcm = gcd * a* b
print(gcd)
print(lcm)
