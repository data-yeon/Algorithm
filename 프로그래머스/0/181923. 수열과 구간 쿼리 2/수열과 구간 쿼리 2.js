function solution(arr, queries) {
    var answer = [];
    
    // 각 쿼리를 처리 
    for (let [s,e,k] of queries) {
        let minVal = Infinity;  
        // k보다 큰 값 중 가장 작은 값을 저장할 변수
        let found = false;      
        // k보다 큰 값을 찾았는지 여부
        
        // s에서 e까지 범위 안에서 k보다 큰 값 중 가장 작은 값 찾기 
        for (let i = s; i <= e; i++){
            //
            if (arr[i] > k && arr[i] < minVal) {
                minVal = arr[i];
                found = true;  // k보다 큰 값을 찾았음을 기록 
            }
        }
        // 찾은 값이 있으면 그 값을 결과에 추가, 없으면 -1을 추가
        answer.push(found ? minVal : -1);
    }
    return answer;
}