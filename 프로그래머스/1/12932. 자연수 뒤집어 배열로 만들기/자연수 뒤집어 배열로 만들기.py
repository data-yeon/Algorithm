def solution(n: int) -> list:
  result = []

  # n이 0이 될 때까지 반복
  while n > 0:
    last_digit = n % 10 
    result.append(last_digit)
    n = n // 10 
  return result