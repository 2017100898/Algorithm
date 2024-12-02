N = int(input()) # 기관차가 끌고 가던 객차의 수
arr = list(map(int, input().split())) # 객차의 손님 수
M = int(input()) # 소형 기관차가 끌 수 있는 객차의 수

# prefix sum
prefix_sum = [0]
for i in range(N):
    prefix_sum.append(prefix_sum[-1] + arr[i])

# dynamic programming
dp = [[0 for _ in range(N + 1)] for _ in range(4)]

for i in range(1, 4):
    for j in range(i * M, N + 1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-M] + prefix_sum[j] - prefix_sum[j-M])

print(dp[-1][-1])