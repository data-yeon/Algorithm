function solution(n, k) {
    var answer = [];
    
    for (let i=1; k*i<=n; i++){
     answer.push(k * i); // k * i가 n보다 작거나 같으면 배열에 추가
    }
    return answer;
}