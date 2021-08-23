s = input()
x = int(s[1])
y = ord(s[0])


dx = [1, 1, -1, -1, -2, -2,  2, 2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]

count = 0

for i in range(8):
	nx = x + dx[i]
	ny = y + dy[i]
	count += 1
	if nx < 1 or nx > 8 or ny < 97 or ny > 104:
		count -= 1

print(count)



