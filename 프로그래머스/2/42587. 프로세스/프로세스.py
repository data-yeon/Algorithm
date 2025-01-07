from collections import deque
def solution(priorities, location):
    # 큐에 우선순위 와 인덱스 형태로 저장 
    queue = deque((priority, index) for index, priority in enumerate(priorities))
    answer = 0 # 실행 순서를 기록할 변수 
    while queue :
        current = queue.popleft() #   큐의 맨 앞 프로세스를 꺼냄 
        # 현재 프로세스보다 우선순위가 높은 프로세스가 존재하는지 확인
        if(any (current[0] < process[0] for process in queue)):
            queue.append(current)
        else : 
            # 우선순위가 가장 높으면 실행이 된다. 
            answer += 1
            if current[1] == location:
                return answer
 