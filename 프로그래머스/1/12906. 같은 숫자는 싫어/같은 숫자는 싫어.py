def solution(arr):
    answer = []
    for num in arr:
        # answer가 비어있거나, 이전 숫자와 현재 숫자가 다를 때만 추가
        if not answer or answer[-1] != num:
            answer.append(num)
    return answer