function solution(a, b) {
    var answer = 0;
    // 두 숫자를 문자열로 변환하고 붙인 후 비교
    const ab = parseInt(a.toString() + b.toString());
    // 2 * a * b 계산
    const multiply = 2 * a * b;  
    // a ⊕ b와 2 * a * b 중 더 큰 값 반환, 같으면 ab 반환
    if (ab > multiply) {
        return ab;
    } else if(multiply > ab) {
        return multiply;
    } else if(ab === multiply){
        console.log("a ⊕ b");
    }
}