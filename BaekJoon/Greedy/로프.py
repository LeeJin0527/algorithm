n = int(input())
line = []
for i in range(n):
	line.append(int(input()))
line.sort()
# print(line)
answer =[]
for i, v in enumerate(line):
	answer.append(v * (n-i))
print(max(answer))
