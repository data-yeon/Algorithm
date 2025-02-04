# 버블 정렬
def solution(array, commands):
    answer = []
    for command in commands: 
        i,j,k = command
        sub_array = array[i - 1:j] 
        sorted_array = bubble_sort(sub_array)  # 선택 정렬 호출
        answer.append(sorted_array[k-1])
    return answer 

def bubble_sort(array):
    # 버블정렬을 사용해서 리스트를 정렬하기 
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1): 
            if array[j] > array[j + 1] :  # 오름 차순 정렬 
                array[j], array[j+1] =array[j+1], array[j]
    return array 