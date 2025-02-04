def solution(array, commands):
    answer = []
    for a,b,c in commands:
        tmp_arr = array[a-1:b]
        tmp_arr.sort()
        answer.append(tmp_arr[c-1])
    return answer