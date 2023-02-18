import sys
from collections import deque

cmd = input().split()
M, N = int(cmd[0]), int(cmd[1])


d2Vec = []
queue = deque([])

for i in range(0, N):
    line = list(map(int, sys.stdin.readline().split()))
    for k in range(0, M):
        if line[k] == 1:
            queue.append((i, k))

    d2Vec.append(line)

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(queue, vec, N, M):
    while queue:
        node  = queue.popleft()

        for j in move:
            next_node = tuple(i + j for i, j in zip(node, j))

            if next_node[0] >= 0 and next_node[1] >= 0 and next_node[0] < N and next_node[1] < M and vec[next_node[0]][next_node[1]] == 0 :
                queue.append(next_node)
                vec[next_node[0]][next_node[1]] = vec[node[0]][node[1]] + 1
                    
    return vec

result = bfs(queue, d2Vec, N, M)
max = 0

for i in range(0, N):
    for k in range(0, M):
        if result[i][k] == 0:
            print(-1)
            exit(0)
        elif result[i][k]  > max:
            max = result[i][k] 

print(max-1)