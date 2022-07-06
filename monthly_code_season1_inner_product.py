def mult(tupl):
    return tupl[0] * tupl[1]

def solution(a, b):
    answer = sum(list(map(mult, zip(a,b))))
    
    return answer

'''
another sol

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
        
    return answer
'''
'''
other's sol

def solution(a, b):
    return sum([x * y for x, y in zip(a, b)])
'''
'''
other's sol2
solution = lambda x, y: sum(a*b for a, b in zip(x,y))
'''