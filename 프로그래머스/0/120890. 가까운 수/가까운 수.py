def solution(array, n):
    answer = 0
    diffs = []
    for num in array:
        diffs.append(abs(num-n))
    min_diff = min(diffs)
    candidates = []
    for i in range(len(array)):
        if diffs[i] == min_diff:
            candidates.append(array[i])
    return min(candidates)