'''
def solution(id_list, report, k):
    answer = []
    dict_name = dict()
    for i in report:
        a, b = i.split()
        if a not in dict_name.keys():
            dict_name[a] = [b]
        # 신고내역 존재
        else:
            if b not in dict_name.get(a):
                dict_name.get(a).append(b)

    list_report = []
    for i in id_list:
        cnt = 0
        for j in list(dict_name.values()):
            if i in j:
                cnt += j.count(i)
        if cnt >= k :
            list_report.append(i)
    for i in id_list:
        cnt = 0
        if i in dict_name.keys():
            for j in list_report:
                if j in dict_name.get(i):
                    cnt += 1
        answer.append(cnt)
    return answer
'''


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_cnt = {i: 0 for i in id_list}

    # 중복 제거
    for i in set(report):
        a, b = i.split()
        report_cnt[b] += 1

    for j in set(report):
        a, b = j.split()
        if report_cnt[b] >= k:
            answer[id_list.index(a)] += 1 # a의 위치값 반환
    return answer