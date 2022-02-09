def solution(fees, records):
    answer = []
    dic = {}
    inTime = []
    
    for i in records:
        time, num, info = i.split(' ')
        if info == "IN":
            if num not in dic:
                # 차량 번호 : 입차 시간, 이용시간, 요금
                inTime = time.split(':')
                dic[num] = [inTime, 0, 0]
            else:
                dic[num][0][0], dic[num][0][1] = time.split(':')

        if info == "OUT":
            outTime = time.split(':')
            if int(outTime[1]) < int(dic[num][0][1]):
                m = 60 - int(dic[num][0][1]) + int(outTime[1])
                h = (int(outTime[0]) - 1) - int(dic[num][0][0])
                dic[num][1] += ((h * 60) + m)
            else:
                m = int(outTime[1]) - int(dic[num][0][1])
                h = int(outTime[0]) - int(dic[num][0][0])
                dic[num][1] += ((h * 60) + m)
            dic[num][0] = [0, 0]

    for j in list(dic.keys()):
        if dic[j][0] != [0, 0]:
            m = 59 - int(dic[j][0][1])
            h = 23 - int(dic[j][0][0])
            dic[j][1] += ((h * 60) + m)
            dic[j][0] = [0, 0]
        # 요금 계산
        if dic[j][1] <= fees[0]:
            dic[j][2] = fees[1]
        else:
            over = dic[j][1] - fees[0]
            if over % fees[2] == 0:
                fee = ((over / fees[2]) * fees[3])
                dic[j][2] = fee + fees[1]
            else:
                fee = ((over // fees[2]) + 1) * fees[3]
                dic[j][2] = fee + fees[1]

    dic_sorted = dict(sorted(dic.items()))
    answer = [total[2] for total in list(dic_sorted.values())]

    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))