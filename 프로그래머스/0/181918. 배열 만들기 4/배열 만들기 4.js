function solution(arr) {
    const stk = []; // 새로운 배열 stk를 초기화
    let i = 0; // i를 0으로 초기화

    // i가 arr의 길이보다 작을 동안 반복
    while (i < arr.length) {
        if (stk.length === 0) {
            // stk가 빈 배열이면 arr[i]를 추가하고 i 증가
            stk.push(arr[i]);
            i++;
        } else if (stk[stk.length - 1] < arr[i]) {
            // stk의 마지막 원소가 arr[i]보다 작으면 arr[i]를 추가하고 i 증가
            stk.push(arr[i]);
            i++;
        } else {
            // stk의 마지막 원소가 arr[i]보다 크거나 같으면 stk의 마지막 원소 제거
            stk.pop();
        }
    }

    // 만들어진 stk 배열을 반환
    return stk;
}