answer1 = int(input())
answer2 = input().split()

for i in range(answer1):
    answer2[i] = int(answer2[i])
    
temp = answer2[0]

for i in answer2:
    if i < temp:
        temp = i
print(temp)

    
