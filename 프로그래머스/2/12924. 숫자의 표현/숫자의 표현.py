def solution(n):
    answer = 0
    for i in range(1, n+1):
        current_sum = 0
        j = i
        while current_sum < n:
            current_sum += j
            j += 1
        if current_sum == n:
            answer += 1
    return answer