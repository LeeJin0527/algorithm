n = int(input())
for i in range(1, n):
	if i == 1:
		print((n-i)*' '+'*'+' '*(2*i-3))
	else:
		print((n-i)*' '+'*'+' '*(2*i-3)+'*')

print((2*n-1)*'*')