def dfs(word, cur):
	global cnt
	global x
	if cur == word:
		x = cnt
		return cnt
	if len(cur) >= 5:
		return
	for i in range(5):
		nx = cur + lst[i]
		cnt += 1
		if nx not in visited:
			visited.append(nx)
			dfs(word, nx)

def solution(word):
	global x
	dfs(word, '')
	answer = x
	return answer


cnt = 0
lst = ['A', 'E', 'I', 'O', 'U']
visited = []