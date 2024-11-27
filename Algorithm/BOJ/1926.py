# 어떤 도화지에 그림이 있을 때, 
# 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이 출력

from collections import deque

n, m = list(map(int, input().split()))
mat = []

for _ in range(n):
    min_mat = list(map(int, input().split()))
    mat.append(min_mat)


def can_go(x, y):
    if x not in range(n):
        return False
    elif y not in range(m):
        return False
    elif mat[x][y] == 0:
        return False
    else:
        return True


def bfs(i, j):
    global mat
    size = 1

    dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
    Q = deque([])
    Q.append((i, j))
    mat[i][j] = 0

    while Q:
        x, y = Q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = dx + x
            ny = dy + y

            if can_go(nx, ny):
                Q.append((nx, ny))
                mat[nx][ny] = 0
                size += 1
    
    return size

max_size = 0
cnt_num = 0

for i in range(n):
    for j in range(m):
        if mat[i][j] == 1:
            cnt_num += 1
            size = bfs(i, j)

            if size >= max_size:
                max_size = size

print(cnt_num)
print(max_size)