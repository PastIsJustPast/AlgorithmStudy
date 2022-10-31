"""
python   pypy3
33692kb 122720kb
4060ms   312ms


유형  : 힙
풀이방법
- 모두 힙에 넣는다.
- 가장 작은 두 덱을 뽑고, 비교횟수를 더하고 다시 힙에 넣는다.
- 이 과정을 반복한다.

"""
import heapq

n = int(input())
cards = []
for _ in range(n):
    card = int(input())
    heapq.heappush(cards,card)

if len(cards) == 1:  # 1개일 경우 비교하지 않아도 된다
    print(0)
else:
    answer = 0
    while len(cards) > 1:
        tmp1 = heapq.heappop(cards)
        tmp2 = heapq.heappop(cards)
        answer += tmp1 + tmp2
        heapq.heappush(cards, tmp1 + tmp2)

    print(answer)