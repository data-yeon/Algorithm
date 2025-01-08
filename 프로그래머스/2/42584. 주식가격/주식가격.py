def solution(prices):
    n = len(prices) # 주식가격의 길이
    answer = [0] * n # 가격이 떨어지지않은 기간 저장할 배열
    stack = [] # 인덱스를 저장해서 비교
    
    #스택엔 가격이 떨어지지않은 시점의 인덱스를 저장
    
    for i in range(n): 
        # 스택이 있고,
        # 마지막 인덱스 stack[-1] 는 아직 가격이 떨어지지않은 상태
        # 현재 시점 가격이 스택에 저장된 마지막 시점보다 떨어지면 
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j 
            
        stack.append(i)
    
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j 
        
    return answer