from collections import deque

N = int(input())
arr = []
max_val = 0

for i in range(N):
    temp = list(map(int, input().split()))
    max_val = max(max_val, max(temp))

    arr.append(temp)

# BFS 를 통한 접근
# 만들어야 할 것: visited 변수, can_go / BFS 함수

saftey_zone = 0


def can_go(x, y, k):
    if x not in range(N):
        return False
    
    elif y not in range(N):
        return False
    
    elif visited[x][y] != 0 or arr[x][y] <= k:
        return False
    
    else:
        return True
    
Q = deque()

def BFS(start, k):
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    
    while Q:
        x, y = Q.popleft()

        for dx, dy in zip(dxs, dys):   
            nx = x + dx
            ny = y + dy

            if can_go(nx, ny, k):
                Q.append((nx, ny))
                visited[nx][ny] = start
    


max_start = 1

for k in range(0, max_val):
    start = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] > k and visited[i][j] == 0:
                start += 1
                Q.append((i, j))
                visited[i][j] = start
                BFS(start, k)
    max_start = max(max_start, start)
            
print(max_start)