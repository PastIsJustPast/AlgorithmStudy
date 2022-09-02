def solution(id_list, report, k):
    #값을 지정할 딕셔너리 생성
    dic = {id:set() for id in id_list}
    mail = {id:0 for id in id_list}
    for rpt in report:
        a, b = rpt.split()
        dic[b].add(a)
            
    for id in id_list:
        if len(dic[id]) >= k :
            for i in dic[id]:
                mail[i] += 1
    return list(mail.values())