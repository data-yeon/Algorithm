function solution(num_list) {
    var answer = [];
    const last = num_list[num_list.length - 1];  //마지막 원소    
    const beforeLast = num_list[num_list.length - 2]; // 그 전 원소 

        if (last > beforeLast) {
              num_list.push(last - beforeLast); // 마지막 원소가 더 크면 차이를 추가
        } else {
        num_list.push(last * 2); // 마지막 원소가 더 작거나 같으면 두 배를 추가
    }
 
          return num_list;
}