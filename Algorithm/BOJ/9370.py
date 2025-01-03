import heapq

T = int(input())

def dijkstra(s):
    Q = []
    distance = [999999999999 for _ in range(n + 1)]
    distance[s] = 0
    heapq.heappush(Q, (0, s))

    while Q:
        curr_dist, curr_dest = heapq.heappop(Q)

        if curr_dist > distance[curr_dest]:
            continue

        for next_dest, next_dist in graph[curr_dest]:
            dist = curr_dist + next_dist
            
            if dist < distance[next_dest]:
                distance[next_dest] = dist
                heapq.heappush(Q, (dist, next_dest))

    return distance

for _ in range(T):
    n, m, t = list(map(int, input().split())) #교차로, 도로, 목적지 후보
    s, g, h = list(map(int, input().split())) #출발지, 지나간 도로

    # m 개의 각 줄 마다, 3개의 정수 a, b, d
    # a와 b 사이에 길이 d의 양방향 도로 있다는 뜻

    graph = {}
    for i in range(1, n + 1):
        graph[i] = []

    for _ in range(m):
        a, b, d = list(map(int, input().split()))
        graph[a].append((b, d))
        graph[b].append((a, d))

    s_dist = dijkstra(s)
    g_dist = dijkstra(g)
    h_dist = dijkstra(h)

    final_dest = []

    for _ in range(t):
        x = int(input())
        if s_dist[g] + g_dist[h] + h_dist[x] == s_dist[x] or s_dist[h] + h_dist[g] + g_dist[x] == s_dist[x]:
            final_dest.append(x)

    for val in sorted(final_dest):
        print(val, end = " ")
    
    print()
