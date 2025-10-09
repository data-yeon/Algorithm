def solution(bin1, bin2):
   
    i = len(bin1) -1
    j = len(bin2) -1 
    carry = 0
    result = ''
    
    while i >= 0 or j>= 0 or carry:
        b1 = int(bin1[i]) if i >= 0 else 0
        b2 = int(bin2[j]) if j >= 0 else 0 
        
        total = b1 + b2 + carry 
        carry = total //2 
        result = str(total% 2) + result
        
        i -=1
        j -=1
    return result