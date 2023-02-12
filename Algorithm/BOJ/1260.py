cmd = input().split()
N, M, V = int(cmd[0]), int(cmd[1]), int(cmd[2])

# 노드끼리의 연결성을 저장할 리스트
edges = []

for i in range(0, N):
    edges.append([])

for i in range(0, M):
    edge = input().split()
    start, end  = int(edge[0]), int(edge[1])
    edges[start - 1].append(end)
    start, end  = int(edge[1]), int(edge[0])
    edges[start - 1].append(end)

for i in range(0, N):
    edges[i].sort()

# DFS
# visit은 방문한 노드의 목록을 저장하는 리스트
visit = []

def dfs(edges, curr, visit):
    # 현재 node 를 방문한 리스트에 넣어줌
    visit.append(curr)

    # 현재 node와 연결된 노드들을 탐색
    for i in edges[curr - 1]:
        if i not in visit:
            # 연결된 노드 중 방문하지 않은 노드를 방문, 재귀로 구현
            dfs(edges, i, visit)
    return

dfs(edges, V, visit)
print(' '.join(str(e) for e in visit))

# BFS
# visit은 방문한 노드의 목록을 저장하는 리스트
visit = []

def bfs(edges, curr, visit):
    # queue 는 방문할 노드의 목록을 저장하는 리스트
    # 시작 시 첫 노드를 큐에 넣어줌
    queue = [curr]
    
    # 큐의 목록이 바닥날 때까지 loop 돌림
    while queue:
        # queue 에 있는 값을 순차적으로 꺼내서 방문
        curr = queue.pop(0)

        if curr not in visit:
            # visit 에 저장
            visit.append(curr)
            # 해당 노드의 자식 노드들을 큐에 추가
            for i in edges[curr - 1]:
                queue.append(i)
    return

bfs(edges, V, visit)
print(' '.join(str(e) for e in visit))
