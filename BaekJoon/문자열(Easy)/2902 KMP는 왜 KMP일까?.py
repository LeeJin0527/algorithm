import sys
lst = list(sys.stdin.readline().rstrip().split("-"))
answer = ''
for i in lst:
	answer += i[0]
print(answer)