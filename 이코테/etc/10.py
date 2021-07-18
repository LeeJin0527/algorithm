array = [('바나나', 2), ('사과', 5), ('키위', 6)]

def setting(data):
	return data[1]

result = sorted(array, key = setting)

print(result)