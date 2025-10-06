def solution(emergency):
    rank = {v: i+1 for i, v in  enumerate(sorted(emergency, reverse=True))}
    return  [rank[v] for v in emergency] 