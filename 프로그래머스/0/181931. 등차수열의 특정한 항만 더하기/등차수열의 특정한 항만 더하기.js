function solution(a, d, included) {

    let sum = 0; 
    for (let i=0; i<included.length; i++){
        // i 번째 항은  a + i * d 로 계산됨
        const term = a + i * d;
        // included[i]가 true이면 그 항을 더함
        if(included[i]){
            sum += term;
            
        }
    }
    
    return sum;
}