def solution(queue1, queue2):
    # 두 큐의 합 계산
    total_sum = sum(queue1) + sum(queue2)
    
    # 합이 홀수라면 균형을 맞출 수 없으므로 -1 반환
    if total_sum % 2 != 0:
        return -1
    
    # 목표 합 설정
    target_sum = total_sum // 2
    
    # 두 큐를 이어 붙여서 하나의 리스트로 만듦
    combined_queue = queue1 + queue2
    n = len(queue1)
    
    # 슬라이딩 윈도우를 위한 변수 초기화
    start, end = 0, n  # start는 queue1의 시작, end는 queue2의 시작
    current_sum = sum(queue1)  # 초기 합은 queue1의 합
    min_operations = 0
    
    # 슬라이딩 윈도우로 합을 맞추는 최소 연산 횟수 찾기
    while start < len(combined_queue) and end < len(combined_queue):
        if current_sum == target_sum:
            return min_operations
        elif current_sum < target_sum:
            # current_sum이 목표보다 작으면 end를 증가시키며 요소 추가
            current_sum += combined_queue[end]
            end += 1
        else:
            # current_sum이 목표보다 크면 start를 증가시키며 요소 제거
            current_sum -= combined_queue[start]
            start += 1
        min_operations += 1
    
    # 모든 경우를 탐색했는데도 합을 맞출 수 없는 경우
    return -1
