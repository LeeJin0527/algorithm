n, m = map(int, input().split())
package =  []
each = []
for i in range(m):
	x, y = map(int, input().split())
	package.append(x)
	each.append(y)

share = n // 6
reminder = n % 6
answer = min(((share * min(package)) + min(reminder * min(each), min(package))), min(each)* n)
print(answer)