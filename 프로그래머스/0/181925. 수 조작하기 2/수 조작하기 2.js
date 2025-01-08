function solution(numLog) {
    var answer = '';
    // numLog의 i번째 값과 i-1번째 값의 차이에 따라 조작을 결정 
    for (let i = 1; i < numLog.length; i++){
        let diff = numLog[i] - numLog[i-1]; 
        
        if (diff === 1){
            answer += 'w';  // 1을 더한 경우
        } else if (diff === -1 ){
            answer += 's';  // 1을 뺀 경우
        } else if (diff === 10) {
            answer += 'd';  // 10을 더한 경우
        } else if (diff === -10){
            answer += 'a';
        }
    }
    return answer;
}