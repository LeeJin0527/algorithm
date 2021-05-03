N = int(input())
P = list(map(int, input().split()))

tmp = sorted(P)
#print(tmp)
sum =0
accu = 0
for i in range(N):
	sum += tmp[i]
	accu += sum
print(accu)

