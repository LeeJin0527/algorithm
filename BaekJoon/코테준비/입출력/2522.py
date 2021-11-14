n = int(input())
for i in range(1, 2*n):
	if i > n:
		print(abs(i-n)*' '+ (n - abs(n-i))*'*')
	else:
		print(abs(n-i)*' '+i*'*')

