# 반복적으로 구현한 n!
def factorial_iterative(n):
	result = 1
	# 1부터 n까지의 수를 차례대로 곱하기
	for i in range(1, n+1):
		result *= i
	return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
	if n <= 1:
		return 1


	# n! = n * (n-1)!
	return n * factorial_iterative(n-1)

print(factorial_recursive(5))
print(factorial_iterative(5))