N = int(input())

stairs  = list()
dp = [0] * N

# 계단 높이를 입력 받아서 list에 넣음
for i in range(0, N):
    num = int(input())
    stairs.append(num)

# 규칙 : 한번에 한 계단, 두 계단씩 오를 수 있음 (첫 계단은 밟아야 함)
# 연속된 세개를 모두 밟아서는 안됨 (즉, 1-1-2 / 1-2-1 / 2-2 만 가능)
# 마지막 도착 계단 무조건 밟아야 함. (마지막 계단 전, 연속된 두개 계단 밟으면 안됨)

# N=1 일 때는 1개의 계단만 카운트, N>=1일 경우 카운트 후 다음단계 진행
if N>=1 :
    dp[0] = stairs[0]

# N=2 일 때는 1칸, 1칸을 가는 것과 2칸을 한번에 가는 경우 중 큰 값을 카운트
# N>=2 일 때는 카운트 후 다음 단계 진행
if N>=2:
    dp[1] = max(stairs[0] + stairs[1], stairs[1])

# N=3 일 때는 1칸, 2칸을 갔을 경우와 2칸, 1칸을 갔을 경우가 있고 더 큰값 카운트
# N>=3 일때는 카운트 후 다음 단계 진행
if N>=3:
    dp[2] = max(stairs[0]+ stairs[2], stairs[1]+ stairs[2])

# N>=4 일 경우, 전전칸을 밟고 현재 칸을 밟는 경우와 전전전 칸을 밟고, 전 칸을 밟고 현재 칸을 밟는 것 중 큰 값을 카운트
for i in range(3, N):
    dp[i] = max(dp[i-2] + stairs[i], stairs[i-1] + stairs[i] + dp[i-3])


print(dp[N-1])
