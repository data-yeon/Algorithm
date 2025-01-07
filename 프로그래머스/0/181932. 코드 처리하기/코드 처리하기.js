function solution(code) {
    var ret =""     // 결과 문자열
    var mode =0;    // 시작할 때 mode 는 0
    
    for (let idx = 0; idx< code.length; idx++){
        if(code[idx] === "1"){
            mode = mode === 0 ? 1 : 0;
//mode === 0: mode가 0인지 확인하는 조건입니다.
// ? 1 : 0: 만약 mode === 0 조건이 참이라면 1을 반환하고, 그렇지 않다면 0을 반환합니다.
        } else {
            // mode 에 따라 행동 
            if ( mode === 0 && idx % 2 === 0 ){
                ret += code[idx]; // mode가 0일 때는 짝수 인덱스에서 추가
            } else if (mode === 1 && idx % 2 === 1 ) {
                ret += code[idx];  // mode가 0일 때는 홀수 인덱스에서 추가
            }
        }
    }
      // ret이 빈 문자열이면 "EMPTY"를 반환
    return ret === "" ? "EMPTY" : ret;
}