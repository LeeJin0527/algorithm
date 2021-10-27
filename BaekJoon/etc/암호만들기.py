from itertools import combinations
from collections import Counter
l, c = map(int, input().split())
password = list(input().split())
password.sort()
# print(password)
vowel = ['a', 'e', 'i', 'o', 'u']
for i in list(combinations(password, l)):
	count = 0
	for j in i:
		if j in vowel:
			count += 1
	if count >= 1 and count <= l-2:
		print(''.join(i))