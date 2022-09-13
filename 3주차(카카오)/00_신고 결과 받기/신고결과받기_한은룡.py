# 딕셔너리 만들면 편하게 풀 수 있음
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {id: [] for id in id_list}  # id를 신고한 사람 명단

    # 신고한사람
    for i in set(report):
        reports[i.split()[1]].append(i.split()[0])

    # k번 이상 신고당한 사람의 신고자에게 매일
    for key, values in reports.items():
        if len(values) >= k:  # key를 신고한사람 수
            for j in values:  # 신고한사람
                answer[id_list.index(j)] += 1

    return answer