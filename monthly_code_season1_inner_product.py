def mult(tupl):
    return tupl[0] * tupl[1]

def solution(a, b):
    answer = sum(list(map(mult, zip(a,b))))
    
    return answer

'''
other's sol

def solution(a, b):
    return sum([x * y for x, y in zip(a, b)])
'''