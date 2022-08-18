def binary_search(arr, n):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == n:
            return mid
        if arr[mid] > n:
            end = mid - 1
        else:
            start = mid + 1
    return end

N = int(input())
for _ in range(N):
    k, n = map(int, input().split())
    weights = [[int(x) for x in input().split()] for _ in range(4)]

    weights_sum0 = {}
    for weight0 in weights[0]:
        for weight1 in weights[1]:
            weights_sum = weight0 + weight1
            if weights_sum not in weights_sum0:
                weights_sum0[weights_sum] = True
    weights_sum1 = {}
    for weight2 in weights[2]:
        for weight3 in weights[3]:
            weights_sum = weight2 + weight3
            if weights_sum not in weights_sum1:
                weights_sum1[weights_sum] = True

    weights_sum0 = list(weights_sum0.keys())
    weights_sum1 = list(weights_sum1.keys())
    weights_sum0.sort()
    weights_sum1.sort()

    idx0 = binary_search(weights_sum0, k - weights_sum1[-1])
    idx1 = binary_search(weights_sum1, k - weights_sum0[-1])

    if idx0 >= 1:
        weights_sum0 = weights_sum0[idx0 - 1:]
    if idx1 >= 1:
        weights_sum1 = weights_sum1[idx1 - 1:]

    optim = weights_sum0[0] + weights_sum1[0]
    optim_diff = abs(k - optim)

    for weight0 in weights_sum0:
        idx = binary_search(weights_sum1, abs(k - weight0))
        for idx in range(idx, idx + 2):
            if idx >= len(weights_sum1) or idx < 0:
                continue
            weight1 = weights_sum1[idx]
            weights_sum = weight0 + weight1
            # print(weights_sum)
            diff = abs(k - weights_sum)
            if diff < optim_diff:
                optim_diff = diff
                optim = weights_sum
            elif diff == optim_diff:
                optim = min(optim, weights_sum)
        # print()
    print(optim)
