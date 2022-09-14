from collections import defaultdict


def solution(fees, records):
    answer = []
    record_dict = defaultdict(list)
    used = defaultdict(int)
    for record in records:
        time, car_num, _ = record.split()
        if record_dict[car_num]:
            ent = record_dict[car_num].pop()
            used[car_num] += time_differ(ent, time)
        else:
            record_dict[car_num].append(time)

    for car_num in sorted(record_dict.keys()):
        print(car_num)
        if record_dict[car_num]:
            ent = record_dict[car_num].pop()
            used[car_num] += time_differ(ent)
        answer.append(calculate_fee(*fees, used[car_num]))

    print(used)
        
    return answer


def calculate_fee(bt, bf, ut, uf, time):
    return bf + uf * max(0, - divmod(-(time - bt), ut)[0])


def time_differ(ent, ext="23:59"):
    ent_h, ent_m = map(int, ent.split(":"))
    ext_h, ext_m = map(int, ext.split(":"))
    return ext_h * 60 + ext_m - (ent_h * 60 + ent_m)


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))