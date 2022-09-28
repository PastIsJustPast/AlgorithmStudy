# 구현 문제

for T in range(int(input())):
    N, K = map(int, input().split())
    nums = set()
    step = N // 4
    num = input() * 2
    for i in range(N):
        for j in range(4):
            seg = num[i + step * j:i + step * (j + 1)]
            nums.add(seg)
    print(f"#{T+1} {int(sorted(nums)[-K], 16)}")