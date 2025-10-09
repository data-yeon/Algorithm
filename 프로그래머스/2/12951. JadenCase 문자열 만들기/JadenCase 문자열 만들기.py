def solution(s):
    answer = ''
    splited_str = s.split(' ')
    
    result = []
    for word in splited_str:
        if word =="":
            result.append("")
        elif word[0].isalpha():
            result.append(word.capitalize())
        else:
            result.append(word[0]+ word[1:].lower())
    answer = ' '.join(result)
    return answer