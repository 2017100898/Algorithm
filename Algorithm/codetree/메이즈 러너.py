#재료
N, M, K = list(map(int, input().split()))

miro_arr = []
people_arr = [[[] for _ in range(N)] for _ in range(N)]
people_dict = {}

for i in range(N):
    temp = list(map(int, input().split()))
    miro_arr.append(temp)

for i in range(1, M+1):
    r, c = list(map(int, input().split()))
    people_dict[i] = [r - 1, c - 1, 0, False] # r, c, 이동횟수, 탈출 여부 
    people_arr[r-1][c-1].append(i)
    # -1은 필수

exit_r, exit_c = list(map(int, input().split())) # 출구 위치
exit = [exit_r - 1, exit_c - 1] # -1은 필수
people_arr[exit_r - 1][exit_c - 1].append(-1)

def dist(r_1, c_1, r_2, c_2):
    distance = abs(r_1 - r_2) + abs(c_1 - c_2)
    return distance

def print_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j] , end = " ")
        print()
    print()

def in_range(x, y):
    if x not in range(N):
        return False
    elif y not in range(N):
        return False
    else:
        return True

def can_move(x, y):
    if x not in range(N):
        return False
    elif y not in range(N):
        return False
    elif miro_arr[x][y] != 0:
        return False
    else:
        return True

#게임 시작
INF = 99999999

for k in range(1, K + 1):
    #print("K : " , k)
    
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    exit_r, exit_c = exit
    
    # 참가자 이동
    for i in range(1, len(people_dict) + 1):
        p_r, p_c, _, p_out = people_dict[i]

        if p_out == False:
            curr_dist = dist(exit_r, exit_c, p_r, p_c)
            next_dx, next_dy = 0, 0

            for dx, dy in zip(dxs, dys): #상하좌우를 순회하며, 이동했을 때 거리가 줄어드는지 파악
                p_nr, p_nc = p_r + dx, p_c + dy # 이동해본다
                if can_move(p_nr, p_nc): #이동이 가능하다면
                    next_dist = dist(exit_r, exit_c, p_nr, p_nc) #출구와의 거리를 구하고
                    if curr_dist > next_dist: #현재의 값과 다른 값들보다 거리가 더 줄어들었으면
                        curr_dist = next_dist # curr_dist을 업데이트 한다
                        next_dx, next_dy = dx, dy #이동할 곳을 기록한다
            
            if (next_dx, next_dy) != (0, 0): #고려해봤을 때 이동할 만한 곳이 있다면 ?
                # 이동한다
                # dict, arr를 함께 이동시켜준다
                next_nx, next_ny = p_r + next_dx, p_c + next_dy

                people_arr[p_r][p_c].remove(i) # 기존에 있던 곳에서 삭제
                people_arr[next_nx][next_ny].append(i)
                people_dict[i][0] = next_nx
                people_dict[i][1] = next_ny
                people_dict[i][2] += 1

                #이동한 곳에 출구가 있으면, 탈출 시킨다

                if (next_nx, next_ny) == (exit_r, exit_c):
                    people_dict[i][3] = True
                    people_arr[next_nx][next_ny].remove(i)

        else: #이미 탈출한 사람에 대해서는 pass
            continue
    
    #print_arr(people_arr)
    alived = False

    for i in range(1, len(people_dict) + 1):
        p_r, p_c, _, p_out = people_dict[i]
        if p_out == False:
            alived = True

    if alived == False:
        break
    
    #print("Alived : ", alived)

    # 블럭회전
    # 가장 작은 정사각형 찾기
    min_n = INF
    for i in range(1, len(people_dict) + 1):
        p_r, p_c, _, p_out = people_dict[i]

        if p_out == False:
        
            diff_x, diff_y = abs(exit_r - p_r) , abs(exit_c - p_c)
            diff = max(diff_x, diff_y)

            if diff < min_n:
                min_n = diff

    #print("Min square n: " , min_n)
    square_r, square_c = 0, 0 # sqaure의 좌상단 값을 기록 해둘 변수

    for i in range(N - min_n):
        breaked = False
        for j in range(N - min_n):
            for p in range(1, len(people_dict) + 1):
                p_r, p_c, _, p_out = people_dict[p]
                if p_out == False:
                    if p_r in range(i, i + min_n + 1) and p_c in range(j, j + min_n + 1):
                        if exit_r in range(i, i + min_n + 1) and exit_c in range(j, j + min_n + 1):
                            square_r, square_c = i, j
                            breaked = True
                            break;
            
            if breaked == True:
                break;
        if breaked == True:
            break;
            
    # 가장 작은 정사각형의 길이 (min_n  + 1)와 최상단 (square_r, square_c) 찾음
    # 사각형 회전

    #사각형 저장해둘 임시 장소
    mini_square = []
    mini_people = []
    
    #print("SQ : ", square_r ,square_c)
    #print_arr(people_arr)

    for i in range(square_c, square_c + min_n + 1):
        mini_sqaure_temp = []
        mini_people_square_temp = []

        for j in range(square_r + min_n, square_r - 1, -1):
            if miro_arr[j][i] > 0:
                val = miro_arr[j][i] - 1
            else:
                val = miro_arr[j][i]

            mini_sqaure_temp.append(val)
            mini_people_square_temp.append(people_arr[j][i])
            
        mini_square.append(mini_sqaure_temp)
        mini_people.append(mini_people_square_temp)
    
    #print_arr(mini_people)

    for i in range(square_r, square_r + min_n + 1):
        for j in range(square_c, square_c + min_n + 1):
            miro_arr[i][j] = mini_square[i - square_r][j - square_c]
            people_arr[i][j] = mini_people[i - square_r][j - square_c]

            if mini_people[i - square_r][j - square_c] != []:
                for temp_p in mini_people[i - square_r][j - square_c]:
                    if temp_p == -1:
                        exit = (i, j)
                    else:
                        people_dict[temp_p][0] = i
                        people_dict[temp_p][1] = j
    

    
    #print("Exit: " , exit)
    #print_arr(people_arr)

cnt = 0

for i in range(1, len(people_dict) + 1):
    _, _, n , _ = people_dict[i]
    cnt += n

print(cnt)
print(exit[0] + 1, exit[1] + 1)