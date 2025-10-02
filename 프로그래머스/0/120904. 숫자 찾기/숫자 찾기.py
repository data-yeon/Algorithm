def solution(num, k):
    s = str(num)
    k = str(k)
    if k in s:
        return s.index(k)+1
    else: 
        return -1