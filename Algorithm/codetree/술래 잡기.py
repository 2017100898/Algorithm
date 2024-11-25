direction = [(-1, 0) , (0, 1), (1, 0), (0, -1)]
move_track = []
tree_list = []
runner_list = []

n, m, h, k = list(map(int, input().split()))

for i in range(m):
    x, y, d = list(map(int, input().split()))
    if d == 1:
        dx, dy = 0, 1
    else:
        dx, dy = 1, 0
    runner_list.append([x - 1, y - 1, dx, dy , True]) # x, y, dx, dy, alive?

for i in range(h):
    x, y = list(map(int, input().split()))
    tree_list.append((x - 1, y- 1))


############### 달팽이 만들기
for i in range(1, n, 2):
    for j in range(0, i):
        move_track.append(direction[0])
    for j in range(0, i):
        move_track.append(direction[1])
    for j in range(0, i + 1):
        move_track.append(direction[2])
    for j in range(0, i + 1):
        move_track.append(direction[3])

for j in range(1, n):
    move_track.append(direction[0])

move_len = len(move_track)
for i in range(move_len - 1, -1, -1):
    a = move_track[i][0] * -1
    b = move_track[i][1] * -1
    move_track.append((a, b))


chaser = [n // 2, n // 2, move_track[0][0], move_track[0][1]] # x, y, dx, dy

def distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def in_range(x, y):
    if x not in range(n):
        return False
    elif y not in range(n):
        return False
    else:
        return True

track_num = 0
score = 0

for k_turn in range(k):
    get_num = 0

    c_x, c_y, c_dx, c_dy = chaser
    chaser_sights = []

    # 도망자의 움직임
    for m_turn in range(m):
        r_x, r_y, r_dx, r_dy, alive = runner_list[m_turn]
        
        if alive == True:
            if distance(r_x, r_y, c_x, c_y) <= 3:
                r_nx = r_x + r_dx
                r_ny = r_y + r_dy
                
                if in_range(r_nx, r_ny):
                    if (r_nx, r_ny) == (c_x, c_y):
                        continue
                    else:
                        runner_list[m_turn][0] = r_nx
                        runner_list[m_turn][1] = r_ny
                    
                else: # in range 아니면 반대방향으로 전환, 술래 없으면 전진
                    runner_list[m_turn][2] = -1 * runner_list[m_turn][2]
                    runner_list[m_turn][3] = -1 * runner_list[m_turn][3]
                    r_x, r_y, r_dx, r_dy, alive = runner_list[m_turn]

                    r_nx = r_x + r_dx
                    r_ny = r_y + r_dy
                    
                    if (r_nx, r_ny) == (c_x, c_y):
                        continue

                    else:
                        runner_list[m_turn][0] = r_nx
                        runner_list[m_turn][1] = r_ny

    # 술래의 움직임
    c_nx, c_ny = c_x + c_dx, c_y + c_dy
    chaser[0] = c_nx
    chaser[1] = c_ny
    

    if len(move_track) - 1 == track_num:
        track_num = 0
    else:
        track_num += 1

    chaser[2] = move_track[track_num][0]
    chaser[3] = move_track[track_num][1]

    c_x, c_y, c_dx, c_dy = chaser

    for i in range(0, 3):
        c_nxtest = c_nx + (c_dx * i)
        c_nytest = c_ny + (c_dy * i)

        if in_range(c_nxtest, c_nytest):
            chaser_sights.append((c_nxtest, c_nytest))

    for m_turn in range(m):
        if runner_list[m_turn][4] == True:
            if (runner_list[m_turn][0], runner_list[m_turn][1]) in chaser_sights:
                if (runner_list[m_turn][0], runner_list[m_turn][1]) in tree_list:
                    continue
                else:
                    runner_list[m_turn][4] = False
                    get_num += 1

    score += (get_num * (k_turn + 1))

print(score)