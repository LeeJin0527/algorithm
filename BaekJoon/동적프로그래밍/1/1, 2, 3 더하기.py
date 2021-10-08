n = int(input())
graph = []
for i in range(n):
	graph.append(int(input()))
answer =[[] for _ in range(max(graph) + 1)]
answer[1] = 1
answer[2] = 2
answer[3] = 4
for i in range(4, len(answer)):
	answer[i] = (answer[(i-1)] + answer[(i-2)] + answer[(i-3)])
for i in graph:
	print(answer[i])


