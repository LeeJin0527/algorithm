import sys
input = sys.stdin.readline
n, m = map(int, input().split())
gcd = []
lcm = []
for i in range(1, min(n, m)+1):
	if (n % i) == 0 and (m % i) == 0:
		gcd.append(i)
m_gcd = max(gcd)
a = n // m_gcd
b = m // m_gcd
m_lcm = m_gcd * a * b
print(m_gcd)
print(m_lcm)


