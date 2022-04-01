import sys
first = [0] * 26
second = [0] * 26
origin = list(sys.stdin.readline().rstrip())
compare = list(sys.stdin.readline().rstrip())
for i in origin:
	first[ord(i)-97] += 1
for i in compare:
	second[ord(i)-97] += 1
answer = 0
for i in range(26):
	answer += abs(first[i] - second[i])
print(answer)