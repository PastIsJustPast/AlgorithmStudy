'''
        메모리(kb) 시간(ms)
python3 33692    4096
pypy3   123444   324
'''

import heapq

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
heapq.heapify(nums)

answer = 0
while len(nums) >= 2:
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    heapq.heappush(nums, a + b)
    answer += a + b
print(answer)