# def solution(arr, divisor):
#     # answer = []
#     # return answer
def solution(arr, divisor):
    result = []  # divisor로 나누어 떨어지는 값을 저장할 리스트

    # arr의 각 원소를 순회하면서 나누어 떨어지는 값만 선택
    for num in arr:
        if num % divisor == 0:  # divisor로 나누어 떨어지는 경우
            result.append(num)

    # 결과가 비어있으면 -1을 담아 반환, 그렇지 않으면 정렬 후 반환
    if not result:
        return [-1]
    else:
        return sorted(result)