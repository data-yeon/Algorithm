function solution(l, r) {
    let result = [];  // 결과를 저장할 배열을 초기화합니다.

    // l에서 r까지의 모든 숫자를 확인합니다.
    for (let i = l; i <= r; i++) {
        // 현재 숫자를 문자열로 변환하고, 숫자가 "0"과 "5"로만 이루어졌는지 확인합니다.
        let str = i.toString();
        
        // 숫자 문자열이 "0"과 "5"로만 구성되어 있는지 확인합니다.
        if ([...str].every(char => char === '0' || char === '5')) {
            result.push(i);  // 조건을 만족하는 숫자를 결과 배열에 추가합니다.
        }
    }

    // 결과 배열이 비어 있으면 [-1]을 반환하고, 그렇지 않으면 결과 배열을 반환합니다.
    return result.length > 0 ? result : [-1];
}