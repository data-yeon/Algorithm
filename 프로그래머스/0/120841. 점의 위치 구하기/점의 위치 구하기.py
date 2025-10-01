def solution(dot):
    x, y = dot   # x좌표, y좌표
    if x > 0 and y > 0:
        return 1   # 1사분면
    elif x < 0 and y > 0:
        return 2   # 2사분면
    elif x < 0 and y < 0:
        return 3   # 3사분면
    else:  # x > 0 and y < 0
        return 4   # 4사분면