def solution(my_string):
    answer = ''
    chs = []
    same_ch = []
    for ch in my_string:
        if ch in chs:
            same_ch.append(ch)
        else:
            chs.append(ch)
            answer += ch
    return answer