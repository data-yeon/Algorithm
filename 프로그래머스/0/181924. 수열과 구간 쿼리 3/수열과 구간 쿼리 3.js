function solution(arr, queries) {
    var answer = [];
    for (let[i,j] of queries) {
         // 각 쿼리를 처리하면서 arr 배열의 값을 서로 바꿈
          // i와 j의 값을 교환
        let temp = arr[i];
        arr[i] =  arr[j];
        arr[j] = temp;
    }
    return arr;
}