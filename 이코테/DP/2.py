d = [0] * 100
def pibo(x):
	if x == 1 or x == 2:
		return 1
	if d[x] != 0:
		return d[x]
	d[x] = pibo(x-2) +pibo(x-1)
	return d[x]
print(pibo(99))