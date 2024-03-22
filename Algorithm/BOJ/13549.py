import heapq

n, k = list(map(int, input().split()))

# 위치 x일 때 걸으면 1초후 x-1 또는 x+1로 이동 (거리 1, x-1 / x+1)
# 순간 이동: 0초 후 2*x로 이동 (거리 0, 2*x)
# 동생 찾을 수 있는 가장 빠른 시간은?
INF = 99999999

def dijkstra(start):

    num = max(n, k)

    dp = [INF for _ in range(100001)]
    dp[start] = 0
    Q = [(0, start)]

    while Q:
        curr_dist, curr_dest = heapq.heappop(Q)

        if curr_dist < dp[curr_dest]:
            continue

        graph = [
            (0, 2 * curr_dest),
            (1, curr_dest - 1),
            (1, curr_dest + 1)
        ]

        for next_dist, next_dest in graph:
            if next_dest in range(100001):
                distance = next_dist + curr_dist

                if distance < dp[next_dest]:
                    dp[next_dest] = distance
                    heapq.heappush(Q, (distance, next_dest))

    return dp

dp = dijkstra(n)
print(dp[k])