n, m = map(int, input().split())
tmp = min(n, m)
gcd = 0
for i in range(tmp, 0, -1):
	if n % i == 0 and m % i == 0:
		gcd = i
		break

n = n// gcd
m = m // gcd
lcm = gcd* n* m
print(gcd)
print(lcm)