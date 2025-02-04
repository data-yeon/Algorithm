# 버블 정렬
def solution(array, commands):
    answer = []
    for command in commands: 
        i,j,k = command
        sub_array = array[i - 1:j] 
        sorted_array = insertion_sort(sub_array)  # 선택 정렬 호출
        answer.append(sorted_array[k-1])
    return answer 

def insertion_sort(array):
    # 삽입정렬을 사용해서 리스트를 정렬하기 
    n = len(array)
    for i in range(1,n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key : # key보다 큰 값들을 한칸씩 뒤로 이동
            array[ j + 1 ] = array[j]
            j -= 1
        array[j + 1] = key 
    return array 