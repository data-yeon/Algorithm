def solution(s):
    s_word = s.split()
    stack = []
    for i in s_word:
        if i == "Z":
            if stack: 
                stack.pop()
        else:
            stack.append(int(i))        
    return sum(stack)