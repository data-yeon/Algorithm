function solution(n) {
    var answer = 0;
    
    //n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 
    if(n % 2 === 1){
        for(let i = 1; i<=n; i++){
            if(i % 2 ===1 ){
            answer += i;
            }
        }
    } else if(n % 2 === 0) {
         //n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return
        for(let i = 1; i<=n; i++){
            if (i % 2 === 0 ){
            answer += i**2;
            }
        }
    }
   
    return answer;
}