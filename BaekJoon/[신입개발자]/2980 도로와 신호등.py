import sys
input = sys.stdin.readline
n, l = map(int, input().split())
cur = 0
time = 0
lst = []
for _ in range(n):
	lst.append(list(map(int, input().split())))

while True:
	if cur == l:
		break
	cur += 1
	time += 1
	for i in range(len(lst)):
		if cur == lst[i][0]:
			if time % (lst[i][1] + lst[i][2]) < lst[i][1]:
				time += lst[i][1] - (time % (lst[i][1] + lst[i][2]))
			break
print(time)