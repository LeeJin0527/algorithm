def recursive_function(i):
	if i == 100:
		return

	print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다')
	recursive_function(i+1)
	print(i, '번째 재귀함수를 종료합니다')

recursive_function(1)



# 한계를 벗어났기 때문에 에러
# RecursionError: maximum recursion depth exceeded while calling a Python object