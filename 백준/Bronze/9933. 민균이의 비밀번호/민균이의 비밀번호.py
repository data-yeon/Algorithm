N = int(input().strip())
words = [input().strip() for _ in range(N)]  # 단어를 리스트로 저장
# 단어 목록에서 비밀번호 찾기
for word in words:
    # 현재 단어 word를 뒤집은 문자열을 reversed_word에 저장
    reversed_word = word[::-1]  # [::-1]은 문자열을 뒤집는 파이썬 슬라이싱 방법

    # 만약 뒤집힌 단어 reversed_word가 words 목록에 포함되어 있다면,
    # 이 단어가 비밀번호라는 뜻이므로 조건을 만족함
    if reversed_word in words:
        # word의 길이를 length 변수에 저장
        length = len(word)

        # 단어의 길이가 항상 홀수이므로 가운데 글자를 찾기 위해
        # 가운데 인덱스를 length // 2로 계산하여 middle_char에 저장
        middle_char = word[length // 2]  # 인덱스는 0부터 시작하므로 중앙 인덱스가 length // 2가 됨

        # 비밀번호의 길이와 가운데 글자를 출력
        print(length, middle_char)

        # 유일한 답이 보장되므로, 답을 찾으면 즉시 루프를 종료하여 불필요한 검사를 방지
        break