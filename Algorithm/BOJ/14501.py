N = int(input())
lst = []
dp = [0 for _ in range(N+1)]

for i in range(0, N):
    TP = input().split()
    T, P = int(TP[0]), int(TP[1])
    lst.append((T, P))
for i in range(N):
    for j in range(i+lst[i][0], N+1):
        if dp[j] < dp[i] + lst[i][1]:
            dp[j] = dp[i] + lst[i][1]

print(dp[-1])