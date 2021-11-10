import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
words = [0] * n

base = ['a', 'n', 't', 'i', 'c']

for i in range(n):
	word = list(input())[4:-4]
	for ch in word:
		words[i] |= (1 << ord(ch) - ord('a'))
compare = []
for i in range(97, 123):
	compare.append(chr(i))
compare = list(set(compare) - set(base))
answer = 0
if m < 5:
	pass
else:
	case = list(combinations(compare, m-5))
	for c in case:
		make = 0
		for ch in base:
			make |= (1 << ord(ch)- ord('a'))
		for ch in c:
			make |= (1 << ord(ch) -ord('a'))
		count = 0
		for i in range(len(words)):
			if words[i] & make == words[i]:
				count += 1
		answer = max(answer, count)
print(answer)


