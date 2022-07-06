def mult(tupl):
    return tupl[0] * tupl[1]

def solution(a, b):
    answer = sum(list(map(mult, zip(a,b))))
    
    return answer