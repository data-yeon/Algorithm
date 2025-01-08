function solution(my_string) {
    var answer = [];
    for (let i =0; i< my_string.length; i++){
        answer.push(my_string.slice(i));
    }
    //사전순으로 정렬 
    answer.sort()
    return answer;
}