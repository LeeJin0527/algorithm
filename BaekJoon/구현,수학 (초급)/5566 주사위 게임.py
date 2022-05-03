n, m = map(int,input().split())
lst = []
for _ in range(n):
	lst.append(int(input()))


move = []
for _ in range(m):
	move.append(int(input()))

start = 0
cnt = 0
for i in move:
	cnt += 1
	start += i
	if start < 0 or start > n-1:
		break
	start += lst[start]
	
	if start < 0 or start > n-1:
		break

print(cnt)
