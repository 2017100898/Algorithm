cmd = list(map(int, input().split()))
S, a, b, c = cmd[0], cmd[1], cmd[2], cmd[3]

# 조건
# S 곡이 수록될 예정
# 각 곡은 세 사람 중 적어도 한 명이 불러야 됨
# 두 사람이 불러도 되고, 세 사람이 불러도 됨
# 앨범을 만들 수 있는 방법의 수를 구해야 함

# 메모이제이션을 위한 dp
dp = [[[[-1 for _ in range(51)] for _ in range(51)] for _ in range(51)] for _ in range(51)]

# 재귀 돌릴 함수
def function(S, a, b, c):
    # 부를 곡이 모두 소진되었을 때 모든 사람의 할당량이 0인 경우만 결과 + 1
    if S == 0:
        if a == 0 and b == 0 and c == 0:
            return 1
        else:
            return 0
    
    # 한명이라도 음수가 되는 순간 그 재귀는 멈춤
    if a < 0 or b < 0 or c < 0:
        return 0

    # 빠른 계산을 위해 메모이제이션을 참고
    # 계산된 적있는 값은 불러와서 사용
    if dp[S][a][b][c] != -1:
        return dp[S][a][b][c]

    result = 0

    # 곡 하나를 세 사람이 부를 수 있는 경우의 수는 총 7개
    result += function(S - 1, a - 1, b, c)
    result += function(S - 1, a, b - 1, c)
    result += function(S - 1, a, b, c - 1)
    result += function(S - 1, a - 1, b - 1, c)
    result += function(S - 1, a - 1, b, c -1)
    result += function(S - 1, a, b - 1, c - 1)
    result += function(S - 1, a - 1, b - 1, c - 1)

    result %= 1000000007
    
    # 메모이제이션
    dp[S][a][b][c] = result
    return result


result = function(S, a, b, c)
print(result)