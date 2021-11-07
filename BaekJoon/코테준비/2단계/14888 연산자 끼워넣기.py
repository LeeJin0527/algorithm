n = int(input())
lst = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
maxResult, minResult = -1e9, 1e9
def dfs(v, result, add, sub, mul, div):
	if v == n:
		global maxResult, minResult
		maxResult = max(result, maxResult)
		minResult = min(result, minResult)
	else:
		if add:
			dfs(v+1, result+lst[v],add-1, sub, mul, div)
		if sub:
			dfs(v+1, result-lst[v], add, sub-1, mul, div )
		if mul:
			dfs(v+1, result*lst[v], add, sub, mul-1, div)
		if div:
			dfs(v+1, int(result/lst[v]), add, sub, mul, div-1)
dfs(1, lst[0], add, sub, mul, div)
print(maxResult)
print(minResult)