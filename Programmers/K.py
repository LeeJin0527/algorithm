https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    temp =[]
    
    for i, v in enumerate(commands):
        # print(i)
        temp.append(array[commands[i][0]-1:(commands[i][1])])
        
    for i in temp:
        i.sort()
    
    # print(temp)
    
    for i, v in enumerate(temp):
        
        answer.append(v[commands[i][2]-1])
        
    # print(answer)
    return answer
