n = int(input())
data = list(map(int, input().split()))

target = 1
data.sort()


for d in range(n):
	if target < data[d]:
		break

	target += data[d]



print(target)
