from collections import deque

N, M, K = list(map(int, input().split()))

potab_arr = []
potab_dict = {}

potab_num = 1

for i in range(N):
    temp = list(map(int, input().split()))
    potab_arr.append(temp)

    for j in range(M):
        potab_dict[potab_num] = [i, j, temp[j], 0, 0] # r,c, 공격력, 최근 공격, 최근 피해    
        potab_num += 1

def print_arr(arr):
    for i in range(N):
        for j in range(M):
            print(arr[i][j], end = " ")
        print()
    print()


def most_big(attacker_list, num):
    if len(attacker_list) >= 2:
        attacker_list_2 = []
        max_val = -1

        for i in attacker_list: ## 공격력 가장 낮은 포탑 선정
            r, c, att, recent, _ = potab_dict[i]
            
            if num == 1:
                criteria = att
            
            elif num == 2:
                criteria = recent
            
            elif num == 3:
                criteria = (r + c)
            
            elif num == 4:
                criteria = c

            if att <= 0 :
                pass

            elif max_val < criteria:
                attacker_list_2 = [i]
                max_val = criteria

            elif max_val == criteria:
                attacker_list_2.append(i)

        attacker_list = attacker_list_2

    return attacker_list


def most_small(attacker_list, num):
    if len(attacker_list) >= 2:
        attacker_list_2 = []
        min_val = 9999999

        for i in attacker_list: ## 공격력 가장 낮은 포탑 선정
            r, c, att, recent, _ = potab_dict[i]
            
            if num == 1:
                criteria = att
            
            elif num == 2:
                criteria = recent
            
            elif num == 3:
                criteria = (r + c)
            
            elif num == 4:
                criteria = c
            
            if att <= 0 :
                pass

            elif min_val > criteria:
                attacker_list_2 = [i]
                min_val = criteria

            elif min_val == criteria:
                attacker_list_2.append(i)

        attacker_list = attacker_list_2

    return attacker_list

########## 공격자 선정

def check_num(arr):
    cnt = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                cnt += 1
    
    return cnt

for k in range(1, K+1):
    attacker_list = [i for i in range(1, len(potab_dict) + 1)]
    attacker_list = most_small(attacker_list, 1)
    attacker_list = most_big(attacker_list, 2)
    attacker_list = most_big(attacker_list, 3)
    attacker_list = most_big(attacker_list, 4)

    hurted_list = [i for i in range(1, len(potab_dict) + 1)]
    hurted_list.remove(attacker_list[0])
        
    hurted_list = most_big(hurted_list, 1)
    
    hurted_list = most_small(hurted_list, 2)
    hurted_list = most_small(hurted_list, 3)
    hurted_list = most_small(hurted_list, 4)
    

    attacker = attacker_list[0]
    hurter = hurted_list[0]
    potab_dict[attacker][2] += (N + M)
    potab_dict[attacker][3] = k
    
    att_r, att_c, att_att, _, _ = potab_dict[attacker]
    hur_r, hur_c, hur_att, _, _ = potab_dict[hurter]
    
    potab_arr[att_r][att_c] = att_att
    #print_arr(potab_arr)

    ########## BFS Test [레이저 공격 시도]
    def can_go(x, y):
        if visited[x][y] != [] or potab_arr[x][y] == 0:
            return False
        else:
            return True

    Q = deque()
    visited = [[[] for _ in range(M)] for _ in range(N)]
    Q.append((att_r, att_c)) # 여기도 ~
    visited[att_r][att_c].append((att_r, att_c)) ## 공격자 선정 후 여기에 넣음! 

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    while Q:
        x, y = Q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx = dx + x
            ny = dy + y
            
            if nx not in range(N):
                if nx < 0:
                    nx = N + nx
                elif nx >= N:
                    nx = nx - N

            if ny not in range(M):
                if ny < 0: 
                    ny = M + ny
                elif ny >= M:
                    ny = ny - M

            if can_go(nx, ny):
                Q.append((nx, ny))
                for i in visited[x][y]:
                    visited[nx][ny].append(i)
                visited[nx][ny].append((nx, ny))


    if visited[hur_r][hur_c] != []:
        ## 레이저 공격 성공

        gate = visited[hur_r][hur_c]

        for g in range(1, len(gate)):
            g_r, g_c = gate[g]
            
            if g == len(gate) - 1:
                potab_arr[g_r][g_c] -= (att_att)
            else:
                potab_arr[g_r][g_c] -= (att_att // 2)
            
            if potab_arr[g_r][g_c] <= 0: # 0 이하인 포탑은 부서짐
                potab_dict[g_r * M + g_c + 1][2] = 0
                potab_dict[g_r * M + g_c + 1][4] = k
                potab_arr[g_r][g_c] = 0
            else:
                potab_dict[g_r * M + g_c + 1][2] = potab_arr[g_r][g_c]
                potab_dict[g_r * M + g_c + 1][4] = k


    else: #레이저 공격 실패 시 포탑 공격
        potab_arr[hur_r][hur_c] -= (att_att)

        if potab_arr[hur_r][hur_c] <= 0:
            potab_dict[hur_r * M + hur_c + 1][2] = 0
            potab_dict[hur_r * M + hur_c + 1][4] = k
            potab_arr[hur_r][hur_c] = 0
        else:
            potab_dict[hur_r * M + hur_c + 1][2] = potab_arr[hur_r][hur_c]
            potab_dict[hur_r * M + hur_c + 1][4] = k

        dxs, dys = [0, 1, 0, -1, 1, 1, -1, -1], [1, 0, -1, 0, 1, -1, 1, -1] #주변애들도 모두 터트림 (//2)

        for dx, dy in zip(dxs, dys):
            nx = dx + hur_r
            ny = dy + hur_c

            if nx not in range(N):
                if nx < 0:
                    nx = N + nx
                elif nx >= N:
                    nx = nx - N

            if ny not in range(M):
                if ny < 0: 
                    ny = M + ny
                elif ny >= M:
                    ny = ny - M


            if potab_arr[nx][ny] != 0 and (nx, ny) != (att_r, att_c):
                potab_arr[nx][ny] -= (att_att // 2)

                if potab_arr[nx][ny] <= 0:
                    potab_dict[nx * M + ny + 1][2] = 0
                    potab_dict[nx * M + ny + 1][4] = k
                    potab_arr[nx][ny] = 0
                else:
                    potab_dict[nx * M + ny + 1][2] = potab_arr[nx][ny]
                    potab_dict[nx * M + ny + 1][4] = k

    living_num = check_num(potab_arr)

    if living_num == 1:
        break

    # 공격 안 당한 애들 + 1점
    
    for i in range(1, len(potab_dict) + 1):
        
        if potab_dict[i][4] < k and potab_dict[i][3] < k and potab_dict[i][2] != 0:
            r, c, _, _, _ = potab_dict[i]
            potab_dict[i][2] += 1
            potab_arr[r][c] += 1
    
    #print_arr(potab_arr)

max_val = 0

for i in range(N):
    for j in range(M):
        if max_val < potab_arr[i][j]:
            max_val = potab_arr[i][j]

print(max_val)