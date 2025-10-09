def solution(s):
    nums = list(map(int, s.split()))  # 문자열 → 정수 변환
    min_value = nums[0]
    max_value = nums[0]

    for x in nums:
        if x < min_value:
            min_value = x
        if x > max_value:
            max_value = x

    return f"{min_value} {max_value}"  # "최솟값 최댓값" 순서