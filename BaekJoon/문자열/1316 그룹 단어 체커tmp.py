n = int(input())
line = []
visited = [[False] * 27 for _ in range(n)]

for i in range(n):
	line.append(input())

for i, v in enumerate(line):
	line[i] = list(v)

for i in range(n):
	for j, v in enumerate(line[i]):
		line[i][j] = ord(v) -97

cnt = n
for i in range(n):
	for j, v in enumerate(line[i]):
		if (visited[i][line[i][j]] == False):
			visited[i][line[i][j]] = True
		else:
			if line[i][j] != line[i][j-1]:
				cnt -= 1
				break
print(cnt)