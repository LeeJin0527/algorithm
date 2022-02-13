
n = int(input())
lst = []
paper = [[0]*101 for _ in range(101)]
for _ in range(n):
	a, b = map(int, input().split())
	for i in range(a, a+10):
		for j in range(b, b+10):
			paper[i][j] = 1
cnt = 0
for i in range(101):
	for j in range(101):
		if paper[i][j] == 1:
			cnt += 1
print(cnt)