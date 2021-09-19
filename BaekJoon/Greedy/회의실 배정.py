n = int(input())
line = []
for i in range(n):
	line.append(list(map(int, input().split())))

line = sorted(line, key = lambda x : (x[1], x[0]) )
i = 0
cnt = 1
for j in range(1, n):

	if(line[j][0] >= line[i][1]):
		cnt += 1
		i = j

print(cnt)