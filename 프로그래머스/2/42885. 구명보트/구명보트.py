def solution(people, limit):
    people.sort()  # 무게를 오름차순으로 정렬
    left = 0  # 가장 가벼운 사람을 가리키는 포인터
    right = len(people) - 1  # 가장 무거운 사람을 가리키는 포인터
    boats = 0  # 필요한 보트 개수

    while left <= right:
        # 가장 가벼운 사람 + 가장 무거운 사람 <= 무게 제한인 경우
        if people[left] + people[right] <= limit:
            left += 1  # 가벼운 사람도 태움
        # 가장 무거운 사람은 태우고 이동
        right -= 1
        boats += 1  # 보트 사용 개수 증가

    return boats