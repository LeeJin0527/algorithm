answer1 = int(input())
answer2 = input().split()

for i in range(answer1):
    answer2[i] = int(answer2[i])
for i in range(answer1):
    print(answer2[answer1 -1 - i], end =' ')

