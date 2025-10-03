def solution(age):
    
    table = ['a','b','c','d','e','f','g','h','i','j']
    answer = ''
    for ch in str(age):
        answer += table[int(ch)]
    return answer