def distance(coor1, coor2):
    dis = abs(coor1[0] - coor2[0]) + abs(coor1[1] - coor2[1])

    return dis

def solution(numbers, hand):
    answer = ''
    coor = {1:(0,0), 2:(0,1), 3:(0,2),
            4:(1,0), 5:(1,1), 6:(1,2),
            7:(2,0), 8:(2,1), 9:(2,2),
            0:(3,1)}
    L = [1, 4, 7]
    R = [3, 6, 9]
    posL = (3,0)
    posR = (3,2)

    for i in numbers:
        if i in L:
            posL = coor[i]
            answer += 'L'
        elif i in R:
            posR = coor[i]
            answer += 'R'
        else:
            disL = distance(coor[i], posL)
            disR = distance(coor[i], posR)

            if disL == disR:
                answer += ('L' if hand == 'left' else 'R')
                if hand == 'left':
                    posL = coor[i]
                else:
                    posR = coor[i]

            elif disL < disR:
                answer += 'L'
                posL = coor[i]

            elif disL > disR:
                answer += 'R'
                posR = coor[i]

    return answer