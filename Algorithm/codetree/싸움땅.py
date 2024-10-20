n, m, k = list(map(int, input().split()))
# n : 격자의 크기
# m : 플레이어 수
# k : 라운드 수

gun_arr = []
people_arr = [[[] for _ in range(n)] for _ in range(n)]
people_dict = {}

for i in range(n):
    gun_arr_temp = list(map(int, input().split()))
    temp = []

    for j in range(n):
        if gun_arr_temp[j] == 0:
            temp.append([])
        else:
            temp.append([gun_arr_temp[j]])

    gun_arr.append(temp)

for i in range(1, m + 1):
    x, y, d, s = list(map(int, input().split()))

    if d == 0:
        dx, dy = -1, 0
    elif d == 1:
        dx, dy = 0, 1
    elif d == 2:
        dx, dy = 1, 0
    else:
        dx, dy = 0, -1

    people_dict[i] = [x - 1, y - 1, dx, dy, s, 0, 0] # r, c, dx, dy, 능력치, 총 공격력, 포인트
    people_arr[x-1][y-1].append(i)
    

def print_arr(arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end = " ")
        print()
    print()


def in_range(x, y):
    if x not in range(n):
        return False
    elif y not in range(n):
        return False
    else:
        return True

def turn_180(dx, dy):
    if dx == 0:
        if dy == 1:
            return (0, -1)
        elif dy == -1:
            return (0, 1)
    elif dx == 1:
        return (-1, 0)
    else:
        return (1, 0)

def turn_90(dx, dy):
    if dx == 0:
        if dy == 1:
            return (1, 0)
        elif dy == -1:
            return (-1, 0)
    elif dx == 1:
        return (0, -1)
    else:
        return (0, 1)

for k_round in range(k):
    for idx_m in range(1, m+1):
        x, y, dx, dy, s, gunpower, point = people_dict[idx_m]

        nx, ny = x + dx, y + dy

        if in_range(nx, ny) == False:
            dx, dy = turn_180(dx, dy)
            nx, ny = x + dx, y + dy
            # 방향을 바꿨으면 dict도 바꿔줌
            people_dict[idx_m][2] = dx
            people_dict[idx_m][3] = dy
        
        people_arr[x][y].remove(idx_m) # 기존에 있던 곳에서 나를 지우고
        people_arr[nx][ny].append(idx_m) # 새롭게 이동한 곳에 다시 넣음
        people_dict[idx_m][0] = nx
        people_dict[idx_m][1] = ny #dict도 수정해줌

        # 이사온 곳에 사람이 있는지 확인
        if len(people_arr[nx][ny]) == 1: # 나밖에 없으면?
            # 총이 있는지 확인
            if len(gun_arr[nx][ny]) >= 1: #총이 있으면 획득을 고려. 놓여있는 것과 내가 갖고 있는 것중 가장 큰 걸로 고름
                max_gun = max(gun_arr[nx][ny])
                if gunpower == 0: #총 없으면 그냥 가짐
                    people_dict[idx_m][5] = max_gun
                    gun_arr[nx][ny].remove(max_gun)

                else: #총 있으면
                    if max_gun > gunpower: # 내가 갖고 있는 것 보다 크면? 바꿈
                        gun_arr[nx][ny].append(gunpower)
                        gun_arr[nx][ny].remove(max_gun)
                        people_dict[idx_m][5] = max_gun
        
        elif len(people_arr[nx][ny]) > 1: #다른 플레이어가 이미 있다면?
            # 두 플레이어가 싸운다!
            a = people_arr[nx][ny][0]
            b = people_arr[nx][ny][1]

            a_x, a_y, a_dx, a_dy, a_s, a_gunpower, a_point = people_dict[a]
            b_x, b_y, b_dx, b_dy, b_s, b_gunpower, b_point = people_dict[b]

            winner = a
            loser = b

            if a_gunpower + a_s < b_gunpower + b_s:
                winner = b
                loser = a

            elif a_gunpower + a_s == b_gunpower + b_s:
                if a_s < b_s:
                    winner = b
                    loser = a
            
            
            #print("winner: ", winner)
            score = abs((a_gunpower + a_s) - (b_gunpower + b_s))
            people_dict[winner][6] += score
                        
            if people_dict[loser][5] > 0: # loser는 본인이 가진 총을 내려 놓음
                gun_arr[nx][ny].append(people_dict[loser][5])
                people_dict[loser][5] = 0

            if len(gun_arr[nx][ny]) >= 1: # winner는 총을 센걸로 바꿈
                max_gun = max(gun_arr[nx][ny])

                if people_dict[winner][5] == 0: #총 없으면 그냥 가짐
                    people_dict[winner][5] = max_gun
                    gun_arr[nx][ny].remove(max_gun)

                else: #총 있으면
                    if max_gun > people_dict[winner][5]: # 내가 갖고 있는 것 보다 크면? 바꿈
                        gun_arr[nx][ny].append(people_dict[winner][5])
                        gun_arr[nx][ny].remove(max_gun)
                        people_dict[winner][5] = max_gun

            #### loser는 새롭게 이동
            x, y, dx, dy, s, gun_power, point = people_dict[loser]

            while True:
                nx = x + dx
                ny = y + dy
                
                if in_range(nx, ny) == False:
                    dx, dy = turn_90(dx, dy)
                    nx, ny  = x + dx, y + dy

                elif len(people_arr[nx][ny]) >= 1:
                    dx, dy = turn_90(dx, dy)
                    nx, ny  = x + dx, y + dy

                else:
                    break


            people_arr[x][y].remove(loser) # 기존에 있던 곳에서 나를 지우고
            people_arr[nx][ny].append(loser) # 새롭게 이동한 곳에 다시 넣음
            people_dict[loser][0] = nx
            people_dict[loser][1] = ny #dict도 수정해줌
            people_dict[loser][2] = dx
            people_dict[loser][3] = dy


            if len(gun_arr[nx][ny]) >= 1: #새로운 곳에 총이 있으면 획득 고려
                max_gun = max(gun_arr[nx][ny])
                people_dict[loser][5] = max_gun
                gun_arr[nx][ny].remove(max_gun)
    
        #if k_round == 1:
        #    print("Gun")
        #    print_arr(gun_arr)
        #    print("People")
        #    print_arr(people_arr)

result = []
for idx_m in range(1, m+1):
    print(people_dict[idx_m][-1] , end = " ")