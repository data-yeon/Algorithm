import sys
input = sys.stdin.readline

n = int(input())  # 첫째 줄에 기록된 출입 기록의 수 n
logs = {}

# 출입기록 
for _ in range(n): 
    name, action = input().split()
    if action == "enter":
        logs[name] = True  # 회사에 들어오면 True로 기록
        
    elif action == "leave": 
        logs[name] = False  # 회사에서 나가면 False로 기록
        
for name in sorted(logs.keys(), reverse=True):
    if logs[name]:  # True인 사람만 출력
        print(name)