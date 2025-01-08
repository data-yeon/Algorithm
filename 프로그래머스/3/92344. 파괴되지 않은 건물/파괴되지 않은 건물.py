
def solution(board, skill):
    result= 0
    m = len(board[0])
    n = len(board)

    attack = [[0 for _ in range(m+1)] for __ in range(n+1)]
    for type, r1,c1,r2,c2,degree in skill:
        deal = degree if type == 2 else -degree
        attack[r1][c1] += deal
        attack[r1][c2+1] -= deal
        attack[r2+1][c1] -= deal
        attack[r2+1][c2+1] += deal
    for i in range(n) :
        for j in range(m) :
            attack[i][j+1] += attack[i][j]
    for j in range(m) :
        for i in range(n) :
            attack[i+1][j] += attack[i][j]
    for i in range(n) :
        for j in range(m) :
            board[i][j] += attack[i][j]
            if board[i][j] > 0 :
                result += 1
    return result