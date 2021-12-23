import sys
def getPI(pattern):
	j = 0
	for i in range(1, len(pattern)):
		while j > 0 and pattern[i] != pattern[j]:
			j = pi[j - 1]
		if pattern[i] == pattern[j]:
			j += 1
			pi[i] = j

def KMP(s, pattern):
	getPI(pattern)
	j = 0
	for i in range(len(s)):
		while j > 0 and s[i] != pattern[j]:
			j = pi[j - 1]
		if s[i] == pattern[j]:
			if j == len(pattern) - 1:
				return True
			else:
				j += 1
	return False

s = sys.stdin.readline().rstrip()
pattern = sys.stdin.readline().rstrip()

pi = [0 for x in range(len(pattern))]
if KMP(s, pattern):
	print('1')
else:
	print('0') 
