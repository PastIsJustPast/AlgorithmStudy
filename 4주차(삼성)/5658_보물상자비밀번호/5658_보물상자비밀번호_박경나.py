# 사각형 변의 길이가 길어지는 것
# 길이가 길어지면 회전 수 증가
# 굳이 덱 안써도 인덱스 알아서 당겨지니까 리스트 써도 괜춘할듯

from collections import deque

def rotate(li: deque):
    li.append(li.popleft())
    return li

def convert(li: list):
    for i in range(0, n):
        li[i] = int(li[i], 16)
    return li

t = int(input())
cnt = 1

for T in range(1, t+1):
    n, k = map(int, input().split())
    dq = deque()
    index = n // 4
    rotated_list = [0] * (index+1)

    text = input()
    for i in range(len(text)):
        dq.append(text[i])

    rotated_list[0] = list(dq)
    for i in range(1, index):
        rotated_list[i] = list(rotate(dq))

    num_list = [[""]*4 for _ in range(index)]
    for i in range(0, index):
        q = 0
        for j in range(0, n):
            if j > 0 and j % index == 0:
                q += 1
            num_list[i][q] += rotated_list[i][j]

    num_list2 = sum(num_list, []) # 1차원으로 변환
    num_list2 = list(set(convert(num_list2)))
    num_list2.sort(reverse=True)
    print("#%d %d" %(T, num_list2[k-1]))