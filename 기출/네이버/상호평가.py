import numpy as np

def solution(scores):
	global final
	num = np.array(scores)
	num = num.T
	num = num.tolist()
	for i, v in enumerate(num):
		ma = max(v)
		mi = min(v)
		if v[i] == ma and v.count(ma) == 1:
			answer = (sum(v) - v[i]) / (len(v)-1)
		elif v[i] == mi and v.count(mi) == 1:
			answer = (sum(v) - v[i]) / (len(v)-1)

		elif v[i] == ma and v.count(ma) != 1:
			answer = sum(v) / len(v)
		elif v[i] == mi and v.count(mi) != 1:
			answer = sum(v) / len(v)
		else:
			answer = sum(v) / len(v)
		# print(answer)
		if answer >= 90:
			grade = 'A'
		elif answer >= 80:
			grade = 'B'
		elif answer >= 70:
			grade ='C'
		elif answer >= 50:
			grade ='D'
		else:
			grade ='F'
		final += grade
	return final


final = ''
