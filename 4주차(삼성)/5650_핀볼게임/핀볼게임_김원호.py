# 49개만 맞음
import sys


sys.stdin = open('sample_input.txt')


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


class Block:
    def __init__(self, num):
        self.num = num
        if num == 1:
            self.reflect = {2: 1, 3: 0}
        elif num == 2:
            self.reflect = {0: 1, 3: 2}
        elif num == 3:
            self.reflect = {0: 3, 1: 2}
        elif num == 4:
            self.reflect = {1: 0, 2: 3}
        else:
            self.reflect = {}

    def interact(self, ball):
        head = ball.head
        if head in self.reflect:
            new_head = self.reflect[head]
        else:
            new_head = (head + 2) % 4
        ball.head = new_head
        ball.score += 1


class Hole:
    member = []

    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
        for hole in Hole.member:
            if hole.num == num:
                self.x = hole.x
                self.y = hole.y
                hole.x = x
                hole.y = y
        Hole.member.append(self)

    def interact(self, ball):
        ball.x = self.x
        ball.y = self.y


class Ball:
    def __init__(self, x, y, head):
        self.x = x
        self.y = y
        self.head = head
        self.score = 0
        self.paths = set()

    def move(self):
        self.paths.add((self.x, self.y, self.head))
        self.x += dx[self.head]
        self.y += dy[self.head]

    def is_repeated(self):
        return (self.x, self.y, self.head) in self.paths


def get_class(x, y, num):
    if num == -1 or num >= 6:
        return Hole(x, y, num)
    elif num:
        return Block(num)
    return 0


T = int(input())
for t in range(1, T+1):
    Hole.member = []
    N = int(input())
    board = [[5] + [int(num) for num in input().split()] + [5] for _ in range(N)]
    board = [[5] * (N + 2)] + board + [[5] * (N + 2)]
    for i in range(N + 2):
        for j in range(N + 2):
            board[i][j] = get_class(i, j, board[i][j])
    max_score = -1
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if board[i][j] == 0:
                for k in range(4):
                    ball = Ball(i, j, k)
                    ball.move()
                    obj = board[ball.x][ball.y]
                    if not obj:
                        continue
                    ball = Ball(i, j, k)
                    board[i][j] = Hole(i, j, -1)
                    while True:
                        ball.move()
                        if ball.is_repeated():
                            break
                        obj = board[ball.x][ball.y]
                        if obj:
                            obj.interact(ball)
                            if obj.num == -1:
                                max_score = max(max_score, ball.score)
                                break
                    board[i][j] = 0
    print(f'#{t} {max_score}')
