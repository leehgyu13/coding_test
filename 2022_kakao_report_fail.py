def solution(id_list, report, k):
    answer = []
    
    # 신고 받은 횟수
    reported = dict.fromkeys(id_list, 0)
    # 자신이 신고한 사람 목록
    info = dict.fromkeys(id_list)
    for id_name in id_list:
        info[id_name] = []
    # 정지 이용자 명단
    out = []
    # 메일 정보
    mail = dict.fromkeys(id_list, 0)
    
    for i in range(len(report)):
        name = report[i].split(' ')
        key = name[0]
        value = name[1]

        if i == 0:
            info[key].append(value)
            reported[value] += 1
        elif i > 0:
            if report[i] not in report[0 : i-1]:
                info[key].append(value)
                reported[name[1]] += 1
            
    for j in id_list:
        if reported.get(j) >= k:
            out.append(j)
    
    for l in out:
        for m in id_list:
            if l in info.get(m):
                mail[m] += 1
    
    answer = list(mail.values())
        
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2

print(solution(id_list, report, k))
