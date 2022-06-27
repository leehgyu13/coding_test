def solution(s):
    answer = 0
    nums = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
    num = ''
    
    for i in s:
        if(i.isalpha()):
            num = num + i
            if num in nums:
                s = s.replace(num, nums[num])
                num =''
    
    answer = s
    
    return answer