def solution(cipher, code):
    answer = ''
    for i, ch in enumerate(cipher, start=1 ): 
        if i%code==0:
            answer+= ch
    return answer