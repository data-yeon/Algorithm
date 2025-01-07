function solution(a, b, c) {
    var answer = 0;
    
    const allDiff = ( a !== b && b !== c && c !== a);
    const triSame = (a === b && b === c );
    //a,b / b,c / a,c
   const twoSame = (a === b || b === c || a === c) && !triSame; 
    // 두 숫자가 같음, 그러나 세 숫자가 모두 같은 경우는 제외
    
    //세 숫자가 모두 다르다면 a + b + c 점
    //숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a2 + b2 + c2 )점을 얻습니다.
   // 세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점을 얻습니다.
    
    
    if (allDiff) {
    answer = (a + b + c);
    } else if (twoSame){
    answer =  ((a + b + c) * (a**2 + b**2 + c**2));
    } else if (triSame){
     answer=  ((a + b + c) * (a**2 + b**2 + c**2 ) * (a**3 + b**3 + c**3));  
    }
    return answer;
}