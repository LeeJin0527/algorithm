import sys
def five(n):
	result = 0
	j = 5
	while j <= n:
		result += n // j
		j = j * 5
	return result


def two(n):
	result = 0
	j = 2
	while j <= n:
		result += n // j
		j = j * 2
	return result

n, m = map(int, input().split())
a = five(n) - five(n-m) -five(m)
b = two(n) - two(n-m) -two(m)
print(min(a, b))