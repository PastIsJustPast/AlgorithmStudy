from math import ceil


def solution(fees, records):
    def get_minutes(time):
        h, m = time.split(':')
        return int(h) * 60 + int(m)

    def get_parking_time(intime, outtime):
        intime = get_minutes(intime)
        outtime = get_minutes(outtime)
        return outtime - intime

    def get_fee(time):
        time -= fees[0]
        if time <= 0:
            return fees[1]
        return fees[1] + ceil(time / fees[2]) * fees[3]

    carnum2intime = {}
    carnum2parking_time = {}
    for record in records:
        time, carnum, _type = record.split()
        if _type == 'IN':
            carnum2intime[carnum] = time
            if carnum not in carnum2parking_time:
                carnum2parking_time[carnum] = 0
        else:
            carnum2parking_time[carnum] += get_parking_time(carnum2intime[carnum], time)
            del carnum2intime[carnum]
    for carnum, intime in carnum2intime.items():
        carnum2parking_time[carnum] += get_parking_time(intime, '23:59')
    carnums = sorted(carnum2parking_time.keys())
    answer = [get_fee(carnum2parking_time[carnum]) for carnum in carnums]
    return answer