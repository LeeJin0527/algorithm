n = int(input())

data = []
for i in range(n):
	data.append(input().split())

def setting(data):
	return int(data[1])

result = sorted(data, key = setting)
for i in result :
	print(i[0], end = ' ')

