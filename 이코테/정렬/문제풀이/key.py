import operator
array = [('바나나', 2), ('사과', 2), ('딸기', 3)]

def setting(data):
	return data[1]

#함수 매개변수를 key에 안넣음!!!
result = sorted(array, key = setting)

print(result)