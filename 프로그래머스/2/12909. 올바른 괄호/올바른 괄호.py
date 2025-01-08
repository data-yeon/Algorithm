def solution(s):
    stack = []
    for i in s: 
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else : 
                return False # 스택이비었는데 닫는괄호가 나옴 
    return not stack # 스택이 비어있으면 True, 아니면 False 
    
    