from collections import deque

n = int(input()) # 전체 사람 수
p_dict = {}

for i in range(n):
    p_dict[i+1] = []

x, y = list(map(int, input().split()))

m = int(input()) #관계의 개수

for _ in range(m):
    a, b = list(map(int, input().split()))
    p_dict[a].append(b)
    p_dict[b].append(a)

# x -> y 촌수 계산하기
Q = deque([x])
visited = [0 for _ in range(n+1)]
visited[x] = 0
breaked = False

while Q:
    curr = Q.popleft()

    if curr == y:
        print(visited[curr])
        breaked = True
        break

    for next in p_dict[curr]:
        if visited[next] == 0:
            visited[next] = visited[curr] + 1
            Q.append(next)

if breaked == False:
    print(-1)
