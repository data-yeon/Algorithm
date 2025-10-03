def solution(n):
    answer = 0
    
    def is_prime(n):
        if n<2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i ==0:
                return False 
        return True 
    
    for i in range(1, n+1):
        if i > 1 and not is_prime(i):
            answer+= 1 
            
    return answer