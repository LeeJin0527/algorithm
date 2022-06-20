import sys
input = sys.stdin.readline
n, m = map(int, input().split())
knowGroup = set(list(map(int, input().split()))[1:])
parties = []
for _ in range(m):
	parties.append(set(list(map(int, input().split()))[1:]))
for _ in range(m):
	for party in parties:
		if party & knowGroup:
			knowGroup = knowGroup.union(party)
cnt = 0
for party in parties:
	if knowGroup & party:
		continue
	cnt += 1
print(cnt)
