def solution(money):
    answer = [ ]
    coffee = money//5500 
    balance = money -  coffee* 5500
    answer = [coffee,balance]
    return answer
