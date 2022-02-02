def solution(sizes):
    first = sizes[0]
    first.sort()
    for size in sizes:
        size.sort()
        if size[0] > first[0] :
            first[0] = size[0]
        if size[1] > first[1]:
            first[1] = size[1]
            
    answer =first[0]*first[1]
    return answer
