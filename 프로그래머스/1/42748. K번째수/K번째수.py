def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command 
        sub_array = array[i - 1:j]  # i부터 j까지의 배열을 슬라이싱
        sub_array.sort()  # 정렬
        answer.append(sub_array[k - 1])  # k번째 값을 결과에 추가
    return answer
