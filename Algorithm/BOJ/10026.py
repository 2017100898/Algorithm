from collections import deque

N = int(input())
arr = []

for i in range(N):
    mini_arr = list(input())
    arr.append(mini_arr)

# 적녹색약: R = G / B
def can_go(x, y):
    if x not in range(N) or y not in range(N):
        return False
    elif visited[x][y] == 1:
        return False
    elif arr[x][y] != 'B':
        return False # 적녹색약은 Blue일 때만 판단하면 됨
    else:
        return True

def can_go_red(x, y):
    if x not in range(N) or y not in range(N):
        return False
    elif visited[x][y] == 1:
        return False
    elif arr[x][y] != 'R':
        return False # R/G에 대해서 한번 더 판별 필요
    else:
        return True

def can_go_green(x, y):
    if x not in range(N) or y not in range(N):
        return False
    elif visited[x][y] == 1:
        return False
    elif arr[x][y] != 'G':
        return False # R/G에 대해서 한번 더 판별 필요
    else:
        return True


def can_go_rg(x, y):
    if x not in range(N) or y not in range(N):
        return False
    elif visited[x][y] == 1:
        return False
    elif arr[x][y] == 'B':
        return False # R/G에 대해서 한번 더 판별 필요
    else:
        return True
    
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
visited = [[0 for _ in range(N)] for _ in range(N)]
    
def bfs(x, y):
    global visited
    Q = deque()
    Q.append((x, y))

    while Q:
        x, y = Q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if can_go(nx, ny):
                visited[nx][ny] = 1
                Q.append((nx, ny))

    return 1

def bfs_red(x, y):
    global visited
    Q = deque()
    Q.append((x, y))

    while Q:
        x, y = Q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if can_go_red(nx, ny):
                visited[nx][ny] = 1
                Q.append((nx, ny))

    return 1

def bfs_green(x, y):
    global visited
    Q = deque()
    Q.append((x, y))

    while Q:
        x, y = Q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if can_go_green(nx, ny):
                visited[nx][ny] = 1
                Q.append((nx, ny))

    return 1

def bfs_rg(x, y):
    global visited
    Q = deque()
    Q.append((x, y))

    while Q:
        x, y = Q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if can_go_rg(nx, ny):
                visited[nx][ny] = 1
                Q.append((nx, ny))

    return 1

blue = 0
red = 0
green = 0
rg = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'B' and visited[i][j] == 0:
            blue += bfs(i, j)
        if arr[i][j] == 'R' and visited[i][j] == 0:
            red += bfs_red(i, j)
        if arr[i][j] == 'G' and visited[i][j] == 0:
            green += bfs_green(i, j)

visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] != 'B' and visited[i][j] == 0:
            rg += bfs_rg(i, j)


print(red+blue+green, blue+rg)