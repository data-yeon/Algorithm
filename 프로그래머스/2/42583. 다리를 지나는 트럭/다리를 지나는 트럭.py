# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque
# 트럭이 최대 올라갈 수 있는 대 수 : bridge_length
# 다리는 weight이하의 무게를 견딞 : weight
# truck_weights: 각 트럭의 무게
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)  # 다리의 길이만큼 초기화
    truck_weights = deque(truck_weights) # 대기중인 트럭들의 무게 리스트를 큐로 변환

    current_weights = 0  # 현재 다리에 오른 모든 트럭의 무게를 저장할 변수
    time = 0 # 시간

    # bridge가 비어있지 않은 동안...
    while bridge:
        time += 1 # 시간 경과
        current_weights -= bridge.popleft() # 다리의 첫번째 트럭 (또는 0 )을 제거하고, 무게에서 빼줌.
        if truck_weights:
            # 새로운 트럭이 다리에 올라갈 수 있는지를 확인.
            if current_weights + truck_weights[0]  <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck) # 새로운 트럭 다리에 추가
                current_weights += truck
            else:
                bridge.append(0) # 트럭이 못 올라가면 시간만 흐른다.


    return time