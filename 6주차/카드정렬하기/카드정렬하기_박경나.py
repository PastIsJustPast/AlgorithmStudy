'''
가장 작은 값을 2개를 뽑고 더하는 방식이니까 heap 자료구조를 이용해서 heappop으로 뽑아내기

PyPy3
메모리    크기
122720KB 336ms

Python3
33692KB	4016ms
'''
import heapq

n = int(input())
heap = list()

for _ in range(n):
    heapq.heappush(heap, int(input()))

if len(heap) == 1:
    print(0)
else:
    result = 0
    while len(heap) > 1:
        # heappop : 가장 작은 원소 pop
        A = heapq.heappop(heap) # 가장 작은 거
        B = heapq.heappop(heap) # 두번째로 작은 거
        result += A+B # 비교 횟수
        heapq.heappush(heap, A+B) # 합치고 다시 힙에 넣어줌
    print(result)