import sys
input = sys.stdin.readline
a, b, c, m = map(int, input().split())

cnt = 0
work = 0
now = 0
if a > m:
	print(0)
	exit()
while cnt != 24:
	cnt +=1
	if now + a <= m:
		now += a
		work += b
	else:
		if now - c >= 0:
			now -= c
		else:
			now = 0

print(work)