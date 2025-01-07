function solution(num_list) {
    let multi = 1;
    let sum = 0;
    
    // 모든 원소들의 곱과 합을 계산
    for (let i = 0; i < num_list.length; i++) {
        multi *= num_list[i];
        sum += num_list[i];
    }

    // 모든 원소들의 합의 제곱
    let square = sum ** 2;
    
    // 곱이 합의 제곱보다 크면 0, 작으면 1을 반환
    if (multi < square) {
        return 1;
    } else {
        return 0;
    }
}