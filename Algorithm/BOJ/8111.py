from collections import deque

T = int(input())
cnt = 1

def bfs(N):
    Q = deque()
    Q.append('1')
    visited = set()

    while Q:
        x = Q.popleft()

        if len(x) > 100:
            return -1
        
        x = int(x)
        remain = x % N

        if remain == 0:
            return x
        
        if remain not in visited:
            visited.add(remain)
            Q.append(str(x) + '0')
            Q.append(str(x) + '1')

for i in range(T):
    N = int(input())
    
    print(bfs(N))