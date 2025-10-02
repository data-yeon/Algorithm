def solution(hp):
    generals = hp//5
    hp %= 5 
    soldiers = hp//3
    hp %= 3 
    workers = hp 
    
    return generals + soldiers + workers