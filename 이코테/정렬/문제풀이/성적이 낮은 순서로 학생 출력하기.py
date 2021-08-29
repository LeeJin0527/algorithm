n = int(input())
array = []

for i in range(n):
	x, y = input().split()
	array.append((x, int(y)))

array.sort(key = lambda x : x[1])

for i in array:
	print(i[0], end = ' ')





