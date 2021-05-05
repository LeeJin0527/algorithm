N, L = map(int,input().split())
x = 0

while(True):
	x = (N - ((L-1)*L //2)) % L
	y = (N - ((L-1)*L //2)) // L
	if x == 0:
		if L > 100 or y < 0 :
			print(-1)
			break
		else:
			for i in range(L):


				print(y + i , end=' ')

			break
	else:
		L = L+1
		if L > 100 or y < 0 :
			print(-1)
			break





