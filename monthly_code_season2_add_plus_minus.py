def applSign(num, sign):
    if sign:
        return num
    elif not(sign):
        return -num

def solution(absolutes, signs):
    answer = 123456789
    
    for i in range(len(absolutes)):
        absolutes[i] = applSign(absolutes[i], signs[i])
    
    answer = sum(absolutes)
    return answer

'''
Other sol

def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
'''