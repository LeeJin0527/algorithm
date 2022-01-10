import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = []
compare = []
for i in range(n):
	lst.append(sys.stdin.readline().rstrip())
for i in range(m):
	compare.append(sys.stdin.readline().rstrip())
lst.sort(key=lambda x:len(x))
compare.sort()
tmp = []
for i in lst:
	tmp.append(i[0])
cnt = 0
flag = 0
for i in range(len(compare)):
	try:
		for j in range(tmp.index(compare[i][0]), len(lst)):
			if lst[j].startswith(compare[i]):
				cnt += 1
				break
	except:
		continue

print(cnt)