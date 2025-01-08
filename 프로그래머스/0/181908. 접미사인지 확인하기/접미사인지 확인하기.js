function solution(my_string, is_suffix) {
    var answer = 0;
        // 문자열이 특정 접미사로 끝나는지 확인
 if (my_string.endsWith(is_suffix)) {
        return 1;
    } else {
        return 0;
    }
}