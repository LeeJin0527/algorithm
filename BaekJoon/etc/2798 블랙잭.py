from itertools import combinations

n , m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
answer = []
for i in list(combinations(lst, 3)):
	if sum(i) > m:
		continue
	answer.append(sum(i))
answer.sort()
print(answer[-1])