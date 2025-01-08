def solution(sequence, k):
    left, right = 0, 0
    current_sum = sequence[0]
    best_range = (0, len(sequence))  # 가장 짧은 구간을 저장할 변수 초기화

    while left < len(sequence) and right < len(sequence):
        # 현재 합이 k와 같을 때, 최적 구간을 갱신
        if current_sum == k:
            # 길이가 더 짧은 구간 또는 시작 인덱스가 더 작은 구간 선택
            if (right - left < best_range[1] - best_range[0]) or \
               (right - left == best_range[1] - best_range[0] and left < best_range[0]):
                best_range = (left, right)

            # 다음 구간 탐색을 위해 left 포인터 이동
            current_sum -= sequence[left]
            left += 1
        elif current_sum < k:
            # 합이 k보다 작으므로 right를 이동하여 합을 늘림
            right += 1
            if right < len(sequence):
                current_sum += sequence[right]
        else:
            # 합이 k보다 크므로 left를 이동하여 합을 줄임
            current_sum -= sequence[left]
            left += 1

    return [best_range[0], best_range[1]]