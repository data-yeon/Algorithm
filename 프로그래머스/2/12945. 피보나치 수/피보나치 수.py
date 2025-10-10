# def solution(n):
#     answer = 0
    
#     return answer

def solution(n):
    answer= 0
    a , b = 0,1
    for i in range(n):
        a, b = b %1234567, (a+b) %1234567 
        answer =a 
    return a 
      