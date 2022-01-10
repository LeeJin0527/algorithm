import sys
input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n):
	lst.append(sys.stdin.readline().rstrip())
# 길이별로 정렬
lst.sort(key=lambda x: len(x))
flag = 0
cnt = 0
for i in range(len(lst)):
	for j in range(i+1, len(lst)):
		if lst[j].startswith(lst[i]):
			flag = 1
			break
	if flag == 1:
		flag = 0
		continue
	cnt +=1
print(cnt)