def get_max_fuel_idx(stations, dist_limit):
    max_idx = -1
    max_fuel = -1
    for idx, station in enumerate(stations):
        dist, fuel = station
        if dist > dist_limit:
            return max_idx
        if fuel > max_fuel:
            max_idx = idx
            max_fuel = fuel
    return max_idx


N = int(input())

stations = []
for _ in range(N):
    dist, fuel = map(int, input().split())
    stations.append((dist, fuel))
stations.sort()

city_dist, original_fuel = map(int, input().split())
if original_fuel >= city_dist:
    print(0)
    exit(0)

dp = [0 for _ in range(N+1)]
dp[0] = original_fuel
for i in range(1, N+1):
    station_idx = get_max_fuel_idx(stations, dp[i-1])
    if station_idx == -1:
        print(-1)
        exit(0)
    _, fuel = stations.pop(station_idx)
    dp[i] = dp[i-1] + fuel
    if dp[i] >= city_dist:
        print(i)
        exit(0)
print(-1)
