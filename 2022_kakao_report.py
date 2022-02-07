def solution(id_list, report, k):
    answer = []

    # 신고 받은 수, 자신을 신고한 사람 명단, 메일
    info = {}
    for name in id_list:
        info[name] = [0, [], 0]

    for i in range(len(report)):
        tmp = report[i].split(' ')

        if i == 0:
            info[tmp[1]][1].append(tmp[0])
            info[tmp[1]][0] += 1

        elif tmp[0] not in info[tmp[1]][1]:
            info[tmp[1]][1].append(tmp[0])
            info[tmp[1]][0] += 1

    for name in id_list:
        if info[name][0] >= k:
            for reporter in info[name][1]:
                info[reporter][2] += 1

    answer = [info[name][2] for name in id_list]

    return answer
