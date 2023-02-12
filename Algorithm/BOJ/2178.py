cmd = input().split()
N, M = int(cmd[0]), int(cmd[1])

vec = []

# 입력값을 벡터에 넣어줌
for i in range(0, N):
    miniVec = []
    miro = input()

    for j in range(0, M):
        miniVec.append(int(miro[j]))
        
    vec.append(miniVec)

length = vec.copy()

# 이동할 수 있는 경우의 수 (총 4가지)
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(N, M, vec):
    visit = []

    #시작점은 0, 0
    queue = [(0, 0)]

    while queue:
        # queue에서 현재 노드를 꺼냄
        node  = queue.pop(0)

        # 방문하지 않은 노드라면, 방문처리
        if node not in visit:
            visit.append(node)
            
            # 다음 이동할 노드를 찾기 위해 양옆, 위아래 확인
            # 벡터 사이즈를 넘지 않고 이동 가능하면 이동을 위해 queue에 넣음
            # 최단거리를 파악하기 위해 다음 노드의 값을 현재 노드 값의 +1을 해줌
            for j in move:
                next_node = tuple(i + j for i, j in zip(node, j))
                if next_node[0] >= 0 and next_node[1] >= 0 and next_node[0] < N and next_node[1] < M and vec[next_node[0]][next_node[1]] == 1:
                    queue.append(next_node)
                    length[next_node[0]][next_node[1]] = length[node[0]][node[1]] + 1
                    
    return length[N-1][M-1]

print(bfs(N, M, vec))
