'''
python3  pypy3
30840kb  115700kb
468ms    144ms

dp[idx] : idx번째 와인잔까지 최대로 먹을 수 있는 와인의 양
dp는 현재, 직전, 직전전 중 2개를 고르는거라고 생각하면 됨
dp[idx] = max(dp[idx - 3] + g[idx-1] + g[idx] , dp[idx-2] + g[idx], dp[idx-1])
'''
n = int(input())
grapes = [0] #dp테이블과 index를 맞추기 위해 0 추가
for _ in range(n):
    grapes.append(int(input()))

#dp테이블
dp = [0] * (n+1)

for idx in range(1,n+1) :
    if idx < 3 :  #
        dp[idx] = dp[idx-1] + grapes[idx]
        continue
    sub = []
    sub.append(dp[idx - 3] + grapes[idx-1] + grapes[idx]) #직전과 자기자신 고르기
    sub.append(dp[idx - 2] + grapes[idx]) #직전전과 자기자신 고르기
    sub.append(dp[idx - 1])  # 자기자신 안고르기
    dp[idx] = max(sub)

print(dp[n])
