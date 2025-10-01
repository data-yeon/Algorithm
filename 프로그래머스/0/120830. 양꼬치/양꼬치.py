def solution(n, k):
    answer =  n*12000 + (k-int(n/10))*2000
    # n = 양꼬치갯수
    # k = 음료수 갯수
    # n/10 = 서비스 음료수 갯수
    
    return answer