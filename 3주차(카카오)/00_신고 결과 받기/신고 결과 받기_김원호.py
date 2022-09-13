def solution(id_list, report, k):
    reporting_id2reported_ids = {}
    reported_id2reporting_ids = {}
    id2mail_count = {}

    for id_ in id_list:
        reporting_id2reported_ids[id_] = set()
        reported_id2reporting_ids[id_] = set()
        id2mail_count[id_] = 0

    for ids in report:
        reporting_id, reported_id = ids.split()
        reporting_id2reported_ids[reporting_id].add(reported_id)
        reported_id2reporting_ids[reported_id].add(reporting_id)

    for reported_id, reporting_ids in reported_id2reporting_ids.items():
        if len(reporting_ids) >= k:
            for reporting_id in reporting_ids:
                id2mail_count[reporting_id] += 1

    answer = [id2mail_count[id_] for id_ in id_list]
    return answer