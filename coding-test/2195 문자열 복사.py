import sys
input = sys.stdin.readline
s = input().rstrip()
p = input().rstrip()

index = 0
answer = 0

while index < len(p):
	copy = ''
	if s.find(p[index:]) != -1:
		answer += 1
		break
	for j in range(index, len(p)):
		copy += p[j]
		if s.find(copy) == -1:
			answer += 1
			index = j
			break
print(answer)
