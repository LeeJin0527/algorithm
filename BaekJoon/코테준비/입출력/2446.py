n = int(input())
for i in range(1, 2*n):
	if i > n:
		print((n-1-abs(n-i)) *' '+(2*abs(n-i)+1)*'*')
	else:
		print((i-1)*' '+ (2*n- (2*i-1))*'*')
