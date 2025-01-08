function solution(number) {
    var answer = 0;
    for (let i =0; i < number.length; i++){
        answer += Number(number[i]); // 문자열의 각 자릿수를 숫자로 변환하여 더함
    }
    return answer % 9 ;
}