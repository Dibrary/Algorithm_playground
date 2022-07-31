
def counting(users, report):
    alarm_counts = dict()
    tmp = set()

    for k in report:
        user,target = k.split()
        users[user].append(target)

        if k not in tmp:
            tmp.add(k)
            if target not in alarm_counts:
                alarm_counts[target] = 1
            else:
                alarm_counts[target] += 1

    return users, alarm_counts


def solution(id_list, report, k):
    users = dict()
    for i in id_list:
        users[i] = []

    user_report, alarm_counts = counting(users, report)
    print(user_report)
    print(alarm_counts)

    answer = []

    for m in user_report.values():
        m = list(set(m)) # 중복 제거

        cnt = 0
        for j in m:
            if alarm_counts[j] >= k:
                cnt += 1
        answer.append(cnt)

    return answer



ids = ['muzi','frodo','apeach','neo']
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(ids, report, k))

print("\n")

ids = ['con', 'ryan']
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

print(solution(ids, report, k)) # 결과가 [0, 0] 이 나와야 됨.



# 다른 사람 코드 (엄청 간단하다;;)

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer


###############################

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic_report = {id: [] for id in id_list} # 해당 유저를 신고한 ID
    for i in set(report):
        i = i.split()
        dic_report[i[1]].append(i[0])

    for key, value in dic_report.items():
        if len(value) >= k:
            for j in value:
                answer[id_list.index(j)] += 1

    return answer