n, m = map(int, input().split())

datas = list(map(int, input().split()))

ball = [0] * (m+1)

tmp = 0
cnt = 0
for data in datas:
	ball[data] +=1

sum = 0
for b in ball:
	sum += b
	cnt += b *(n -sum)

print(cnt)
