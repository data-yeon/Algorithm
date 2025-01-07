function solution(ineq, eq, n, m) {
    var answer = 0;
    // 비교 조건을 처리한다 
    if (ineq === ">" && eq === "="){
        return n >= m ? 1 : 0;
    } else if(ineq === "<" && eq === "="){
        return n <= m ? 1 : 0;
        
    } else if(ineq === ">" && eq === "!"){
        return n>m ? 1 : 0;
    } else if(ineq === "<" && eq === "!"){
        return n<m ? 1 : 0;
    }
    return answer;
}