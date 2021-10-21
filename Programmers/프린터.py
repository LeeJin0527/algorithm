def solution(priorities, location):
    priorities = [[v, i] for i, v in enumerate(priorities)]
    i = 0
    h = []
    while True:
        if len(priorities) == 1:
            h.append(priorities[i])
            break
        if priorities[i][0] != (max(priorities)[0]):
            priorities = priorities[i+1:] + [priorities[i]]
        else:
            h.append(priorities[i])  
            priorities = priorities[i+1:]  
    for i, v in enumerate(h):
        if v[1] == location:
            return i+1
