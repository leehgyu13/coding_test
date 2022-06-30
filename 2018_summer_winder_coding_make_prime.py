def isprime(num):
    import math
    if num < 2 : return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0 : return False
    return True

def solution(nums):
    answer = 0
    prime = False

    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                tmp = nums[i] + nums[j]
                prime = isprime(tmp + nums[k])
                print(tmp + nums[k])
                print(i, j, k)
                if prime:
                    answer += 1
                    prime = False

    return answer

'''
from itertools import combinations
def prime_number(x):
    answer = 0
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            answer+=1
    return 1 if answer==1 else 0

def solution(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums,3)])
'''