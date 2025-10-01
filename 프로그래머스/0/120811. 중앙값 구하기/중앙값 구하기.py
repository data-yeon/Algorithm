def solution(array):
    arr  = sorted(array)
    n = len(arr)
    mid = n//2
    if n % 2 == 1:
        return arr[mid]
    else:
        return (arr[mid-1] + arr[mid])/2