def pibo(x):
	if x == 1 or x == 2:
		return 1
	return pibo(x-1) + pibo(x-2)
print(pibo(4))