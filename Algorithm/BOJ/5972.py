import heapq

N, M = list(map(int, input().split()))
graph = {}

for i in range(1, N + 1):
    graph[i] = []

for i in range(M):
    A, B, C = list(map(int, input().split()))
    graph[A].append((B, C))
    graph[B].append((A, C))

Q = []
distance = [float('inf') for _ in range(N + 1)]
distance[1] = 0
heapq.heappush(Q, (0, 1))

while Q:
    curr_dist, curr_dest = heapq.heappop(Q)

    if curr_dist < distance[curr_dest]:
        continue

    for next_dest, next_dist in graph[curr_dest]:
        dist = curr_dist + next_dist
        if dist < distance[next_dest]:
            distance[next_dest] = dist
            heapq.heappush(Q, (dist, next_dest))

print(distance[N])