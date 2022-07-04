from functools import reduce

def solution(numbers):
    answer = -1

    answer = 45 - int(reduce(lambda x,y: x + y, numbers))

    return answer

'''
def solution(numbers):
    return 45 - sum(numbers)
'''