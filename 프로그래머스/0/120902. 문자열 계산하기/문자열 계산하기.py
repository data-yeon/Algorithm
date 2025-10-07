def solution(my_string):
    parts = my_string.split()
    answer = int(parts[0])
    
    for i in range (1,len(parts),2):
        op = parts[i]
        num = int(parts[i+1])
        
        if op == '+':
            answer += num
        elif op == '-':
            answer -= num
    return answer