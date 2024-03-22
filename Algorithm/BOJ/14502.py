# 1. (완전 탐색) 벽을 3개 세운다.
# 2. (BFS) 바이러스 퍼트린다.
# 3. (BFS) 안전영역을 count 한다.

from collections import deque
from itertools import combinations

# 0: 빈칸
# 1: 벽
# 2: 바이러스

N, M = list(map(int, input().split()))
arr = []
num = []

for i in range(N):
    temp = list(map(int, input().split()))

    for j in range(M):
        if temp[j] == 0:
            num.append((i, j))
    arr.append(temp)


comb = list(combinations(num, 3))

# (comb % M, comb // M)

def can_go(x, y, c_list):
    
    if x not in range(N):
        return False
    
    elif y not in range(M):
        return False
    
    elif visited[x][y] != 0 or arr[x][y] == 1:
        return False
    
    elif (x, y) in c_list:
        return False
    
    else:
        return True

def bfs(c_list):
    dxs = [0, 1, 0, -1]
    dys = [1, 0 ,-1, 0]
    
    while Q:
        x, y = Q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx = dx + x
            ny = dy + y
            
            if can_go(nx, ny, c_list):
                Q.append((nx, ny))
                visited[nx][ny] = 1

                
Q = deque()
max_saftey = 0


for cs in comb:
    # 벽 세울 곳 선정
    visited = [[0 for _ in range(M)] for _ in range(N)]

    # 퍼뜨리기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2 and visited[i][j] == 0:
                Q.append((i , j))
                visited[i][j] = 1
                bfs(cs)

    safety = 0

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and arr[i][j] == 0:
                if (i , j ) not in cs:
                    safety += 1

        max_saftey = max(safety, max_saftey)

print(max_saftey)