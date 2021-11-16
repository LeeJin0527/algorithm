n = int(input())
j = 2
while j <= n:
	if n % j == 0:
		print(j)
		n = n // j
	else:
		j += 1