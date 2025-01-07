def solution(array, commands):
    answer = []
    for command in commands: 
        i,j,k = command
        sub_array = array[i - 1:j] 
        sorted_array = selection_sort(sub_array)  # 선택 정렬 호출
        answer.append(sorted_array[k-1])
    return answer 

def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        min_index = i
        for j in range(i +1, n):
            if array[j] < array[min_index]:
                min_index = j 
        array[i], array[min_index] = array[min_index], array[i]
    return array 