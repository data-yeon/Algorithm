def solution(my_string):
    answer = 0
    buf = ''
    for s in my_string:
        if s.isdigit():
            buf += s 
        else: 
            if buf: 
                answer += int(buf)
                buf = ''
    if buf: 
        answer += int(buf)
    return answer 