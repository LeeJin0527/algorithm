answer1 = int(input())

d = [[0 for j in range(20)] for i in range(20)]
for i in range(answer1):
    answer2= input().split()
    for j in range( answer1):
        d[int(answer2[0])][int(answer2[1])] = 1
        
    



for i in range(1,20):
    for j in range(1,20):
        print(d[i][j], end =' ')
    print()

