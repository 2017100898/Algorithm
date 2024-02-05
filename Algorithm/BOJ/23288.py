N, M, K = list(map(int, input().split()))
mats  = []

for _ in range(N):
    mat = list(map(int, input().split()))
    mats.append(mat)

init_dice = [
    [0, 2, 0],
    [4, 1, 3],
    [0, 5, 0],
    [0, 6, 0]]

dice = init_dice.copy()
cnt = 0

x = 0  #위치
y = 0 #위치

cmd  = "right"

def turn_dice(dice, cmd):
    if cmd == "right":
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]
        
    elif cmd == "left":
        dice[3][1], dice[1][0], dice[1][1], dice[1][2] = dice[1][0], dice[1][1], dice[1][2], dice[3][1]
        
    elif cmd == "up":
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]
        
    elif cmd == "down":
        dice[1][1], dice[2][1], dice[3][1], dice[0][1] = dice[0][1], dice[1][1], dice[2][1], dice[3][1]
    
    return dice
        
def move_xy(cmd):
    if cmd == "right":
        return (0, 1)
    
    elif cmd == "left":
        return (0, -1)
    
    elif cmd == "up":
        return (-1, 0)
    
    elif cmd == "down":
        return (1, 0)
    
def can_move(x, y):
    if x not in range(0, N):
        return False
    
    elif y not in range(0, M):
        return False
    
    else:
        return True

num = 1
visitied = [[0 for _ in range(M)] for _ in range(N)]

def dfs(x, y, target_num):
    global num, visitied

    dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
    
    for dx, dy in zip(dxs, dys):
        n_x, n_y = x+dx, y+dy
        if can_move(n_x, n_y):
            if visitied[n_x][n_y] == 0:
                if mats[n_x][n_y] == target_num:
                    num += 1
                    visitied[n_x][n_y] = 1
                    dfs(n_x, n_y, target_num)

for i in range(K):
    num = 1
    visitied = [[0 for _ in range(M)] for _ in range(N)]
            
    dxy = move_xy(cmd)
    
    if can_move(x + dxy[0], y + dxy[1]):
        x, y = x + dxy[0], y + dxy[1]
        dice = turn_dice(dice, cmd)
    else:
        if cmd == "right": cmd = "left"
        elif cmd == "up": cmd = "down"
        elif cmd == "left": cmd = "right"
        elif cmd == "down": cmd = "up"
        
        dxy = move_xy(cmd)
        
        x, y = x + dxy[0], y + dxy[1]
        dice = turn_dice(dice, cmd)

    visitied[x][y] = 1
    A = dice[3][1]
    B = mats[x][y]

    dfs(x, y, B)

    # 칸수 * 정수 (mats[x][y])
    cnt += (num * mats[x][y]) 
    
    if A > B:
        if cmd == "right": cmd = "down"
        elif cmd == "down": cmd = "left"
        elif cmd == "left": cmd = "up"
        elif cmd == "up": cmd = "right"

    elif A < B:
        if cmd == "right": cmd = "up"
        elif cmd == "up": cmd = "left"
        elif cmd == "left": cmd = "down"
        elif cmd == "down": cmd = "right"

    else:
        pass


print(cnt)