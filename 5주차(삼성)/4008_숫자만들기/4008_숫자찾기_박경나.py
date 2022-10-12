# dfs로 풀었는데 순열로 어떻게 푸는지 모르겠습니다ㅠ

def dfs(sum, idx):
    global max, min
    if idx == n:
        if sum > max:
            max = sum
        if sum < min:
            min = sum
        return
    for i in range(4):
        if op_num[i] > 0:
            if i == 0:
                op_num[i] -= 1
                dfs(sum+num[idx], idx + 1)
                op_num[i] += 1
            elif i == 1:
                op_num[i] -= 1
                dfs(sum - num[idx], idx + 1)
                op_num[i] += 1
            elif i == 2:
                op_num[i] -= 1
                dfs(sum * num[idx], idx + 1)
                op_num[i] += 1
            else:
                op_num[i] -= 1
                dfs(int(sum / num[idx]), idx + 1) # // 쓰면 반올림됨
                op_num[i] += 1
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    op_num = list(map(int, input().split())) # + - * /
    #op = []
    num = list(map(int, input().split()))
    max = -2e9
    min = 2e9
    dfs(num[0], 1)
    print("#{} {}".format(tc, max-min))

    '''
    연산자 순열?
    for j in range(len(op_num)):
        for k in range(op_num[j]):
            if j == 0:
                op.append("+")
            elif j == 1:
                op.append("-")
            elif j == 2:
                op.append("*")
            else:
                op.append("/")
    op = permutations(op, n-1) 음....,,,,.....
    op = list(set(op))
    '''
