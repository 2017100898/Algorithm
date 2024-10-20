from collections import deque

L, N, Q = list(map(int, input().split()))
# L : 체스판 크기
# N : 기사의 수
# Q : 명령의 수

Arr = [] # 체스판 (0 번: 빈칸, -1번: 벽, 나머지는 기사 번호대로)
Bomb = [] # 함정 위치 
Kisa = {} # 기사 정보 (r, c, h, w, k)
Cmd = [] # 명령 (i , d) : i번 기사에게 방향 d로 이동

for i in range(L):
    temp = list(map(int, input().split()))
    arr_temp = []

    for j in range(L):
        if temp[j] == 1:
            Bomb.append((i, j))
            arr_temp.append(0)
        elif temp[j] == 2:
            arr_temp.append(-1)
        else:
            arr_temp.append(0)

    Arr.append(arr_temp)

for n in range(1, N + 1):
    kisa_temp = list(map(int, input().split()))
    r = kisa_temp[0] - 1
    c = kisa_temp[1] - 1
    h = kisa_temp[2]
    w = kisa_temp[3]
    k = kisa_temp[4]

    for i in range(r, r+h):
        for j in range(c, c+w):
            Arr[i][j] = n
    
    Kisa[n] = [r, c, h, w, k, 0, True]

for i in range(Q):
    cmd_temp = list(map(int, input().split()))
    Cmd.append(cmd_temp)


def can_go(x, y):
    if x not in range(L):
        return -1
    elif y not in range(L):
        return -1
    elif Arr[x][y] == -1:
        return -1
    elif Arr[x][y] == 0 or visited[x][y] != 0:
        return 0
    else:
        return 1

def print_arr(arr):
    for i in range(L):
        for j in range(L):
            print(arr[i][j] , end = " ")
        print()


def print_dxy(d):
    if d == 0 :
        dxy = (-1, 0)

    elif d == 1:
        dxy = (0, 1)

    elif d == 2:
        dxy = (1, 0)

    elif d == 3:
        dxy = (0, -1)

    return dxy

for q in range(Q):
    i, d = Cmd[q]
    # d: 위(0), 오(1), 아래(2), 왼(3)
    
    if Kisa[i][6] == False:
        continue

    ####### BFS를 통해 이동 가능한지 테스트 및 영향 받는 애들 찾기
    can_move = True
    need_to_move = []

    push_i = i
    dx, dy = print_dxy(d)
    k_r, k_c, k_h, k_w, k_k, _, _ = Kisa[i]
    queue = deque()

    visited = [[0 for _ in range(L)] for _ in range(L)]
    need_to_move.append(i)
    
    for rs in range(k_r, k_r + k_h):
        for cs in range(k_c, k_c + k_w):
            visited[rs][cs] = i
            queue.append((rs, cs))

    while queue:
        
        x, y = queue.popleft()
        nx = x + dx
        ny = y + dy

        go_res = can_go(nx, ny)

        if go_res == -1: # 벽
            can_move = False
            
        elif go_res == 1:
            k_r, k_c, k_h, k_w, k_k, _, _ = Kisa[Arr[nx][ny]]
            need_to_move.append(Arr[nx][ny])

            for rs in range(k_r, k_r + k_h):
                for cs in range(k_c, k_c + k_w):
                    visited[rs][cs] = Arr[nx][ny]
                    queue.append((rs, cs))

    if can_move == False:
        continue

    else:
        ############## 해당되는 애들 이동시킴
        need_to_move = set(need_to_move)

        for i in range(L):
            for j in range(L):
                if Arr[i][j] in need_to_move:
                    Arr[i][j] = 0

        for m in need_to_move:
            damage = 0

            r, c, h, w, k, d, live = Kisa[m]
            Kisa[m][0] += dx
            Kisa[m][1] += dy
        
            for l in range(Kisa[m][0], Kisa[m][0]+h):
                for o in range(Kisa[m][1], Kisa[m][1]+w):
                    Arr[l][o] = m

                    if (l, o) in Bomb and m != push_i:
                        damage += 1
            
            Kisa[m][5] += damage
            if Kisa[m][4] <= Kisa[m][5]:
                Kisa[m][6] = False

        for m in need_to_move:
            if Kisa[m][6] == False:
                for l in range(Kisa[m][0], Kisa[m][0]+Kisa[m][2]):
                    for o in range(Kisa[m][1], Kisa[m][1]+Kisa[m][3]):
                        Arr[l][o] = 0

result = 0

for m in Kisa:
    if Kisa[m][6] == True:
        result += Kisa[m][5]

print(result)