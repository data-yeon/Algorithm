def solution(s):
    freq = {}
    for ch in s : 
        freq[ch] = freq.get(ch, 0) + 1 
    ones = []
    for ch, cnt in freq.items():
        if cnt ==1:
            ones.append(ch)
    ones.sort()
    answer = ''.join(ones)
    return answer