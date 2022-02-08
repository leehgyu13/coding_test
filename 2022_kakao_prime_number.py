def solution(n, k):
    answer = -1
    
    notation = ""
    
    q, r = divmod(n, k)
    notation = str(r) + notation
        
    while q >= k:
        q, r = divmod(q, k)
        notation = str(r) + notation
        
    notation = str(q) + notation
    
    tmp = []
    tmp = notation.split('0')
    
    for i in tmp:
        not_prime = 0
        if i != '' and i != '1':
            num = int(i)
            if num == 2 or num == 3:
                answer += 1
            elif num % 2 == 0:
                not_prime = 1
            else:
                for j in range(3, int(num ** 0.5) + 1, 2):
                    if num % j == 0:
                        not_prime = 1
                        break
                if not_prime == 0:
                    answer += 1
    
    answer += 1
    
    return answer
