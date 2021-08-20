# 나의 풀이
s = list(map(int, input()))

cnt = 0
start = s[0]
for i in range(1, len(s)):
	if s[i] != start:
		cnt += 1
		start = s[i]

if cnt % 2 == 0 :
	cnt = cnt //2
else:
	cnt = cnt // 2 + 1
print(cnt)
# 책 풀이
# s = list(map(int, input()))
# count0 = 0 # 문자열을 모두 0으로 만드는데 드는 비용
# count1 = 0 # 문자열을 모두 1로 바꾸는데 드는 비용
#
# if s[0] == 1:
# 	count0 += 1
# else:
# 	count1 +=1
#
# for i in range(len(s)-1):
# 	if s[i] != s[i+1]:
# 		if s[i+1] == 0:
# 			count1 +=1
# 		else:
# 			count0 +=1
#
# print(min(count0, count1))