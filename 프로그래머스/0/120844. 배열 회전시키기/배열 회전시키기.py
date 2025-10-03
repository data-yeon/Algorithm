def solution(numbers, direction):
    n = len(numbers)
    answer = [0]*n
    if direction == "right":
        answer[0] = numbers[-1]
        for i in range(n-1):
            answer[i+1] = numbers[i]
            
    elif direction == "left":
        answer[-1] = numbers[0]
        for i in range(1,n):
            answer[i-1] = numbers[i]
    return answer