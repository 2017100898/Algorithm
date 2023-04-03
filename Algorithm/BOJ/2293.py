cmd = input().split()
n, k = int(cmd[0]), int(cmd[1])

# 동전 정보를 m에 저장
m = []
for i in range(0, n):
    m.append(int(input()))

# k원을 완성하기 위해 필요한 동전 개수를 저장할 dp 선언
dp = [0 for i in range(k+1)]

# 0원을 완성하기 위한 방법은 1개
dp[0] = 1

# 각 동전에 대해 dp[new_coin] = dp[pred_coin] + dp[new_coin - coin의 가치]
# 점화식을 계산해서 dp list 업데이트
for coin in m:
    for new_coin in range(coin, k+1):
        if new_coin >= coin:
            dp[new_coin] += dp[new_coin - coin]

print(dp[k])