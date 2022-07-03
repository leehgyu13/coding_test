def solution(board, moves):
    answer = 0
    basket = []
    
    for i in moves:
        for doll in board:
            if doll[i - 1] != 0:
                if basket == []:
                    basket.append(doll[i - 1])
                    doll[i - 1] = 0
                else:
                    if basket[-1] == doll[i - 1]:
                        basket.pop()
                        doll[i - 1] = 0
                        answer += 2
                    else:
                        basket.append(doll[i - 1])
                        doll[i - 1] = 0
                break
    
    return answer