
# DFS : 재귀로 이루어진다.


N, M = list(map(int, input().split()))
graph = {}

for i in range(1, N + 1):
    graph[i] = []
    
for _ in range(M):
    u , v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)
    
visited = [0 for _ in range(N + 1)]

def can_go(x):
    if visited[x] == 1:
        return False
    
    else:
        return True
    
    
def dfs(x):
    for dy in graph[x]:
        if can_go(dy):
            visited[dy] = 1
            dfs(dy)
cnt = 0

for i in graph:
    if visited[i] == 0:
        cnt+= 1
        dfs(i)
        
print(cnt)