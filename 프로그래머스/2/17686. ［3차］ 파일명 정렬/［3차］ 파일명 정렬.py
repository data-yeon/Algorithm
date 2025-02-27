def solution(files):
    answer = []
    # 파일명을 HEAD, NUMBER, TAIL로 나누는 함수
    def split_filename(filename):
        head, number, tail = "", "", ""
        i = 0
        length = len(filename)

        # HEAD 추출: 숫자가 나오기 전까지
        while i < length and not filename[i].isdigit():
            head += filename[i]
            i += 1
        # NUMBER 추출: 최대 5자리까지의 연속된 숫자
        while i < length and filename[i].isdigit():
            number += filename[i]
            i += 1
            if len(number) == 5:  # 최대 5자리까지만 허용
                break
        # TAIL 추출: 남은 부분
        tail = filename[i:]

        return [head, number, tail]

    # 정렬 키 함수 정의
    def key_func(file):
        head, number, tail = split_filename(file)
        return (head.lower(), int(number))  # HEAD는 대소문자 무시, NUMBER는 정수 변환
    
    # 파일 정렬 후 answer에 저장
    answer = sorted(files, key=key_func)  
    #sorted(files, key=key_func) 실행 → 
    # files 리스트의 각 요소(파일명)가 key_func()에 전달됨.
    return answer  # ✅ 정렬된 리스트 반환
