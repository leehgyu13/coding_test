def solution(n, k):
    answer = -1
    
    tmp = []
    
    q, r = divmod(n, k)
    tmp.append(str(r))
        
    while q >= k:
        q, r = divmod(q, k)
        tmp.append(str(r))
        
    tmp.append(str(q))
    tmp.reverse()
        
    notation = "".join(tmp)
    
    tmp = []
    tmp = notation.split('0')
    
    for i in tmp:
        not_prime = 0
        if i != '' and i != '1':
            num = int(i)
            for j in range(2, num-1):
                if num % j == 0:
                    not_prime = 1
                    break
            if not_prime == 0:
                answer += 1
    
    answer += 1
    
    return answer
