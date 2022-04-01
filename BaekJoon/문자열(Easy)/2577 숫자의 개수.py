import sys
a = int(input())
b = int(input())
c = int(input())
result  = a * b * c

answer = [0] * 10
for i in list(str(result)):
	answer[int(i)] += 1
for i in answer:
	print(i)