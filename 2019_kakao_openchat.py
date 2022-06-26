def solution(record):
    answer = []
    notices = []
    dic = {}

    for i in record:
        tmp = i.split()
        if (tmp[0] == "Enter"):
            notices[0] = tmp[1] + "님이 들어왔습니다."
            dic[tmp[1]] = tmp[2]
        elif (tmp[0] == "Leave"):
            notices[0] = tmp[1] + "님이 나갔습니다."
        elif (tmp[0] == "Change"):
            dic[tmp[1]] = tmp[2]

    for notice in notices:
        id = notice.split("님")
        result = notice.replace(id[0], dic[id[0]])
        answer.append(result)
        
    return answer