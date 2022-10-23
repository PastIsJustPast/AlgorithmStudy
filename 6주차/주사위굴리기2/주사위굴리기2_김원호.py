'''
        메모리(kb) 시간(ms)
python3 30948    916
pypy3   149520   592
'''

class Dice:
    def __init__(self, x, y, upside, downside, eastside, westside, southside, northside, head):
        self.x = x
        self.y = y
        self.north_south = [upside, northside, downside, southside]
        self.east_west = [upside, eastside, downside, westside]
        self.head = head
        self.score = 0

    def move(self):
        nx = self.x + dx[self.head]
        ny = self.y + dy[self.head]
        if not(0 <= nx < N and 0 <= ny < M):
            self.head = (self.head + 2) % 4
            self.move()
            return
        self.x = nx
        self.y = ny
        self.rotate_dice()
        self.get_score(self.x, self.y, set())
        self.rotate_head()

    def rotate_dice(self):
        if self.head % 2:
            self.east_west = self.east_west[-dy[self.head]:] + self.east_west[:-dy[self.head]]
            self.north_south[0], self.north_south[2] = self.east_west[0], self.east_west[2]
        else:
            self.north_south = self.north_south[dx[self.head]:] + self.north_south[:dx[self.head]]
            self.east_west[0], self.east_west[2] = self.north_south[0], self.north_south[2]

    def rotate_head(self):
        board_num = board[self.x][self.y]
        dice_num = self.north_south[2]
        self.head = (self.head + (dice_num > board_num) - (dice_num < board_num)) % 4

    def get_score(self, x, y, visit):
        self.score += board[x][y]
        visit.add((x, y))
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == board[x][y] and (nx, ny) not in visit:
                    visit.add((nx, ny))
                    self.get_score(nx, ny, visit)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M, K = map(int, input().split())
board = [[int(x) for x in input().split()] for _ in range(N)]
dice = Dice(0, 0, 1, 6, 3, 4, 5, 2, 1)
for _ in range(K):
    dice.move()
print(dice.score)
