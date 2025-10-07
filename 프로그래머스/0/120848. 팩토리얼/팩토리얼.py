def factorial(n): 
    answer = 1
    for i in range(n,0,-1):
        answer *= i
    return answer 

def solution(n):
    i = 1 
    while True:
        if factorial(i)>n:
            return i -1
        i += 1