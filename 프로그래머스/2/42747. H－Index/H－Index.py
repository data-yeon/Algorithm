def solution(citations):
    citations.sort(reverse=True)  # 인용 횟수를 내림차순 정렬
    h_index = 0  # H-Index 값 초기화
    # answer = 0
    # return answer
    
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h_index = i + 1 
        else:
            break  # H-Index 조건을 만족하지 않으면 중단

    return h_index
        