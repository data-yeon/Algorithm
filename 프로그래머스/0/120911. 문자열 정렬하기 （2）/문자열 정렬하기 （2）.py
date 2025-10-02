def solution(my_string):
    answer = ''
    for ch in my_string:
        if ch.islower():
            answer +=ch
        elif ch.isupper():
            answer+=ch.lower()
        else: 
            answer.append(ch)
    return ''.join(sorted(answer))