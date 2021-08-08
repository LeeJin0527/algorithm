# 소수 판별 함수
def is_prime_number(x):
	# 2부터 (x-1) 까지의 모든 수를 확인하며
	for i in range(2, x):
		if x % i == 0 :
			return False
	return True

print(is_prime_number(4))
print(is_prime_number(7))