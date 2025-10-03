def solution(order):
    answer = 0
    digits = {"3", "6", "9"}
    return sum (ch in digits for ch in str(order))