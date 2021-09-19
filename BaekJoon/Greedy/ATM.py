n = int(input())
line = list(map(int, input().split()))
# 1 2 3 3 4
line.sort()
# print(line)
answer =[]

sum = 0
accu = 0
for i, v in enumerate(line):
	sum += v
	accu += sum

print(accu)