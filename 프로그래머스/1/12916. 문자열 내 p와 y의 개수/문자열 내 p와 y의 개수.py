def solution(s):
    # 모든 문자를 소문자로 변환
    s = s.lower()
    # 'p'의 개수와 'y'의 개수를 비교
    return s.count('p') == s.count('y')