import sys
input = sys.stdin.readline
answer = [0]
for i in range(1, 10):
	x, y = map(int, input().split())
	answer.append(answer[i-1] - x + y)
print(max(answer))