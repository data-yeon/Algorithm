function solution(x1, x2, x3, x4) {
    /*
    •	OR (∨): 둘 중 하나라도 참이면 참 (true)을 반환합니다.
	•	AND (∧): 둘 다 참이어야 참 (true)을 반환합니다.
    
    */
    var answer = true;
    return (x1 || x2) && (x3 || x4);
    
}