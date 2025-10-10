def solution(s):
    transform_count = 0
    removed_zero = 0 
    
    while s != "1":
        zero_count = s.count("0")
        removed_zero += zero_count
        s = s.replace("0", "")
        length = len(s)
        s = bin(length)[2:]
        transform_count +=1 
        
    return [transform_count, removed_zero]