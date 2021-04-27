answer1 = int(input())
answer2 = input().split()

for i in range(answer1):
    answer2[i] = int(answer2[i])
    
temp =[]
for i in range( 24):
    temp.append(0)
    
for i in range(answer1):
    temp[answer2[i]] += 1
    
for i in range(1, 24):
    print(temp[i], end =' ')
