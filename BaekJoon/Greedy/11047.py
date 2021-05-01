N, K = map(int, input().split())
A = [map(int, input().split()) for _ in range(N)]

tmp = []
rem = K
cnt = 0
suma = 0
remcnt = 0

for i in range(N):
	tmp.append(*A[N -i -1])
#print(tmp)

for i, v in enumerate(tmp):

	if tmp[i] <= rem: # 잔액이 단위보다 크면

		cnt = rem // tmp[i]

		remcnt += cnt

		suma += cnt * tmp[i]
		rem = K - suma
		i += 1

		if suma == K:
			break
print(remcnt)











