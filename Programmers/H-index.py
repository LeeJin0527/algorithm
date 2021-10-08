def solution(citations):
	citations.sort()
	visited = [False for _ in range(max(citations)+1)]
	for i in range(len(visited)):
		visited[i] = (len([v for v in citations if i <= v]))

	for i, v in enumerate(visited):
		if i > v:
			break
		tmp = i
	answer = tmp
	return answer


