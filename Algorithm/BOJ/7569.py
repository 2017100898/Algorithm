import sys
from collections import deque

cmd = input().split()
M, N, H = int(cmd[0]), int(cmd[1]), int(cmd[2])

# 토마토를 저장할 vector
d3Vec = []
queue = deque([])

for j in range(0, H):
    d2Vec = []
    for i in range(0, N):
        line = list(map(int, sys.stdin.readline().split()))
        for k in range(0, M):
            # 값이 1일 때, 시작점이 되므로 해당 인덱스를 queue에 넣어줌
            if line[k] == 1:
                queue.append((j, i, k))

        d2Vec.append(line)
    d3Vec.append(d2Vec)

# 퍼져나갈 수 있는 경로 (6가지)
move = [(0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

def bfs(queue, vec, H, N, M):
    while queue:
        # 현재 node는 queue에서 하나씩 가져옴
        node  = queue.popleft()

        # 이동할 수 있는 모든 경로 고려하여 다음 노드 선택
        for j in move:
            next_node = tuple(i + j for i, j in zip(node, j))
            
            # 만일 다음 노드가 벡터를 벗어나면 포함시키지 않음
            # 또한 아직 익지 않은 노드 (0)만 고려함
            if next_node[0] >= 0 and next_node[1] >= 0 and next_node[2] >= 0 and next_node[0] < H and next_node[1] < N and next_node[2] < M and vec[next_node[0]][next_node[1]][next_node[2]] == 0 :
                queue.append(next_node)

                # 며칠이 걸리는지 파악하기 위해 현재 노드의 값 +1 한 값을 다음 노드에 입력해줌
                vec[next_node[0]][next_node[1]][next_node[2]] = vec[node[0]][node[1]][node[2]] + 1
                    
    return vec

result = bfs(queue, d3Vec, H, N, M)
max = 0

# 최종 vector를 순회하여 최대 며칠이 걸리는지 파악
# 안익은 토마토가 있으면 -1 반환
for j in range(0, H):
    for i in range(0, N):
        for k in range(0, M):
            if result[j][i][k] == 0:
                print(-1)
                exit(0)
            elif result[j][i][k]  > max:
                max = result[j][i][k] 

print(max-1)