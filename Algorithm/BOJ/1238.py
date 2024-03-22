import heapq

N, M, X = list(map(int, input().split()))
graph_init = {}
graph_reverse = {}
INF = 99999999

for i in range(M):
    v1, v2, e = list(map(int, input().split()))
    if v1 in graph_init:
        graph_init[v1].append((e, v2))
    else:
        graph_init[v1] = [(e, v2)]

    if v2 in graph_reverse:
        graph_reverse[v2].append((e, v1))
    else:
        graph_reverse[v2] = [(e, v1)]

def dijkstra(graph, start):
    dp = [INF for _ in range(N + 1)]
    dp[0] = 0
    dp[start] = 0
    Q = [(0, start)]

    while Q:
        curr_dist, curr_dest = heapq.heappop(Q)

        if curr_dist > dp[curr_dest]:
            continue

        for next_dist, next_dest in graph[curr_dest]:
            distance = curr_dist + next_dist
            if distance < dp[next_dest]:
                dp[next_dest] = distance
                heapq.heappush(Q, (distance, next_dest))
    return dp

dp = dijkstra(graph_init, X)
dp_reserve = dijkstra(graph_reverse, X)
max_val = 0

for i in range(len(dp)):
    max_val = max(max_val, dp[i] + dp_reserve[i])

print(max_val)