'''
[원칙]
1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다. (청소 후 -1로 변경)
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우, 
(1) 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
(2) 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다. (stop)

3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
(1) 반시계 방향으로 90도 회전한다.
(2) 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
(3) 1번으로 돌아간다.
'''

# N x M 크기의 직사각형 방
N, M = list(map(int, input().split()))

# 청소기의 좌표 (r , c)와 방향 d
# 방향: 0 -> 북, 1 -> 동, 2 -> 남, 3->서
x, y, d = list(map(int, input().split()))

# 장소의 상태
# 0:청소되지않은 빈칸
# 1: 벽
# 방의 가장 북,남,서,동쪽 줄 중 하나 이상에 위치한 모든 칸에 벽 있음
mats = []
for _ in range(N):
    mat = list(map(int, input().split()))
    mats.append(mat)
    
# 반시계 회전
def unclock(direction):
    if direction == 0: return 3
    elif direction >= 1: return direction - 1
    
def move(direction):
    if direction == 0: return [-1, 0]
    elif direction == 1: return [0, 1]
    elif direction == 2: return [1, 0]
    elif direction == 3: return [0, -1]

def back(direction):
    if direction == 0: return [1, 0]
    elif direction == 1: return [0, -1]
    elif direction == 2: return [-1, 0]
    elif direction == 3: return [0, 1]
    
    
def can_go(x, y):
    if x not in range(N):
        return False
    
    elif y not in range(M):
        return False
    
    elif mats[x][y] == 1:
        return False
    
    else:
        return True

clean_cnt = 0

while True:
    if mats[x][y] == 0:
        mats[x][y] = -1
        clean_cnt += 1
        
    poss_clean = False
    
    dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
    
    for dx, dy in zip(dxs, dys):
        nx, ny = dx + x, dy + y
        if can_go(nx, ny):
            if mats[nx][ny] == 0 :
                poss_clean = True
    
    
    if poss_clean == True:
        
        while True:
            d = unclock(d)
            dx, dy = move(d)
            nx, ny = dx + x, dy + y
            
            if can_go(nx, ny):
                if mats[nx][ny] == 0:
                    x, y = nx, ny
                    break
        
    else:
        dx, dy = back(d)
        nx, ny = dx + x, dy + y
        
        if mats[nx][ny] == 1:
            break
        else:
            x, y= nx, ny
            
print(clean_cnt)
            