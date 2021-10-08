def solution(n, times):
    left = 0
    answer = right = max(times) * n
    while left <= right:
        compare = 0
        mid = (left + right )// 2
        for i in times:
            compare += mid // i
        if compare < n:
            left = mid + 1
        else:
            right = mid -1
            if mid < answer:
                answer = mid
                
    return answer
