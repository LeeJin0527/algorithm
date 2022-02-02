n, m = map(int, input().split())
lst = []
for i in range(n):
	lst.append(int(input()))
dice = []
for i in range(m):
	dice.append(int(input()))

# idx >= 9 : 종료
# idx 가 0 보다 작은건 없음
cnt = 0
curIdx = 0
for i in dice:
	curIdx += i
	cnt += 1
	if curIdx >= n-1:
		print(cnt)
		exit()
	if curIdx < 0:
		curIdx = 0
	if lst[curIdx] != 0:
		curIdx += lst[curIdx]
	if curIdx >= n-1:
		print(cnt)
		exit()



