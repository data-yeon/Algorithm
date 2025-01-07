def solution(elements):
  answer = set()
  n = len(elements)
  extended_elements = elements * 2 

  for length in range(1, n + 1):
    current_sum = sum(extended_elements[0:length])
    answer.add(current_sum)

    # 시작 인덱스를 1부터  n-1 까지 순회하면서 슬라이딩 윈도우 적용
    for start in range(1, n):
      # 이전 합에서 앞의 원소를 빼고 새로운 원소를 더함 
      current_sum -= extended_elements[start - 1]
      current_sum += extended_elements[start + length - 1]

      answer.add(current_sum)

  return len(answer)