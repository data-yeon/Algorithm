function solution(arr, queries) {
    // queries 배열의 각 쿼리를 순차적으로 처리합니다.
    queries.forEach(query => {
        const [s, e, k] = query;  // 각 쿼리에서 s, e, k를 구조 분해 할당으로 꺼냅니다.
        
        // s부터 e까지의 범위를 순회하면서 인덱스를 찾습니다.
        for (let i = s; i <= e; i++) {
            if (i % k === 0) {   // i가 k의 배수인 경우
                arr[i] += 1;     // arr[i]에 1을 더해줍니다.
            }
        }
    });

    return arr;  // 모든 쿼리를 처리한 후, arr 배열을 반환합니다.
}