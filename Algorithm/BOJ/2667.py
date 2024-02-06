from collections import deque


N = int(input())
mats = []

for _ in range(N):
    mat = list(map(int, input()))
    mats.append(mat)
    
visited = [[0 for _ in range(N)] for _ in range(N)]
Q = deque()

def can_go(x, y):
    if x not in range(0, N):
        return False
    
    elif y not in range(0, N):
        return False

    elif visited[x][y] == 1 or mats[x][y] == 0:
        return False

    else:
        return True
    
def bfs():
    order = 1
    dxs = [0, 0, -1, 1]
    dys = [1, -1, 0, 0]
    
    while Q:
        x, y = Q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if can_go(nx, ny):
                Q.append([nx, ny])
                visited[nx][ny] = 1
                order += 1
    
    return order

result = []

for i in range(N):
    for j in range(N):
        if mats[i][j] == 1:
            if visited[i][j] == 0:
                Q.append([i, j])
                visited[i][j] = 1
                
                num = bfs()
                result.append(num)

result.sort()
print(len(result))
for i in result:
    print(i)