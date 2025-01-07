from math import ceil
def solution(progresses, speeds):
    answer = [] # 각 배포마다 몇개 기능이 배포되는지 저장
    days = [] # 각 기능이 완료되기까지 걸리는 일수 저장 
    
    # (100 - 진도) / 속도 , 각작업 남을 일 수 계산
    for p,s in zip(progresses, speeds): 
        days.append(ceil((100 - p)/ s))
    
    # 첫번째 기능 배포 시점 기준
    current_day = days[0] 
    count = 0 # 한번 배포 시, 포함되는 기능 
    
    for day in days:
        if day <= current_day: 
            # 기준 일수 안에 끝나면 배포 
            count += 1 
        else: 
            # 새로운 배포 시점 시작 
            answer.append(count) 
            current_day = day 
            count = 1 
    answer.append(count)
    return answer