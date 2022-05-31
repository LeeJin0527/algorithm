import sys
input = sys.stdin.readline
n = int(input())

lst = []
lst = list(input().rstrip())

lst.insert(0, 0)

score = 0
bonusScore = 0
for i in range(1, len(lst)):
	if lst[i] == 'X':
		bonusScore = 0
	elif lst[i] == 'O':
		score += i
		score += bonusScore
		bonusScore += 1
print(score)
