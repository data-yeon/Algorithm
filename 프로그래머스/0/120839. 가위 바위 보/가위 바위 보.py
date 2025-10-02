def solution(rsp):
    trans = {'2': '0', '0':'5','5':'2'}
    
    return ''.join(trans[ch] for ch in str(rsp))