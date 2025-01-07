def calculate_work_hours(schedule, time_slots):
    work_hours = {}
    
    for day in schedule:
        for i, shift in enumerate(day):
            hours = time_slots[i]
            for name in shift:
                if name != '-':
                    if name in work_hours:
                        work_hours[name] += hours
                    else:
                        work_hours[name] = hours
    return work_hours

def is_fair_schedule(work_hours):
    if not work_hours:  # 근무자가 없으면 공평하다고 간주
        return "Yes"
    
    max_hours = max(work_hours.values())
    min_hours = min(work_hours.values())
    
    return "Yes" if max_hours - min_hours <= 12 else "No"

# 입력 처리
n = int(input().strip())
schedule = []

# 시간대별 근무 시간
time_slots = [4, 6, 4, 10]

for _ in range(n):
    week_schedule = []
    for _ in range(4):
        # 각 시간대 근무자를 리스트로 추가
        shift = input().strip().split()
        week_schedule.append(shift)
    schedule.append(week_schedule)

# 전체 근무 시간 계산
work_hours = calculate_work_hours(schedule, time_slots)

# 공평성 확인 후 출력
result = is_fair_schedule(work_hours)
print(result)