from sys import stdin
answer = ""
eachCountOfWord = 0
for input in stdin:
	for word in input.strip().split():
		if word == "<br>":
			answer += '\n'
			eachCountOfWord = 0
			continue
		if word == "<hr>":
			if eachCountOfWord != 0:
				answer += '\n'

			answer += f"{'-' * 80} \n"
			eachCountOfWord = 0
			continue
		if len(word) + eachCountOfWord > 80:
			answer += '\n'
			eachCountOfWord = 0

		answer += f"{word} "
		eachCountOfWord += len(word) + 1

for word in answer.split('\n'):
	print(word.strip())
