function solution(babbling) {
    var answer = 0;
    //발음 할 수 있는 단어들 
    const possibleWords = ["aya", "ye", "woo", "ma"];
    
    //주어진 각 문자열을 확인
    babbling.forEach(word => {
        let temp = word;
        // 가능한 단어들을 하나씩 제거 
        possibleWords.forEach (pw =>{
            temp = temp.replace(pw, " ");
        });
        // 제거된 후 , 남는 문자가 없는지 확인 
//(모든 발음 가능 단어로만 이루어졌다면 공백만 남음)
        if(temp.trim()===""){
            answer++
        }
    });
    return answer;
    
}