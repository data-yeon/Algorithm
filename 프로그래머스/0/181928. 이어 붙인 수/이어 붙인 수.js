function solution(num_list) {
    var answer = 0
    let oddStr = '' //홀
    let evenStr = '' // 짝
    
    for (let num of num_list){
        if(num % 2 === 0 ){
            evenStr += num;  // 짝수일 때
        } else {
             oddStr += num;   // 홀수일 때 
        }
        
    }
     // 홀수와 짝수를 정수로 변환하여 합을 구함
    return parseInt(oddStr) + parseInt(evenStr);
}