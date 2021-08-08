data = list(map(int, input()))
# print(data)
start = data[0]

group = 0

for i in range(1, len(data)):
	if data[i] != start:
		start = data[i]
		group += 1

if group % 2 == 0:
	group = group //2
else:
	group = group//2 +1
print(group)





