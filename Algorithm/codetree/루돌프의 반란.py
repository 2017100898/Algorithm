N, M, P, C, D = list(map(int, input().split()))
R_r, R_c = list(map(int, input().split()))

rudolf_info = [R_r - 1, R_c - 1, 0, 0] # x, y, dx, dy
santa_dict = {}
santa_arr = [[0 for _ in range(N)] for _ in range(N)]

for i in range(P):
    S_p, S_r, S_c = list(map(int, input().split()))
    santa_dict[S_p] = [S_r - 1, S_c - 1, 0, 0, -1, True, 0] # x, y, dx, dy, when_sleep, alive, score
    santa_arr[S_r - 1][S_c - 1] = S_p


def distance(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def in_range(x, y):
    if x not in range(N):
        return False
    elif y not in range(N):
        return False
    else:
        return True

INF = 9999999999

def print_arr(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()
    print()

for m in range(1, M + 1):

    #print("******** Turn : ", m)

    # 루돌프 이동
    
    # 산타와 루돌프 거리 계산 및 가장 가까운 애 찾음

    R_x, R_y, _, _ = rudolf_info
    min_distance = INF
    min_santa = 0
    

    for i in range(1, P + 1):
        S_x, S_y, _, _, _, alive, _ = santa_dict[i]
        
        if alive == True:
            dist = distance(R_x, R_y, S_x, S_y)
            if min_distance > dist:
                min_distance = dist
                min_santa = i
            elif min_distance == dist:
                if santa_dict[min_santa][0] < S_x:
                    min_santa = i
                elif santa_dict[min_santa][0] == S_x:
                    if santa_dict[min_santa][1] < S_y:
                        min_santa = i
    
    S_x, S_y, _, _, _, alive, _ = santa_dict[min_santa]
    
    if S_x < R_x : R_dx = -1
    elif S_x > R_x : R_dx = 1
    else: R_dx = 0

    if S_y < R_y : R_dy = -1
    elif S_y > R_y : R_dy = 1
    else: R_dy = 0

    rudolf_info[2] = R_dx
    rudolf_info[3] = R_dy

    R_nx = R_dx + R_x
    R_ny = R_dy + R_y
    #print("Rudolf : " , R_nx, R_ny)
    rudolf_info[0] = R_nx
    rudolf_info[1] = R_ny

    if santa_arr[R_nx][R_ny] != 0:
        target_santa = santa_arr[R_nx][R_ny]
        S_x, S_y, S_dx, S_dy, _, alive, _ = santa_dict[target_santa]

        # 루돌프가 움직여서 충돌
        # 해당 산타는 +C 점수
        santa_dict[target_santa][6] += C # C 점수 얻음
        santa_dict[target_santa][4] = m # m 번째에 기절
        # 동시에 루돌프가 이동해온 방향으로 C 만큼 밀려남

        S_dx, S_dy = R_dx, R_dy
        S_nx = S_x + S_dx * C
        S_ny = S_y + S_dy * C

        if in_range(S_nx, S_ny) == False:
            santa_dict[target_santa][5] = False  # range 밖이면 죽음
            santa_arr[S_x][S_y] = 0
        
        else:
            if santa_arr[S_nx][S_ny] == 0:
                santa_arr[S_x][S_y] = 0
                santa_arr[S_nx][S_ny] = target_santa
                santa_dict[target_santa][0], santa_dict[target_santa][1] = S_nx, S_ny

            else: #누군가 있으면 상호작용이 일어남
                target_i = 0
                temp = []
                temp.append(santa_arr[S_x][S_y])
                santa_arr[S_x][S_y] = 0
                
                while True:
                    con_nx = S_x + S_dx * C + S_dx * (target_i)
                    con_ny = S_y + S_dy * C + S_dy * (target_i)

                    if in_range(con_nx, con_ny) == False:
                        santa_dict[temp[0]][5] = False
                        break

                    else:
                        if santa_arr[con_nx][con_ny] == 0:
                            santa_arr[con_nx][con_ny] = temp.pop(0)
                            santa_dict[santa_arr[con_nx][con_ny]][0] = con_nx
                            santa_dict[santa_arr[con_nx][con_ny]][1] = con_ny
                            break

                        else:
                            temp.append(santa_arr[con_nx][con_ny])
                            santa_arr[con_nx][con_ny] = temp.pop(0)
                            santa_dict[santa_arr[con_nx][con_ny]][0] = con_nx
                            santa_dict[santa_arr[con_nx][con_ny]][1] = con_ny
                            target_i += 1
    
    #print_arr(santa_arr)
    check_alive = False
    for i in range(1, P + 1):
        S_x, S_y, _, _, when_sleep, alive, _ = santa_dict[i]
        if alive == True:
            check_alive =True

    if check_alive == False:
        break

    # 산타 이동 (1 ~ P번)
    R_x, R_y, _, _ = rudolf_info
    can_move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(1, P + 1):
        S_x, S_y, _, _, when_sleep, alive, _ = santa_dict[i]

        if when_sleep + 2 <= m and alive == True:
            curr_dist = distance(R_x, R_y, S_x, S_y)
            can_moving = False
            fin_c = 0

            for c in range(len(can_move)):
                S_dx, S_dy = can_move[c]
                next_dist = distance(R_x, R_y, S_x + S_dx, S_y + S_dy)

                if curr_dist > next_dist:
                    if in_range(S_x + S_dx, S_y + S_dy) and santa_arr[S_x + S_dx][S_y + S_dy] == 0:
                        #print(curr_dist, next_dist)
                        S_nx = S_x + S_dx
                        S_ny = S_y + S_dy
                        can_moving = True
                        fin_c = c
                        curr_dist = next_dist

            if can_moving == True:
                if santa_arr[S_nx][S_ny] == 0:
                    santa_arr[S_x][S_y] = 0
                    santa_arr[S_nx][S_ny] = i
                    santa_dict[i][0] = S_nx
                    santa_dict[i][1] = S_ny
                    
                    if (S_nx, S_ny) == (R_x, R_y):
                        S_dx, S_dy = can_move[fin_c]

                        santa_dict[i][6] += D
                        santa_dict[i][4] = m

                        S_x = S_nx # 이동한 곳
                        S_y = S_ny
                        S_dx = S_dx * -1
                        S_dy = S_dy * -1 #자신이 이동해온 방향의 반대로

                        S_nx = S_x + S_dx * D
                        S_ny = S_y + S_dy * D

                        if in_range(S_nx, S_ny) == False:
                            santa_dict[i][5] = False  # range 밖이면 죽음
                            santa_arr[S_x][S_y] = 0
                        
                        else:
                            if santa_arr[S_nx][S_ny] == 0: # 밀려난 곳에 다른 산타 없으면?
                                santa_arr[S_x][S_y] = 0 #기존
                                santa_arr[S_nx][S_ny] = i #밀려난 곳
                                santa_dict[i][0], santa_dict[i][1] = S_nx, S_ny

                            else: #누군가 있으면 상호작용이 일어남
                                target_i = 0
                                temp = []
                                temp.append(santa_arr[S_x][S_y])
                                santa_arr[S_x][S_y] = 0
                                
                                while True:
                                    con_nx = S_x + S_dx * D + S_dx * (target_i)
                                    con_ny = S_y + S_dy * D + S_dy * (target_i)
                                    if in_range(con_nx, con_ny) == False:
                                        santa_dict[temp[0]][5] = False
                                        break

                                    else:
                                        if santa_arr[con_nx][con_ny] == 0:
                                            santa_arr[con_nx][con_ny] = temp.pop(0)
                                            santa_dict[santa_arr[con_nx][con_ny]][0] = con_nx
                                            santa_dict[santa_arr[con_nx][con_ny]][1] = con_ny
                                            break
                                        else:
                                            temp.append(santa_arr[con_nx][con_ny])
                                            santa_arr[con_nx][con_ny] = temp.pop(0)
                                            santa_dict[santa_arr[con_nx][con_ny]][0] = con_nx
                                            santa_dict[santa_arr[con_nx][con_ny]][1] = con_ny
                                            target_i += 1
        #print_arr(santa_arr)

    #print_arr(santa_arr)
    check_alive = False
    for i in range(1, P + 1):
        S_x, S_y, _, _, when_sleep, alive, _ = santa_dict[i]
        if alive == True:
            santa_dict[i][6] += 1
            check_alive =True

    if check_alive == False:
        break

for i in range(1, P+ 1):
    print(santa_dict[i][6] , end= " ")