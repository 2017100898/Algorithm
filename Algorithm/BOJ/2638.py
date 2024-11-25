from collections import deque

N, M = list(map(int, input().split()))
mat = []

for i in range(N):
    min_mat = list(map(int, input().split()))
    mat.append(min_mat)

def can_move(x, y):
    if x not in range(N):
        return False

    elif y not in range(M):
        return False

    elif mat[x][y] == 1:
        return False

    elif visited[x][y] == 1:
        return False

    else:
        return True

dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
res = 0
mat[0][0] = -1

while True:
    fin = True

    for i in range(N):
        if 1 in mat[i]:
            fin = False

    if fin == True:
        break

    Q = deque()
    Q.append((0, 0))
    visited = [[0 for _ in range(M)] for _ in range(N)]
    
    # 1. 내부와 외부의 경계 파악
    while Q:
        x, y = Q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if can_move(nx, ny):
                mat[nx][ny] = -1
                visited[nx][ny] = 1
                Q.append((nx, ny))

    # 2. 치즈 녹임
    for i in range(N):
        for j in range(M):
            cnt = 0

            if mat[i][j] == 1:
                for dx, dy in zip(dxs, dys):
                    if i + dx in range(N) and j + dy in range(M):
                        if mat[i + dx][j + dy] == -1:
                            cnt += 1

                if cnt >= 2:
                    mat[i][j] = 0


    res += 1


print(res)