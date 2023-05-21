# N x N 크기의 땅
# 각 땅에는 1개의 나라 존재
# 더 이상의 인구 이동이 없을 때까지 인구 이동 지속
# 두 나라의 인구 차이가 L명 이상, R명 이하 => 국경선을 연다
# 국경선이 열려 있으면 두 나라는 하루동안 연합이라 한다 => 연합 나라의 각 칸 인구 수는 (연합인구수 / 칸 개수)
# 연합 해체하고 국경선을 닫는다

# N, L, R 및 땅 정보를 입력 받음
N, L, R = map(int, input().split())
Mat = []

for i in range(0, N):
    miniMat = list(map(int, input().split()))
    Mat.append(miniMat)

# 인구 이동

result = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# bfs 구현

def bfs(x, y):
    global visit, Mat
    queue = [(x, y)]
    unions = [(x, y)]

    while queue:
        node = queue.pop(0)  
        
        # node를 기준으로 상하좌우를 확인하고 차이가 L ~ R 사이라면 해당 나라를 Union에 넣는다
        for i in range(0, 4):
            if (0 <= node[0] + dx[i] < N) and (0 <= node[1] + dy[i] < N) and visit[node[0] + dx[i]][node[1] + dy[i]] == 0:
                if L <= abs(Mat[node[0]][node[1]] - Mat[node[0] + dx[i]][node[1] + dy[i]]) <= R:
                    visit[node[0] + dx[i]][node[1] + dy[i]] = 1
                    queue.append((node[0] + dx[i], node[1] + dy[i]))
                    unions.append((node[0] + dx[i], node[1] + dy[i]))

    return unions

# 더 이상 인구 이동이 없을 때까지 아래 코드를 반복

while True:
    visit = [[0 for w in range(N)] for h in range(N)]
    moved = False

    for x in range(0, N):
        for y in range(0, N):
            if visit[x][y] == 0:
                visit[x][y] = 1
                sum = 0
                # x, y 를 기준으로 bfs를 실행
                unions = bfs(x, y)

                if len(unions) > 1:
                    moved = True
                    
                    # 인구 합병
                    for j in unions:
                        sum += Mat[j[0]][j[1]]
                    
                    for j in unions:
                        Mat[j[0]][j[1]] = sum // len(unions)
    
    if moved == False:
        break
    
    result += 1

print(result)