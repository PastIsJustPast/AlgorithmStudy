'''
풀이를 참고해서... 이해해보려고..했지만 이해를 못한 것 같습니다^^..ㅜㅜ

PyPy3
메모리       시간
185600KB	392ms

Python3 메모리 초과
'''

a,b,c = map(int, input().split())
a,b,c = -a, -b, -c
x = input()
y = input()
dp = [[0]*((len(y)+1)) for _ in range((len(x)+1))]
diag = 0
#print(dp)

for i in range(1, (len(x)+1)):
    dp[i][0] = dp[i-1][0] + b
#print(dp) #[[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0]]

for i in range(1, (len(y)+1)):
    dp[0][i] = dp[0][i-1] + b
#print(dp) #[[0, 1, 2], [1, 0, 0], [2, 0, 0], [3, 0, 0]]

for i in range(1, len(x)+1):
    for j in range(1, len(y)+1):
        if x[i-1] == y[j-1]: # 두 문자가 같은 경우
            diag = dp[i-1][j-1] + a
        else: # 두 문자 모두 공백이 아니고 서로 다른 경우
            diag = dp[i-1][j-1] + c
        #print(diag)
        dp[i][j] = min(min(dp[i-1][j] + b, dp[i][j-1] + b), diag)
        #print(dp)
        '''
        [[0, 1, 2], [1, 2, 0], [2, 0, 0], [3, 0, 0]]
        [[0, 1, 2], [1, 2, 3], [2, 0, 0], [3, 0, 0]]
        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 0]]
        [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 0, 0]]
        [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 0]]
        [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, -7]]
        '''
print(dp[len(x)][len(y)] * (-1))