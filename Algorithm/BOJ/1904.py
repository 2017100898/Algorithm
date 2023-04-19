# 자연수 N을 입력 받는다.
N = int(input())

# 점화식을 만들기 위해 1, 2, 3 계산
# dp[i] = dp[i-2] + dp[i-1] 임을 확인
if N == 1 :
    print(1)
elif N == 2 :
    print(2)
elif N == 3: 
    print(3)

# N >= 4 일 때는 점화식 계산으로 정답값 출력
else:
    # dp[i-2]
    first = 2
    # dp[i-1]
    second = 3
    
    for i in range(4, N+1):
        # 최종적으로 15746으로 나눈 값을 반환해야하므로 dp[i] = (dp[i-2] + dp[i-1] ) % 15746
        temp = (first + second) % 15746
        # 점화식 계산을 위해 dp[i-2]와 dp[i-1]를 각각 업데이트 해준다
        first, second = second, temp
    
    # N 에 해당하는 dp[i-1] 프린트
    print(second)