def solution(n):
    root = int(n ** 0.5)
    if root * root == n:
        return 1
    else:
        return 2 
 