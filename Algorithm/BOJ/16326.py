from collections import deque
INF = 9999999
N = int(input())
mats = []

class Shark:
    def __init__(self):
        self.size = 2
        self.temp_size = 0
        self.time = 0
        self.location = [0, 0]
        
    def eat(self):
        self.temp_size += 1
        
        if self.size == self.temp_size:
            self.size += 1
            self.temp_size = 0
        
        return self.temp_size
    
    def fish_num(self):
        return self.ate_fish
    
    def move(self, location, dist):
        self.time += dist
        self.location = location
        
        return self.location
    
    def print_size(self):
        return self.size
    
shark = Shark()

for _ in range(N):
    mat = list(map(int, input().split()))
    mats.append(mat)
    
for i in range(N):
    for j in range(N):
        if mats[i][j] == 9:
            shark.location = [i , j]
            mats[i][j] = 0
            

def can_go(x, y, size):
    if x not in range(N):
        return False
    
    elif y not in range(N):
        return False
    
    elif visited[x][y] == 1 or size < mats[x][y]:
        return False
    
    else:
        return True
    
    
def bfs():
    dxs = [0, 0, 1, -1]
    dys = [1, -1, 0, 0]
    
    while Q:
        x, y = Q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x+ dx, y+dy
            
            if can_go(nx, ny, shark.size):
                Q.append([nx, ny])
                visited[nx][ny] = 1
                dp[nx][ny] = dp[x][y] + 1
                
cnt = 0     

while True:
    min_dist = INF
    s_x, s_y = shark.location

    min_x, min_y = s_x, s_y
    
    dp = [[0 for _ in range(N)] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    Q = deque()
    
    Q.append([s_x, s_y])
    visited[s_x][s_y] = 1
    dp[s_x][s_y] = 0

    bfs()
    found_fish = False

    for i in range(N):
        for j in range(N):
            if dp[i][j] != 0 and mats[i][j] != 0 and mats[i][j] < shark.print_size():
                if dp[i][j] < min_dist:
                    min_dist = dp[i][j]
                    min_x, min_y = i, j
    
    if min_dist == INF:
        break
    
    else:
        shark.move([min_x, min_y], dp[min_x][min_y])
        shark.eat()
        mats[min_x][min_y] = 0
        
print(shark.time)